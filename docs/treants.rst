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

Alternatively, we could attach the ``data`` limb to every object it applies for
by doing::

    >>> import datreant.data.attach

If you want explicit control of which objects have this limb, the first
approach is the one to use, but the second one is useful for interactive work.

Storing and retrieving ``numpy`` arrays
=======================================
If
