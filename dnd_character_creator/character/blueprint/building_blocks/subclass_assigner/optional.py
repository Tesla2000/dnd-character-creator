from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner import (
    AnySubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner import (
    SubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.base import (
    CanNotAssign,
)
from dnd_character_creator.choices.class_creation.character_class import (
    AnySubclass,
)


class OptionalAssigner(SubclassAssigner):
    assigner: AnySubclassAssigner

    def _select_subclass(self, blueprint: Blueprint) -> AnySubclass:
        return self.assigner._select_subclass(blueprint)

    def get_change(self, blueprint: Blueprint) -> Blueprint:
        try:
            return super().get_change(blueprint)
        except CanNotAssign:
            return Blueprint()
