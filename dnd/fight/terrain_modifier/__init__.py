from enum import IntEnum

from dnd.fight.terrain_modifier._base import _TerrainModifier as TerrainModifier
from dnd.fight.terrain_modifier._ice_storm import (
    _IceStormTerrainModifier as IceStormTerrainModifier,
)
from dnd.fight.terrain_modifier._type import TerrainModifierType

type AnyTerrainModifier[SlotT: IntEnum] = IceStormTerrainModifier[SlotT]

__all__ = [
    "AnyTerrainModifier",
    "IceStormTerrainModifier",
    "TerrainModifier",
    "TerrainModifierType",
]
