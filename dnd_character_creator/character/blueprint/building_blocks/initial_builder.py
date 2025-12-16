from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    LevelAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.base_resolver import (
    AllChoicesResolverBase,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.level_up import (
    LevelUp,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.stats_builder import (
    StatsBuilder,
)


class InitialBuilder(CombinedBlock):
    blocks: tuple[
        LevelAssigner,
        StatsBuilder,
        RaceAssigner,
        AllChoicesResolverBase,
        LevelUp,
    ]
