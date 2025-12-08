from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field
from pydantic import PositiveInt

from dnd_character_creator.character.race.race import Race
from dnd_character_creator.choices.alignment import Alignment
from dnd_character_creator.choices.background_creatrion.background import (
    Background,
)
from dnd_character_creator.choices.sex import Sex


class CharacterBaseTemplate(BaseModel):
    """Template for AI-generated basic character parameters.

    This model defines the structure for generating core character attributes
    using LLM structured output. All fields have descriptions to guide the AI
    in making appropriate choices.
    """

    name: str = Field(
        description="Character's full name, appropriate for their race and background."
    )

    sex: Sex = Field(description="Character's biological sex.")

    age: PositiveInt = Field(
        description="Character's age in years, appropriate for their race. "
        "Consider racial lifespans: elves live centuries, humans decades."
    )

    race: Race = Field(
        description="Character's race. Choose based on character concept and setting."
    )

    background: Background = Field(
        description="Character's background representing their life before adventuring. "
        "Should align with character concept and backstory."
    )

    alignment: Alignment = Field(
        description="Character's moral and ethical outlook. Should fit personality and backstory."
    )

    level: int = Field(
        ge=1,
        le=20,
        description="Character's experience level from 1 (novice) to 20 (legendary).",
    )
