from typing import Generator

from frozendict import frozendict

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks import \
    BuildingBlock
from dnd_character_creator.choices.class_creation.character_class import Class


class LevelIncrementer(BuildingBlock):
    class_: Class

    def get_change(self, blueprint: Blueprint) -> Generator[
        Blueprint, Blueprint, None]:
        existing_classes = dict(blueprint.classes)

        # Add one level to the class
        current_class_level = existing_classes.get(self.class_, 0)
        existing_classes[self.class_] = current_class_level + 1

        # Validate total levels don't exceed character level
        total_class_levels = sum(existing_classes.values())
        character_level = blueprint.level or 0

        if total_class_levels > character_level:
            raise ValueError(
                f"Total class levels ({total_class_levels}) would exceed "
                f"character level ({character_level}). "
                f"Set character level first with LevelAssigner."
            )

        yield Blueprint(classes=frozendict(existing_classes))