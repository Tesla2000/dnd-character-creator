from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generator

from pydantic import ConfigDict

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.skill_proficiency import Skill


class SkillChoiceResolver(BuildingBlock, ABC):
    """Abstract base class for resolving n_skill_choices.

    When a race/class grants skill proficiencies of the player's choice
    (n_skill_choices > 0), this component determines which skills to select
    from the available skills_to_choose_from.

    Subclasses must implement _select_skills to determine the
    selection strategy.
    """

    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def _select_skills(
        self, n: int, available_skills: frozenset[Skill]
    ) -> frozenset[Skill]:
        """Select n skills from available options.

        Args:
            n: Number of skills to select.
            available_skills: Set of skills to choose from.

        Returns:
            Frozenset of n selected skills.
        """
        pass

    def _get_change(
        self, blueprint: Blueprint
    ) -> Blueprint:
        """Apply skill choices based on n_skill_choices."""
        if blueprint.n_skill_choices == 0:
            # No skill choices to resolve, yield empty
            return Blueprint()

        if not blueprint.skills_to_choose_from:
            raise ValueError(
                "skills_to_choose_from must not be empty when n_skill_choices > 0"
            )

        if blueprint.n_skill_choices > len(blueprint.skills_to_choose_from):
            raise ValueError(
                f"Cannot choose {blueprint.n_skill_choices} skills from "
                f"{len(blueprint.skills_to_choose_from)} available skills"
            )

        # Select skills
        selected_skills = self._select_skills(
            blueprint.n_skill_choices, blueprint.skills_to_choose_from
        )

        # Add to existing skill proficiencies
        new_skill_proficiencies = blueprint.skill_proficiencies + tuple(selected_skills)

        return Blueprint(
            skill_proficiencies=new_skill_proficiencies,
            n_skill_choices=0,
            skills_to_choose_from=frozenset(),
        )
