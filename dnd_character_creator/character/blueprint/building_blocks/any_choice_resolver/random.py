from __future__ import annotations

import random
from typing import Optional
from typing import TypeVar

from dnd_character_creator.character.blueprint.building_blocks.any_choice_resolver.base import (
    AnyChoiceResolver,
)
from pydantic import ConfigDict

T = TypeVar("T")


class RandomAnyChoiceResolver(AnyChoiceResolver):
    """Randomly selects concrete values for ANY_OF_YOUR_CHOICE placeholders.

    Provides deterministic randomness when seed is set, useful for
    reproducible character generation.

    Example:
        >>> resolver = RandomAnyChoiceResolver(seed=42)  # Reproducible
        >>> # or
        >>> resolver = RandomAnyChoiceResolver()  # Truly random
    """

    model_config = ConfigDict(frozen=True)

    seed: Optional[int] = None

    def _select_from_available(self, available: list[T]) -> T:
        """Randomly select an item from available options.

        Args:
            available: List of options to choose from.

        Returns:
            Randomly selected item.
        """
        if self.seed is not None:
            random.seed(self.seed)

        return random.choice(available)
