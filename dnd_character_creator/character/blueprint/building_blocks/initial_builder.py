from __future__ import annotations

from typing import NamedTuple

from dnd_character_creator.character.blueprint.building_blocks import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    LevelAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.base_resolver import (
    AllChoicesResolverBase,
)
from dnd_character_creator.character.blueprint.building_blocks.race_assigner import (
    BaseRaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.stats_builder import (
    StatsBuilder,
)


class InitialBuilderBlocks(NamedTuple):
    level_assigner: LevelAssigner
    stats_builder: StatsBuilder
    race_assigner: BaseRaceAssigner
    all_choices_resolver: AllChoicesResolverBase


class InitialBuilder(CombinedBlock):
    blocks: InitialBuilderBlocks
