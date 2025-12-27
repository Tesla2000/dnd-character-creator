from typing import Union

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.ai import (
    AISubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.base import (
    CanNotAssign,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.base import (
    SubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.random import (
    RandomSubclassAssigner,
)
from dnd_character_creator.choices.class_creation.character_class import (
    AnySubclass,
)


class OptionalSubclassAssigner(SubclassAssigner):
    assigner: Union[RandomSubclassAssigner, AISubclassAssigner]

    def _select_subclass(self, blueprint: Blueprint) -> AnySubclass:
        return self.assigner._select_subclass(blueprint)

    def get_change(self, blueprint: Blueprint) -> Blueprint:
        try:
            return super().get_change(blueprint)
        except CanNotAssign:
            return Blueprint()
