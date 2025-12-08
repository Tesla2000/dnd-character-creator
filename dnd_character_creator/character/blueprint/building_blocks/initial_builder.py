from dnd_character_creator.character.blueprint.building_blocks import \
    CombinedBlock, LevelAssigner, RaceAssigner
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver import \
    AllChoicesResolver
from dnd_character_creator.character.blueprint.building_blocks.level_up.level_up import \
    LevelUp
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.standar_array import \
    StandardArray
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.stats_builder import \
    StatsBuilder

class InitialBuilder(CombinedBlock):
    blocks: tuple[LevelAssigner, StatsBuilder, RaceAssigner, AllChoicesResolver, LevelUp]
