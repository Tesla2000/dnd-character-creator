from dnd_character_creator.character.blueprint.building_blocks.simplified_builders.simplified_blocks import (
    Classes,
)
from dnd_character_creator.character.blueprint.building_blocks.simplified_builders.simplified_blocks import (
    SimplifiedBlocks,
)
from dnd_character_creator.character.builder import Builder
from dnd_character_creator.character.presentable_character import (
    PresentableCharacter,
)
from dnd_character_creator.choices.class_creation.character_class import Class
from frozendict import frozendict


class TestSimplifiedBuilder:
    def test_default(self):
        classes = Classes(class_levels=frozendict({Class.WIZARD: 16}))
        blocks = SimplifiedBlocks(classes=classes)
        builder = Builder(building_blocks=(blocks,))
        result = builder.build()
        assert result.error is None
        assert isinstance(result.character, PresentableCharacter)
