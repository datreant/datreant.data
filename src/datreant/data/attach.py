"""
Modifications made to :mod:`datreant` classes on import of module.

"""

from datreant.core import Tree, Bundle
from . import limbs
from . import agglimbs

Tree._attach_limb_class(limbs.Data)
Bundle._attach_agglimb_class(agglimbs.MemberData)
