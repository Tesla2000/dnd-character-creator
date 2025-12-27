from __future__ import annotations

from abc import ABC

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_priority import (
    StatsPriority,
)


class StatsBuilder(BuildingBlock, ABC):
    stats_priority: StatsPriority
