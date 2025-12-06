from DND_character_creator.character.building_blocks.building_block import \
    BuildingBlock
from DND_character_creator.character.character import Character
from DND_character_creator.choices.class_creation.character_class import \
    Class


class ClassAssigner(BuildingBlock):
    class_: Class

    def apply(self, character: Character) -> None:
        character.classes