"""AI-powered skill proficiency choice resolver."""

from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.blueprint_formatter import (
    BlueprintFormatter,
)
from dnd_character_creator.character.blueprint.building_blocks.skill_proficiency_choice_resolver.base import (
    SkillProficiencyChoiceResolver,
)
from dnd_character_creator.skill_proficiency import Skill
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from pydantic import Field


class SkillProficiencySelection(BaseModel):
    """Schema for AI to select skill proficiency replacements."""

    skill_proficiencies: set[Skill] = Field(default_factory=set)


class AISkillProficiencyChoiceResolver(SkillProficiencyChoiceResolver):
    """AI-powered resolver for Skill.ANY_OF_YOUR_CHOICE placeholders.

    Uses an LLM to make intelligent skill selections based on
    character context (race, background, class, etc.).

    Example:
        >>> resolver = AISkillProficiencyChoiceResolver(
        ...     llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
        ... )
    """

    llm: ChatOpenAI

    formatter: BlueprintFormatter = Field(
        default_factory=BlueprintFormatter,
        description="Blueprint formatter for creating AI prompts",
    )

    def _select_from_available(
        self, available: list[Skill], _: Blueprint
    ) -> Skill:
        """Not used in AI implementation - overrides _get_change instead."""
        raise NotImplementedError(
            "AISkillProficiencyChoiceResolver overrides _get_change directly"
        )

    def _build_prompt(self, blueprint: Blueprint) -> str:
        """Build a prompt for AI skill proficiency selection.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Formatted prompt string.
        """
        system_prompt = (
            "You are resolving Skill.ANY_OF_YOUR_CHOICE placeholders "
            "for a D&D 5e character.\n"
            "Replace each placeholder with the most appropriate skill "
            "based on the character's race, class, background, and concept.\n"
        )

        character_description = self.formatter.format(
            blueprint, system_prompt=system_prompt
        )

        instructions = ["\n## Placeholders to Resolve\n"]

        # Count skill placeholders
        count = list(blueprint.skill_proficiencies).count(
            Skill.ANY_OF_YOUR_CHOICE
        )
        if count == 0:
            return ""  # No placeholders to resolve

        instructions.append(
            f"Skill Proficiencies: {count} ANY_OF_YOUR_CHOICE "
            f"placeholder(s) to replace"
        )
        instructions.append(
            f"  Available: {', '.join(s.value for s in Skill if s != Skill.ANY_OF_YOUR_CHOICE)}"
        )

        instructions.append(
            "\n## Selection Instructions\n"
            "Return the complete skill proficiency set with placeholders "
            "replaced by specific choices.\n"
            "Choose skills that best fit the character's class, "
            "background, and concept.\n"
            "Avoid duplicates unless the character already has them."
        )

        return character_description + "\n".join(instructions)

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Replace Skill.ANY_OF_YOUR_CHOICE placeholders using AI.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Blueprint with skill placeholders replaced by AI selections.
        """
        # Check if there are any placeholders
        if Skill.ANY_OF_YOUR_CHOICE not in blueprint.skill_proficiencies:
            return Blueprint()

        # Build prompt and get AI selection
        prompt = self._build_prompt(blueprint)
        if not prompt:
            return Blueprint()

        structured_llm = self.llm.with_structured_output(
            SkillProficiencySelection
        )
        selection = structured_llm.invoke(prompt)

        # Validate selection count
        count = list(blueprint.skill_proficiencies).count(
            Skill.ANY_OF_YOUR_CHOICE
        )
        if len(selection.skill_proficiencies) != count:
            raise ValueError(
                f"AI returned {len(selection.skill_proficiencies)} skills "
                f"but expected {count}"
            )

        # Replace placeholders
        new_skills = set(blueprint.skill_proficiencies)
        new_skills.discard(Skill.ANY_OF_YOUR_CHOICE)
        new_skills.update(selection.skill_proficiencies)

        return Blueprint(skill_proficiencies=new_skills)
