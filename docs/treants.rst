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

and recall it ::

    >>> s.data['something wicked'].shape
    (1000000, 3)

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
