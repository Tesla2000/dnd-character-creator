from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd_character_creator.character.blueprint.blueprint import Blueprint

from dnd_character_creator.character.feature.feature import Feature
from dnd_character_creator.skill_proficiency import Skill


class SkillProficiencyFeature(Feature):
    """A feature that grants proficiency in one or more skills.

    Examples:
        - Skill Expert feat
        - Background features that grant skills
        - Class features that grant skill proficiencies
    """

    skills: frozenset[Skill]

    def assign_to(self, blueprint: Blueprint) -> Blueprint:
        """Add skill proficiencies to the character.

        Adds the skills to the character's skill_proficiencies and
        records the feature in other_active_abilities.
        """
        # Blueprint uses tuple for skill_proficiencies, so convert frozenset to tuple
        existing_skills = set(blueprint.skill_proficiencies)
        new_skills = existing_skills | self.skills
        new_skill_proficiencies = tuple(new_skills)

        return type(blueprint)(
            skill_proficiencies=new_skill_proficiencies,
            other_active_abilities=blueprint.other_active_abilities
            + (f"{self.name}: {self.description}",),
        )
