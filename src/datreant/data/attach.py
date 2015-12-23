"""
Modifications made to :mod:`datreant` classes on import of module.

"""

import datreant
from . import limbs

datreant.Treant._attach_limb(limbs.Data)
datreant.collections.CollectionBase._attach_limb(limbs.MemberData)
