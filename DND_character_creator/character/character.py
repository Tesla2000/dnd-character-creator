from __future__ import annotations

from collections import defaultdict
from typing import Optional, Annotated

from pydantic import BaseModel
from pydantic import Field
from pydantic import PositiveInt

from DND_character_creator.character.spells import Spells
from DND_character_creator.choices.alignment import Alignment
from DND_character_creator.choices.background_creatrion.background import (
    Background,
)
from DND_character_creator.choices.class_creation.character_class import (
    Class,
)
from DND_character_creator.choices.equipment_creation.armor import ArmorName
from DND_character_creator.choices.equipment_creation.weapons import WeaponName
from DND_character_creator.choices.invocations.eldritch_invocation import \
    WarlockPact
from DND_character_creator.choices.race_creation.main_race import Race
from DND_character_creator.choices.sex import Sex
from DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from DND_character_creator.feats import Feat


class Character(BaseModel):
    sex: Sex
    backstory: str
    level: int = Field(ge=1, le=20)
    age: PositiveInt
    classes: dict[Class, PositiveInt] = Field(default_factory=lambda: defaultdict(int))
    race: Race
    name: str
    background: Background
    alignment: Alignment
    height: PositiveInt
    weight: PositiveInt
    eye_color: str
    skin_color: str
    hairstyle: str
    appearance: str
    character_traits: str
    ideals: str
    bonds: str
    weaknesses: str
    base_description: Optional[str] = None
    feats: list[Feat] = Field(
        description="Feats from a list fitting description of the character if"
        " race is variant human at least one must be different "
        "than ability score improvement",
        default_factory=list,
    )
    sub_race: Optional[str] = None
    sub_class: Optional[str] = None
    warlock_pact: Optional[WarlockPact] = None
    armor: Optional[ArmorName] = Field(
        None,
        description="You would typically have clothes for spell casters. You "
        "have a total of 'amount_of_gold_for_equipment' to spend "
        "for both armor and weapons. Barbarians and Monks usually "
        "don't use armor either."
    )
    weapons: list[WeaponName] = Field(
        description="You would typically leave it empty for spell casters. "
        "You have a total of 'amount_of_gold_for_equipment' to "
        "spend for both armor and weapons.",
        default_factory=list,
    )
    other_equipment: list[str] = Field(
        default_factory=list,
        description="All alchemical supplies, medicines, potions etc.",
    )
    spells: Spells = Field(default_factory=Spells)
