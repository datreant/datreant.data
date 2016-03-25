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
    ...                           columns=['A', 'B', 'C'],
    ...                           index=pd.Int64Index(np.arange(10**6) + i*10**6))
    ...
    ...    s.data.append('something enormous', a_piece)

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
full object into memory. For these cases we can use
:meth:`~datreant.data.limbs.Data.retrieve` to get subselections of our data.
Taking our large 10^8 row DataFrame, we can get at rows 1000000 to 2000000
with something like::

    >>> s.data.retrieve('something enormous', start=10000000, stop=2000000).shape
    (1000000, 3)

If we only wanted columns 'B' and 'C', we could get only those, too::

    >>> s.data.retrieve('something enormous', start=10000000, stop=2000000,
    ...                 columns=['B', 'C']).shape
    (1000000, 2)

These operations are performed "out-of-core", meaning that the full dataset is
never read entirely into memory to get back the result of our subselection.

Retrieving from a query
-----------------------
For large datasets it can also be useful to retrieve only rows that match some
set of conditions. We can do this with the ``where`` keyword, for example
getting all rows for which column 'A' is less than -2::

    >>> s.data.retrieve('something enormous', where="A < -2").head()
                     A         B         C
    131      -2.177729 -0.797003  0.401288
    134      -2.017321  0.750593 -1.366106
    198      -2.203170 -0.670188  0.494191
    246      -2.156695  1.107288 -0.065875
    309      -2.334792  0.984636  0.006232
    321      -3.784861 -1.222399  0.038717
    346      -2.057103 -0.230953  0.732774
    364      -2.418875  0.250880 -0.850418
    413      -2.528563 -0.261624  1.233367
    480      -2.205484  0.036570  0.501868

.. note:: Since our data is randomly generated in this example, the rows you get running
          the same example will be different.

Or perhaps when both column 'A' is less than -2 and column 'C' is greater than 2::

    >>> s.data.retrieve('something enormous', where="A < -2 & C > 2").head()
                     A         B         C
    1790     -3.103821 -0.616780  2.714530
    5635     -2.431589 -0.580400  3.163408
    7664     -2.364559  0.304764  2.884965
    9208     -2.569256  1.105211  2.008396
    9487     -2.028096  0.146484  2.234081
    9968     -2.362063  0.544276  2.469602
    11503    -2.494900 -0.005465  2.487311
    12725    -2.353478 -0.001569  2.274861
    14991    -2.129492 -1.889708  2.324640
    15178    -2.327528  1.852786  2.425977

See the documentation for `querying`_ with :meth:`pandas.HDFStore.select` for
more information on the range of possibilities for the ``where`` keyword.

.. _querying: http://pandas.pydata.org/pandas-docs/stable/io.html#querying-a-table

Bonus: storing anything pickleable
==================================


Deleting datasets
=================

