from __future__ import annotations

from typing import Generator

from frozendict import frozendict

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.choices.class_creation.character_class import Class


class ClassAssigner(BuildingBlock):
    """Adds one level to a specific class.

    Increments the level for the specified class by 1. Validates that total
    character level doesn't exceed the blueprint's level field.

    Example:
        >>> builder = Builder([
        ...     LevelAssigner(level=10),
        ...     ClassAssigner(class_=Class.FIGHTER),  # +1 level
        ...     ClassAssigner(class_=Class.FIGHTER),  # +1 level
        ...     ClassAssigner(class_=Class.WIZARD),   # +1 level
        ... ])  # Character at level 10 with 2 Fighter / 1 Wizard (7 unused levels)
    """

    class_: Class

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Add one level to the class, validating total level.

        Yields:
            Blueprint with updated classes.

        Raises:
            ValueError: If total levels would exceed character level.
        """
        # Get existing classes or empty dict
        existing_classes = dict(blueprint.classes)

        # Add one level to the class
        current_class_level = existing_classes.get(self.class_, 0)
        existing_classes[self.class_] = current_class_level + 1

        # Validate total levels don't exceed character level
        total_class_levels = sum(existing_classes.values())
        character_level = blueprint.level if blueprint.level is not None else 0

        if total_class_levels > character_level:
            raise ValueError(
                f"Total class levels ({total_class_levels}) would exceed "
                f"character level ({character_level}). "
                f"Set character level first with LevelAssigner."
            )

        yield Blueprint(classes=frozendict(existing_classes))