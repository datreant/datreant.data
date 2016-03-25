==============================================
Storing and retrieving datasets within Treants
==============================================
The functionality of a :class:`~datreant.core.Treant` can be expanded to
conveniently store ``numpy`` and ``pandas`` objects in a couple different ways. 
If we have an existing Treant::

    >>> import datreant.core as dtr
    >>> s = dtr.Treant('sequoia')
    >>> s
    <Treant: 'sequoia'>

We can attach the :class:`~datreant.data.limbs.Data` limb to only this instance
with::

    >>> import datreant.data
    >>> s.attach('data')
    >>> s.data
    <Data([])>

Alternatively, we could attach the :class:`~datreant.data.limbs.Data` and
:class:`~datreant.data.agglimbs.AggData` limbs to every object they apply for
by doing::

    >>> import datreant.data.attach

If you want explicit control of which objects have this limb, the first
approach is the one to use, but the second one is useful for interactive work.

Storing and retrieving ``numpy`` arrays
=======================================
Perhaps we have generated a `numpy <http://www.numpy.org/>`_ array of dimension
(10^6, 3) that we wish to have easy access to later ::

    >>> import numpy as np
    >>> a = np.random.randn(1000000, 3)
    >>> a.shape
    (1000000, 3)

We can store this easily ::

    >>> s.data['something wicked'] = a 
    >>> s.data
    <Data(['something wicked'])>

Looking at the contents of the directory ``sequoia``, we see it has a new
subdirectory corresponding to the name of our stored dataset ::

    >>> s.draw()
    sequoia/
     +-- something wicked/
     |   +-- npData.h5
     +-- Treant.608f7463-5063-450a-96eb-c5c93f16dc32.json

and inside of this is a new HDF5 file (``npData.h5``). Our ``numpy`` array is
stored inside, and we can recall it just as easily as we stored it::

    >>> s.data['something wicked']
    array([[ 0.49884872, -0.30062622,  0.64513512],
           [-0.12839311,  0.68467086, -0.96125085],
           [ 0.36655902, -0.13178154, -0.58137863],
           ..., 
           [-0.20229488, -0.30303892,  1.44345568],
           [ 0.10119334, -0.50691484,  0.05854653],
           [-2.0551924 ,  0.80378532, -0.28869459]])


Storing and retrieving ``pandas`` objects
=========================================
`pandas <http://pandas.pydata.org/>`_ is the *de facto* standard for working
with tabular data in Python. It's most-used objects, the
:class:`~pandas.Series` and :class:`~pandas.DataFrame` are just as easily
stored as ``numpy`` arrays. If we have a DataFrame we wish to store::

    >>> import pandas as pd
    >>> df = pd.DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C'])
    >>> df.head()
              A         B         C
    0 -0.474337 -1.257253  0.497824
    1 -1.057806 -1.393081  0.628394
    2  0.063369 -1.820173 -1.178128
    3 -0.747949  0.607452 -1.509302
    4 -0.031547 -0.680997  1.127573

then as you can expect, we can store it with::

    >>> s.data['something terrible'] = df

and recall it with::

    >>> s.data['something terrible'].head()
              A         B         C
    0 -0.474337 -1.257253  0.497824
    1 -1.057806 -1.393081  0.628394
    2  0.063369 -1.820173 -1.178128
    3 -0.747949  0.607452 -1.509302
    4 -0.031547 -0.680997  1.127573

Our data is stored in its own HDF5 file (``pdData.h5``) in the subdirectory we
specified, so now our Treant looks like this::

    s.draw()
    sequoia/
     +-- something wicked/
     |   +-- npData.h5
     +-- Treant.608f7463-5063-450a-96eb-c5c93f16dc32.json
     +-- something terrible/
         +-- pdData.h5

Alternatively, we can use the :meth:`~datreant.data.limbs.Data.add` method to
store datasets::

    >>> s.data.add('something terrible')

but the effect is the same. Since internally this uses the `pandas.HDFStore`_
class for storing pandas objects, all limitations for the types of indexes and
objects it can store apply.

.. _pandas.HDFStore: http://pandas.pydata.org/pandas-docs/stable/api.html#hdfstore-pytables-hdf5

Appending to existing data
--------------------------
Sometimes we may have code that will generate a :class:`~pandas.Series` or
:class:`~pandas.DataFrame` that is rather large, perhaps larger than our
machine's memory. In these cases we can
:meth:`~datreant.data.limbs.Data.append` to an existing store instead of writing
out a single, huge DataFrame all at once::

    >>> s.data['something terrible'].shape     # before
    (1000, 3)

    >>> df2 = pd.DataFrame(np.random.randn(2000, 3), columns=['A', 'B', 'C'])
    >>> s.data.append('something terrible', df2)
    >>> s.data['something terrible'].shape     # after
    (3000, 3)

Have code that will generate a DataFrame with 10^8 rows? No problem::
    
    >>> for i in range(10**2):
    ...    a_piece = pd.DataFrame(np.random.randn(10**6, 3),
                                  columns=['A', 'B', 'C'])

           s.data.append('something enormous', a_piece)

Note that the :class:`~pandas.DataFrame` appended must have the same column
names and dtypes as that already stored, and that only rows can be appended,
not columns. For :class:`pandas.Series` objects the dtype must match. 
Appending of :class:`pandas.Panel` objects also works, but the limitations are
more stringent. See the `pandas HDFStore documentation`_ for more details on
what is technically possible.

.. _pandas HDFStore documentation: http://pandas.pydata.org/pandas-docs/stable/io.html#hdf5-pytables

Retrieving subselections
------------------------
For pandas stores that are very large, we may not want or be able to pull the
full object into memory. 

Bonus: storing anything pickleable
==================================


Deleting datasets
=================

