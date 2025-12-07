from __future__ import annotations

from typing import Generator

from pydantic import Field

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler.ai_builder_base import \
    AIBuilderBase


class AIBaseBuilderAssigner(AIBuilderBase):
    """Uses AI to assign all basic character parameters based on a description.

    This building block leverages LLM structured output to generate coherent
    character parameters (name, sex, age, race, background, alignment, level)
    from a natural language description. Always generates all fields regardless
    of what's already set.

    Example:
        >>> assigner = AIBaseBuilderAssigner(
        ...     description="A wise elderly elven wizard who studies ancient magic",
        ...     model_name="gpt-4o",
        ...     temperature=0.7
        ... )
        >>> builder = Builder([assigner])
        >>> character = builder.build()
    """

    model_name: str = Field(
        default="gpt-4o",
        description="OpenAI model name to use for generation",
    )

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Generate character parameters using AI and yield the difference.

        Args:
            blueprint: The current blueprint state.

        Yields:
            Blueprint with AI-generated character parameters.
        """
        prompt = (
            f"Create a D&D 5e character based on this description: {self.description}\n"
            f"Here are current values: {blueprint.model_dump_json(exclude_unset=True)}"
        )
        result = self._generate_character_template(prompt)

        yield Blueprint(
            name=result.name,
            sex=result.sex,
            age=result.age,
            race=result.race,
            background=result.background,
            alignment=result.alignment,
            level=result.level,
        )
