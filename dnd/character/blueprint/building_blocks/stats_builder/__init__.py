from typing import Union

from dnd.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd.character.blueprint.state import BlueprintProtocol

AnyStatsBuilder = Union[StandardArray[BlueprintProtocol]]

__all__ = [
    "StandardArray",
    "AnyStatsBuilder",
]
