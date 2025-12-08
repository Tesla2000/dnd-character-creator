"""Random subclass assigner for character creation."""

from __future__ import annotations

import random
from typing import Optional

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.base import (
    SubclassAssigner,
)
from dnd_character_creator.choices.class_creation.character_class import (
    AnySubclass,
)
from dnd_character_creator.choices.class_creation.character_class import (
    subclasses,
)
from pydantic import ConfigDict


class RandomSubclassAssigner(SubclassAssigner):
    """Randomly selects a subclass from available options.

    Provides deterministic randomness when seed is set, useful for
    reproducible character generation.

    Example:
        >>> from dnd_character_creator.choices.class_creation.character_class import Class
        >>> assigner = RandomSubclassAssigner(
        ...     class_=Class.WIZARD,
        ...     seed=42  # Reproducible
        ... )
        >>> # or
        >>> assigner = RandomSubclassAssigner(class_=Class.WIZARD)  # Truly random
    """

    model_config = ConfigDict(frozen=True)

    seed: Optional[int] = None

    def _select_subclass(self, blueprint: Blueprint) -> AnySubclass:
        """Randomly select a subclass for the character's class.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Randomly selected subclass.
        """
        if self.seed is not None:
            random.seed(self.seed)

        # Get all available subclasses for this class
        subclass_enum = subclasses[self.class_]
        available_subclasses = list(subclass_enum)

        # Randomly select one
        return random.choice(available_subclasses)
