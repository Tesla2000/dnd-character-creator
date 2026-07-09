from __future__ import annotations

from typing import Literal

from dnd.character.blueprint.building_blocks.all_choices_resolver import (
    AnyChoiceResolver,
)
from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.level_assigner import LevelAssigner
from dnd.character.blueprint.building_blocks.race_assigner import AnyRaceAssigner
from dnd.character.blueprint.building_blocks.stats_builder import AnyStatsBuilder
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.building_block import _WideBlueprint


class InitialBuilder(BuildingBlock):
    """Combines level assignment, stats, race, and choice resolution."""

    type: Literal[BuildingBlockType.INITIAL_BUILDER] = BuildingBlockType.INITIAL_BUILDER

    level_assigner: LevelAssigner
    stats_builder: AnyStatsBuilder
    race_assigner: AnyRaceAssigner
    all_choices_resolver: AnyChoiceResolver

    def apply(self, blueprint: _WideBlueprint) -> _WideBlueprint:
        r1 = self.level_assigner.apply(blueprint)
        r2 = self.stats_builder.apply(r1)
        r3 = self.race_assigner.apply(r2)
        return self.all_choices_resolver.apply(r3)
