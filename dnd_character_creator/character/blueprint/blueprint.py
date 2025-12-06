from __future__ import annotations

from typing import Optional

from pydantic import Field, PositiveInt

from dnd_character_creator.character.character import Character
from dnd_character_creator.choices.alignment import Alignment
from dnd_character_creator.choices.background_creatrion.background import Background
from dnd_character_creator.choices.race_creation.main_race import Race
from dnd_character_creator.choices.sex import Sex


class Blueprint(Character):
    """Blueprint for building a Character with optional fields.

    All required fields from Character are optional in Blueprint, allowing
    incremental character construction through building blocks.
    """

    # Override required fields to be optional
    sex: Optional[Sex] = None
    backstory: Optional[str] = None
    level: Optional[int] = Field(None, ge=1, le=20)
    age: Optional[PositiveInt] = None
    race: Optional[Race] = None
    name: Optional[str] = None
    background: Optional[Background] = None
    alignment: Optional[Alignment] = None
    height: Optional[PositiveInt] = None
    weight: Optional[PositiveInt] = None
    eye_color: Optional[str] = None
    skin_color: Optional[str] = None
    hairstyle: Optional[str] = None
    appearance: Optional[str] = None
    character_traits: Optional[str] = None
    ideals: Optional[str] = None
    bonds: Optional[str] = None
    weaknesses: Optional[str] = None
