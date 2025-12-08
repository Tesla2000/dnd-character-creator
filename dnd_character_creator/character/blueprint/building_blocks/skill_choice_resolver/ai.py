"""AI-powered skill choice resolver for intelligent skill selection."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.blueprint_formatter import (
    BlueprintFormatter,
)
from dnd_character_creator.character.blueprint.building_blocks.skill_choice_resolver.base import (
    SkillChoiceResolver,
)
from dnd_character_creator.skill_proficiency import Skill
from frozendict import frozendict
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from pydantic import Field


class SkillSelection(BaseModel):
    """Schema for AI to select skills."""

    selected_skills: tuple[Skill, ...] = Field(
        description="Selected skill proficiencies"
    )


class AISkillChoiceResolver(SkillChoiceResolver):
    """AI-powered skill choice resolver that selects skills based on character context.

    Uses an LLM to make intelligent skill selections based on the character's
    class, background, stats, and overall concept. The AI considers which skills
    best fit the character's role and abilities.

    Example:
        >>> resolver = AISkillChoiceResolver(
        ...     model_name="gpt-4o-mini",
        ...     temperature=0.3
        ... )
        >>> builder = Builder().add(resolver)
    """

    model_name: str = Field(
        description="OpenAI model name to use for skill selection"
    )

    temperature: float = Field(
        default=0.3,
        description="Temperature for AI selection (lower = more deterministic)",
    )

    ai_model_kwargs: Mapping[str, Any] = Field(
        default_factory=frozendict,
        description="Additional kwargs to pass to ChatOpenAI",
    )

    formatter: BlueprintFormatter = Field(
        default_factory=BlueprintFormatter,
        description="Blueprint formatter for creating AI prompts",
    )

    def _create_llm(self) -> ChatOpenAI:
        """Create a ChatOpenAI instance with configured parameters.

        Returns:
            Configured ChatOpenAI instance.
        """
        return ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            **self.ai_model_kwargs,
        )

    def _build_prompt(self, blueprint: Blueprint) -> str:
        """Build a prompt for AI skill selection.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Formatted prompt string.
        """
        n = blueprint.n_skill_choices
        available_skills = blueprint.skills_to_choose_from

        parts = [
            f"You are selecting {n} skill proficiencies for a D&D 5e character.",
            "Choose skills that best fit the character's class, background, "
            "ability scores, and overall concept.",
        ]

        # Use formatter to add character details
        character_description = self.formatter.format(blueprint)
        if character_description:
            parts.append(character_description)

        # Add available skills
        parts.append("\n## Available Skills")
        parts.append(
            f"Select exactly {n} skills from the following options:\n"
        )

        # Filter out ANY_OF_YOUR_CHOICE placeholder
        actual_skills = [
            skill
            for skill in available_skills
            if skill != Skill.ANY_OF_YOUR_CHOICE
        ]

        for skill in sorted(actual_skills, key=lambda s: s.value):
            parts.append(f"  - {skill.value}")

        # Add selection instructions
        parts.append("\n## Selection Instructions")
        parts.append(
            f"Return exactly {n} skills from the available options above."
        )
        parts.append(
            "Consider:"
            "\n  - Which skills complement the character's primary ability scores"
            "\n  - Which skills fit the character's class and background"
            "\n  - Which skills support the character's role in a party"
            "\n  - The character's backstory and personality"
        )

        return "\n".join(parts)

    def _select_skills(self, blueprint: Blueprint) -> frozenset[Skill]:
        """Use AI to select skills from available options.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Frozenset of AI-selected skills.
        """
        # Build prompt and get AI selection
        prompt = self._build_prompt(blueprint)

        llm = self._create_llm()
        structured_llm = llm.with_structured_output(SkillSelection)
        selection = structured_llm.invoke(prompt)

        # Validate selection
        if len(selection.selected_skills) != blueprint.n_skill_choices:
            raise ValueError(
                f"AI returned {len(selection.selected_skills)} skills "
                f"but expected {blueprint.n_skill_choices}"
            )

        # Filter out ANY_OF_YOUR_CHOICE if present
        actual_available = frozenset(
            skill
            for skill in blueprint.skills_to_choose_from
            if skill != Skill.ANY_OF_YOUR_CHOICE
        )

        # Validate all selected skills are available
        for skill in selection.selected_skills:
            if skill not in actual_available:
                raise ValueError(
                    f"AI selected {skill.value} which is not in available skills"
                )

        return frozenset(selection.selected_skills)
