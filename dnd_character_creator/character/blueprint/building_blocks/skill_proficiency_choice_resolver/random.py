from __future__ import annotations

import random
from typing import Optional

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.skill_proficiency_choice_resolver.base import (
    SkillProficiencyChoiceResolver,
)
from dnd_character_creator.skill_proficiency import Skill
from pydantic import ConfigDict


class RandomSkillProficiencyChoiceResolver(SkillProficiencyChoiceResolver):
    """Randomly selects skills for ANY_OF_YOUR_CHOICE placeholders.

    Provides deterministic randomness when seed is set, useful for
    reproducible character generation.

    Example:
        >>> resolver = RandomSkillProficiencyChoiceResolver(seed=42)
        >>> # or
        >>> resolver = RandomSkillProficiencyChoiceResolver()  # Truly random
    """

    model_config = ConfigDict(frozen=True)

    seed: Optional[int] = None

    def _select_from_available(
        self, available: list[Skill], _: Blueprint
    ) -> Skill:
        """Randomly select a skill from available options.

        Args:
            available: List of Skill options to choose from.
            blueprint: Current character blueprint (unused in random selection).

        Returns:
            Randomly selected Skill.
        """
        if self.seed is not None:
            random.seed(self.seed)

        return random.choice(available)
