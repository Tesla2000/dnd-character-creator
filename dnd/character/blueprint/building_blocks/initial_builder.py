from __future__ import annotations

from collections.abc import Generator
from typing import Literal

from dnd.character.blueprint.building_blocks.all_choices_resolver import (
    AnyChoiceResolver,
)
from dnd.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd.character.blueprint.building_blocks.level_assigner import (
    LevelAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner import (
    AnyRaceAssigner,
)
from dnd.character.blueprint.building_blocks.stats_builder import (
    AnyStatsBuilder,
)
from dnd.character.blueprint.state import BlueprintProtocol
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.delta.delta import Delta


class InitialBuilder(BuildingBlock):
    """Building block that performs initial character generation.

    Combines level assignment, ability score building, race selection,
    and choice resolution into a single orchestrated process.
    """

    type: Literal[BuildingBlockType.INITIAL_BUILDER] = BuildingBlockType.INITIAL_BUILDER

    level_assigner: LevelAssigner
    stats_builder: AnyStatsBuilder
    race_assigner: AnyRaceAssigner
    all_choices_resolver: AnyChoiceResolver

    def flatten(self) -> Generator[BuildingBlock]:
        for block in (
            self.level_assigner,
            self.stats_builder,
            self.race_assigner,
            self.all_choices_resolver,
        ):
            yield from block.flatten()

    def get_change(
        self, state: BlueprintProtocol
    ) -> Generator[Delta, None, BlueprintProtocol]:
        current: BlueprintProtocol = state
        for block in self.flatten():
            current = yield from block.get_change(current)
        return current
