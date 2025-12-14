from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.skill_proficiency import Skill
from pydantic import ConfigDict


class SkillProficiencyChoiceResolver(BuildingBlock, ABC):
    """Resolves Skill.ANY_OF_YOUR_CHOICE placeholders.

    This resolver replaces ANY_OF_YOUR_CHOICE placeholders in the
    blueprint's skill_proficiencies set with concrete Skill choices.

    Note: This is different from SkillChoiceResolver which handles
    n_skill_choices from skills_to_choose_from.
    """

    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def _select_from_available(
        self, available: list[Skill], blueprint: Blueprint
    ) -> Skill:
        """Select a skill from available options.

        Args:
            available: List of Skill options excluding ANY_OF_YOUR_CHOICE.
            blueprint: Current character blueprint for context.

        Returns:
            Selected Skill.
        """

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Replace Skill.ANY_OF_YOUR_CHOICE placeholders.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Blueprint with skill proficiency placeholders replaced.
        """
        resolved = set()
        for skill in blueprint.skill_proficiencies:
            if skill == Skill.ANY_OF_YOUR_CHOICE:
                available = [s for s in Skill if s != Skill.ANY_OF_YOUR_CHOICE]
                resolved.add(self._select_from_available(available, blueprint))
            else:
                resolved.add(skill)
        return Blueprint(skill_proficiencies=resolved)
