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

    >>> b.categories['amplitude'] = [1, 2, 3, 4]
    >>> for member in b:
    ...    member.data

