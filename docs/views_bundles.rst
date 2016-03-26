===========================================
Aggregating datasets with Views and Bundles
===========================================
Just as Treants and Trees have the :class:`~datreant.data.limbs.Data` limb 
for storing and retrieving datasets in their filesystem trees, the
:class:`~datreant.core.View` and :class:`~datreant.core.Bundle` objects also
have the :class:`~datreant.data.agglimbs.AggData` limb for accessing these
datasets in aggregate.

Given a directory with four Treants ::

    > ls
    elm/  maple/  oak/  sequoia/

we'll gather these up in a Bundle ::

    >>> import datreant.core as dtr
    >>> import glob
    >>> b = dtr.Bundle(glob.glob('*'))
    >>> b
    <Bundle([<Treant: 'sequoia'>, <Treant: 'maple'>, <Treant: 'oak'>, <Treant: 'elm'>])>

and then attach the :class:`~datreant.data.limbs.AggData` limb to only this
Bundle instance with::

    >>> import datreant.data
    >>> b.attach('data')

.. note:: Attaching a limb like :class:`~datreant.data.agglimbs.AggData` to a
          Bundle or View with the :meth:`~datreant.core.Bundle.attach` method
          will attach the required limb to each member instance. In this case,
          each member gets a :class:`~datreant.data.limbs.Data` limb.

and so we can now do::

    >>> b.data
    <AggData([])>

This tells us that there are no datasets with the same key within every member
of the Bundle. So, let's make something that does. Let's build a "dataset" that
gives us a sinusoid based on a characteristic of each Treant in the Bundle::

    >>> import numpy as np
    >>> b.categories['frequency'] = [1, 2, 3, 4]
    >>> for member in b:
    ...     member.data['sinusoid/array'] = np.sin(
    ...         member.categories['frequency'] * np.linspace(0, 8*np.pi,
    ...                                                      num=200))

So now if we do::

    >>> b.data
    <AggData(['sinusoid/array'])>

we see we now have a dataset name in common among all members. If we recall
it ::

    >>> sines = b.data['sinusoid/array']
    >>> type(sines)
    dict

we get back a dictionary with the full path to each member as keys::

    >>> sines.keys()
    ['/bob/research/arborea/sequoia/',
     '/bob/research/arborea/oak/',
     '/bob/research/arborea/elm/',
     '/bob/research/arborea/maple/']

and the values are the :`numpy` arrays we stored for each member. If we'd
rather get back a dictionary with names instead of paths, we could do that
with the :meth:`~datreant.data.agglimbs.AggData.retrieve` method::

    >>> b.data.retrieve('sinusoid/array', by='name').keys()
    ['sequoia', 'oak', 'maple', 'elm']

Getting uuids as the keys is also possible, and is often useful since these
will be unique among Treants, while names (and in some cases, paths) are
generally not.


MultiIndex aggregation for ``pandas`` objects
=============================================
:mod:`numpy` arrays or pickled datasets are always retrieved in aggregate as
dictionaries, since this is the simplest way of aggregating these objects while
retaining the ability to identify datasets from individual members. Aggregation
is most useful, however, for :mod:`pandas` objects, since for these we can
naturally build versions of the same data structure with an additional index
for data membership.

We'll make a :class:`pandas.Series` version of the same dataset we stored
before::

    >>> import pandas as pd
    >>> for member in b:
    ...     member.data['sinusoid/series'] = pd.Series(member.data['sinusoid/array'])

So now when we retrieve this aggregated dataset by name, we get a series with
an outermost index of member names::

    >>> sines = b.data.retrieve('sinusoid/series', by='name')
    >>> sines.groupby(level=0).head()
    sequoia  0    0.000000
             1    0.125960
             2    0.249913
             3    0.369885
             4    0.483966
    oak      0    0.000000
             1    0.369885
             2    0.687304
             3    0.907232
             4    0.998474
    maple    0    0.000000
             1    0.249913
             2    0.483966
             3    0.687304
             4    0.847024
    elm      0    0.000000
             1    0.483966
             2    0.847024
             3    0.998474
             4    0.900479
    dtype: float64

So we can immediately use this for aggregated analysis, or perhaps just pretty
plots::

    >>> for name, group in sines.groupby(level=0):
    ...     group.reset_index(level=0, drop=True).plot(legend=True, label=name) 

.. image:: _static/images/sines.png


Subselection with Views
=======================


API reference: AggData
======================
See the :ref:`AggData_api` API reference for more details.
