"""AI-powered expertise choice resolver for intelligent expertise selection."""

from dnd.character.blueprint.building_blocks.expertise_choice_resolver.base import (
    ExpertiseChoiceResolver,
)
from dnd.character.blueprint.building_blocks.building_block import _WideBlueprint
from dnd.skill_proficiency import Skill
from typing import Literal
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from pydantic import BaseModel
from pydantic import Field
from structured_output_creator import OpenAIService, RaisingService


class AIExpertiseChoiceResolver(ExpertiseChoiceResolver):
    """AI-powered expertise choice resolver that selects skills based on character context."""

    type: Literal[BuildingBlockType.AI_EXPERTISE_CHOICE_RESOLVER] = (
        BuildingBlockType.AI_EXPERTISE_CHOICE_RESOLVER
    )

    llm: RaisingService[BaseModel] = Field(
        exclude=True,
        default_factory=lambda: RaisingService(service=OpenAIService()),
        description="Language model for making AI-powered decisions",
    )

    def _build_prompt(self, state: _WideBlueprint) -> str:
        n = state.n_expertise_choices
        available_skills = state.expertise_choices_from

        parts = [
            f"You are selecting {n} skills to grant expertise (doubled proficiency "
            "bonus) on for a D&D 5e character.",
            "Choose skills that best fit the character's class, background, "
            "ability scores, and overall concept.",
        ]

        parts.append("\n## Available Skills")
        parts.append(f"Select exactly {n} skills from the following options:\n")

        for skill in sorted(available_skills, key=lambda s: s.value):
            parts.append(f"  - {skill.value}")

        parts.append("\n## Selection Instructions")
        parts.append(f"Return exactly {n} skills from the available options above.")
        parts.append(
            "Consider:"
            "\n  - Which skills the character will roll most often"
            "\n  - Which skills complement the character's primary ability scores"
            "\n  - Which skills fit the character's class and background"
            "\n  - The character's backstory and personality"
        )

        return "\n".join(parts)

    def _select_expertise(self, state: _WideBlueprint) -> frozenset[Skill]:
        prompt = self._build_prompt(state)
        n = state.n_expertise_choices

        class ExpertiseSelection(BaseModel):
            selected_skills: list[Skill] = Field(min_length=n, max_length=n)

        selection = self.llm.create_structured_output(prompt, ExpertiseSelection)

        actual_available = frozenset(state.expertise_choices_from)

        for skill in selection.selected_skills:
            if skill not in actual_available:
                raise ValueError(
                    f"AI selected {skill.value} which is not in available skills"
                )

        return frozenset(selection.selected_skills)
