from __future__ import annotations

import random
from typing import Optional

from pydantic import ConfigDict

from dnd_character_creator.character.blueprint.building_blocks.skill_choice_resolver.base import (
    SkillChoiceResolver,
)
from dnd_character_creator.skill_proficiency import Skill


class RandomSkillChoiceResolver(SkillChoiceResolver):
    """Randomly selects skills from available options.

    Provides deterministic randomness when seed is set, useful for
    reproducible character generation.

    Example:
        >>> resolver = RandomSkillChoiceResolver(seed=42)  # Reproducible
        >>> # or
        >>> resolver = RandomSkillChoiceResolver()  # Truly random
    """

    model_config = ConfigDict(frozen=True)

    seed: Optional[int] = None

    def _select_skills(
        self, n: int, available_skills: frozenset[Skill]
    ) -> frozenset[Skill]:
        """Randomly select n skills from available options.

        Args:
            n: Number of skills to select.
            available_skills: Set of skills to choose from.

        Returns:
            Frozenset of n randomly selected skills.
        """
        if self.seed is not None:
            random.seed(self.seed)

        available_list = list(available_skills)
        selected = random.sample(available_list, n)
        return frozenset(selected)