from __future__ import annotations

from typing import Optional

from pydantic import Field, PositiveInt, NonNegativeInt

from dnd_character_creator.character.character import Character
from dnd_character_creator.character.stats import Stats
from dnd_character_creator.character.race.subraces import Subrace
from dnd_character_creator.choices.alignment import Alignment
from dnd_character_creator.choices.background_creatrion.background import Background
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.choices.language import Language
from dnd_character_creator.choices.sex import Sex
from dnd_character_creator.feats import Feat
from dnd_character_creator.other_profficiencies import (
    GamingSet,
    MusicalInstrument,
    ToolProficiency,
)
from dnd_character_creator.skill_proficiency import Skill


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
    subrace: Optional[Subrace] = None
    name: Optional[str] = None
    background: Optional[Background] = None
    alignment: Optional[Alignment] = None
    stats: Optional[Stats] = None
    health: Optional[PositiveInt] = None
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
    dark_vision_range: Optional[NonNegativeInt] = None
    speed: Optional[PositiveInt] = None
    n_stat_choices: NonNegativeInt = 0
    n_skill_choices: NonNegativeInt = 0
    skills_to_choose_from: frozenset[Skill] = Field(
        default_factory=frozenset,
        description="Skills from which n_skill_choices can be chosen"
    )
    languages: tuple[Language, ...] = Field(default=())
    skill_proficiencies: tuple[Skill, ...] = Field(
        default=(), description="Skills the character is proficient in"
    )
    feats: tuple[Feat, ...] = Field(
        description="Feats from a list fitting description of the character if"
        " race is variant human at least one must be different "
        "than ability score improvement",
        default=(),
    )
    tool_proficiencies: tuple[ToolProficiency | GamingSet | MusicalInstrument, ...] = Field(
        default=(), description="Tool proficiencies"
    )

