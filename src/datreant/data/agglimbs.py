"""
AggLimbs for convenient Treant data storage and retrieval.

"""
import six
import pandas as pd

from datreant.core.agglimbs import AggLimb


class AggData(AggLimb):
    """Manipulators for collection data.

    """
    _name = 'data'

    def __repr__(self):
        return "<AggData({})>".format(self.keys(mode='all'))

    def _repr_html_(self):
        data = self.keys(mode='all')
        agg = "Data"
        if not data:
            out = "No Data"
        else:
            out = "<h3>{}</h3>".format(agg)
            out = out + "<ul style='list-style-type:none'>"
            for datum in data:
                out = out + "<li>{}</li>".format(datum)
            out = out + "</ul>"
        return out

    def __getitem__(self, handle):
        """Retrieve aggreggated dataset from all members.

        Returns datasets indexed according to member uuids.
        See :meth:`AggData.retrieve` for more information.

        Raises :exc:`KeyError` if dataset doesn't exist for any members.

        :Arguments:
            *handle*
                name of data to retrieve; may also be a list of names

        :Returns:
            *data*
                aggregated data, indexed by member name; if *handle* was a
                list, will be a list of equal length with the aggregated
                datasets as members

        """
        if isinstance(handle, list):
            out = list()
            for item in handle:
                out.append(self.retrieve(item, by='uuid'))
        elif isinstance(handle, six.string_types):
            out = self.retrieve(handle, by='uuid')

        return out

    def keys(self, mode='all'):
        """List available datasets.

        :Arguments:
            *mode*
                'any' returns a list of all handles present in at least one
                member; 'all' returns only handles that are present in all
                members

        :Returns:
            *handles*
                list of handles to available datasets

        """
        datasets = [set(member.data) for member in self._collection]
        if mode == 'any':
            out = set.union(*datasets)
        elif mode == 'all':
            out = set.intersection(*datasets)

        out = list(out)
        out.sort()

        return out

    def any(self):
        return keys('any')

    def all(self):
        return keys('all')

    def retrieve(self, handle, by='uuid', **kwargs):
        """Retrieve aggregated dataset from all members.

        This is a convenience method. The stored data structure for each member
        is read from disk and aggregated. The aggregation scheme is dependent
        on the form of the data structures pulled from each member:

        pandas DataFrames or Series
            the structures are appended together, with a new level added
            to the index giving the member (see *by*) each set of rows
            came from

        pandas Panel or Panel4D, numpy arrays, pickled python objects
            the structures are returned as a dictionary, with keys giving
            the member (see *by*) and each value giving the corresponding
            data structure

        This method tries to do smart things with the data it reads from each
        member. In particular:
            - members for which there is no data with the given handle are
              skipped
            - the lowest-common-denominator data structure is output; this
              means that if all data structures read are pandas DataFrames,
              then a multi-index DataFrame is returned; if some structures are
              pandas DataFrames, while some are anything else, a dictionary is
              returned

        :Arguments:
            *handle*
                name of data to retrieve

        :Keywords:
            *by*
                top-level index of output data structure; 'name' uses member
                names, 'uuid' uses member uuids; if names are not unique,
                it is better to go with 'uuid' ['uuid']

        See :meth:`Data.retrieve` for more information on keyword usage.

        :Keywords for pandas data structures:
            *where*
                conditions for what rows/columns to return
            *start*
                row number to start selection
            *stop*
                row number to stop selection
            *columns*
                list of columns to return; all columns returned by default
            *iterator*
                if True, return an iterator [``False``]
            *chunksize*
                number of rows to include in iteration; implies
                ``iterator=True``

        :Returns:
            *data*
                aggregated data structure

        """
        def dict2multiindex(agg):
            agg_mi = None
            for member in agg:
                d = agg[member]
                label = len(d.index)*[member]
                index = pd.MultiIndex.from_arrays([label, d.index])
                d.index = index

                if agg_mi is not None:
                    agg_mi = agg_mi.append(d)
                else:
                    agg_mi = d

            return agg_mi

        # first, check for existence in any member
        if handle not in self.keys('any'):
            raise KeyError(
                    "No dataset '{}' found in any member".format(handle))

        # get indexer from *by* keyword
        if by == 'uuid':
            def get_index(member): return member.uuid
        elif by == 'name':
            def get_index(member): return member.name
            names = [member.name for member in self._collection]
            if len(set(names)) != len(names):
                raise KeyError(
                        "Member names not unique; data structure may not"
                        " look as expected. Set `by` to 'uuid' to avoid this.")
        else:
            raise ValueError(
                    "*by* keyword must be either 'name' or 'uuid'")

        # first, collect all the data into a dictionary, the
        # lowest-common-denominator aggregation structure
        agg = dict()
        for member in self._collection:
            try:
                agg[get_index(member)] = member.data.retrieve(handle, **kwargs)
            except KeyError:
                pass

        # if data are all Series or all DataFrames, we build a multi-index
        # Series or DataFrame (respectively)
        all_s = all([isinstance(d, pd.Series) for d in agg.values()])
        all_df = all([isinstance(d, pd.DataFrame) for d in agg.values()])

        if all_s or all_df:
            agg = dict2multiindex(agg)

        return agg
