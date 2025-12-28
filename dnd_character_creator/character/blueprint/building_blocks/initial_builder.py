from __future__ import annotations

from typing import NamedTuple

from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver import (
    AnyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.level_assigner import (
    LevelAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.race_assigner import (
    AnyRaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_builder import (
    AnyStatsBuilder,
)
from pydantic import Field


class InitialBuilderBlocks(NamedTuple):
    level_assigner: LevelAssigner
    stats_builder: AnyStatsBuilder
    race_assigner: AnyRaceAssigner
    all_choices_resolver: AnyChoiceResolver


class InitialBuilder(CombinedBlock):
    input_blocks: InitialBuilderBlocks = Field(alias="blocks")
