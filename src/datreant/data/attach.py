"""
Modifications made to :mod:`datreant` classes on import of module.

"""

from datreant.core import Treant
from datreant.core.collections import CollectionBase
from . import limbs
from . import agglimbs

Treant._attach_limb_class(limbs.Data)
CollectionBase._attach_agglimb_class(agglimbs.MemberData)
