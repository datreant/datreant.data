"""
Modifications made to :mod:`datreant` classes on import of module.

"""

import datreant.core
from . import limbs

datreant.core.Treant._attach_limb(limbs.Data)
datreant.core.collections.CollectionBase._attach_limb(limbs.MemberData)
