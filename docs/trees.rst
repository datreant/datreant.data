=================================
Using Trees to subselect datasets
=================================
The :class:`~datreant.data.limbs.Data` limb isn't just for Treants; it works
for :class:`~datreant.core.Tree` objects as well. So we could use our
Treant 'sequoia' directly as a Tree instead of a Treant if we wanted::

    >>> import datreant.core as dtr
    >>> import datreant.data
    >>> t = dtr.Tree('sequoia/')
    >>> t.attach('data')
    >>> t.data
    <Data(['a grocery list', 'something enormous', 'something wicked'])>

and it would work all the same. This behavior is most useful, however, when
nesting datasets.

Nesting within a tree
=====================
Dataset names are their paths downward relative to the Tree/Treant they are
called from, so we can store a dataset like::

    >>> t.data['a/better/grocery/list'] = ['ham', 'eggs', 'steak']
    >>> t.data
    <Data(['a grocery list', 'a/better/grocery/list', 'something enormous', 'something wicked'])>

and this creates the directory structure you might expect::

    >>> t.draw()
    sequoia/
     +-- a grocery list/
     |   +-- pyData.pkl
     +-- Treant.608f7463-5063-450a-96eb-c5c93f16dc32.json
     +-- something enormous/
     |   +-- pdData.h5
     +-- a/
     |   +-- better/
     |       +-- grocery/
     |           +-- list/
     |               +-- pyData.pkl
     +-- something wicked/
         +-- npData.h5

This allows us to group together related datasets in a natural way, as we would
probably do even if we weren't using :mod:`datreant` objects. So if we had several
shopping lists, we might put them under a directory of their own::

    >>> t.data['shopping lists/food'] = ['milk', 'ham', 'eggs', 'steak']
    >>> t.data['shopping lists/clothes'] = ['shirts', 'pants', 'shoes']
    >>> t.data['shopping lists/misc'] = ['dish soap']
    
which would give us::

    >>> t['shopping lists'].draw()
    shopping lists/
     +-- misc/
     |   +-- pyData.pkl
     +-- food/
     |   +-- pyData.pkl
     +-- clothes/
         +-- pyData.pkl

and we could always get them back easily enough::

    >>> t.data['shopping lists/food']
    ['milk', 'ham', 'eggs', 'steak']


Trees as subselections
======================
But since Trees can access datasets inside them, we could work more directly
with our shopping lists by using the 'shopping lists' Tree ::

   >>> lets_go_shopping = t['shopping lists'] 
   >>> lets_go_shopping.data
    <Data(['clothes', 'food', 'misc'])>

and now selecting is a bit less verbose::

    >>> lets_go_shopping['food']
    ['milk', 'ham', 'eggs', 'steak']
