from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler.base_filler import (
    InitialDataFiller,
)
from pydantic import Field


class AIPartialBuilderAssigner(InitialDataFiller):
    """Uses AI to fill only unset basic character parameters.

    This building block leverages LLM structured output to generate values
    only for fields that are currently unset in the blueprint. Already set
    fields are preserved and passed to the AI as context.

    Example:
        >>> from langchain_openai import ChatOpenAI
        >>> builder = Builder([
        ...     RaceAssigner(race=Race.ELF),  # Set race first
        ...     AIPartialBuilderAssigner(
        ...         description="A wise wizard",
        ...         model_name="gpt-4o",
        ...         temperature=0.7
        ...     ),  # AI fills other fields, respects race=ELF
        ... ])
        >>> character = builder.build()
    """

    model_name: str = Field(
        default="gpt-4o-mini",
        description="OpenAI model name to use for generation",
    )

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Generate only unset character parameters using AI.

        Args:
            blueprint: The current blueprint state.

        Yields:
            Blueprint with AI-generated values for unset fields only.
        """
        # Get currently set fields
        set_fields = blueprint.model_dump(exclude_unset=True)

        prompt = (
            f"Create a D&D 5e character based on this description: {self.description}\n"
            f"The following fields are already set and must be respected: {set_fields}\n"
            f"Only generate values for unset fields."
        )
        result = self._generate_character_template(prompt)

        # Only yield fields that aren't already set
        updates = {}
        if "name" not in set_fields:
            updates["name"] = result.name
        if "sex" not in set_fields:
            updates["sex"] = result.sex
        if "age" not in set_fields:
            updates["age"] = result.age
        if "race" not in set_fields:
            updates["race"] = result.race
        if "background" not in set_fields:
            updates["background"] = result.background
        if "alignment" not in set_fields:
            updates["alignment"] = result.alignment
        if "level" not in set_fields:
            updates["level"] = result.level

        return Blueprint(**updates)
