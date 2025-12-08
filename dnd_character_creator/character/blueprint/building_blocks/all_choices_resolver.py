from dnd_character_creator.character.blueprint.building_blocks import \
    CombinedBlock, AnyChoiceResolver, StatChoiceResolver, SkillChoiceResolver
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser.base import \
    EquipmentChooser
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler.base_filler import \
    InitialDataFiller


class AllChoicesResolver(CombinedBlock):
    blocks: tuple[AnyChoiceResolver, StatChoiceResolver, SkillChoiceResolver, InitialDataFiller, EquipmentChooser]