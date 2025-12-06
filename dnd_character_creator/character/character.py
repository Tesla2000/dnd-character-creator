from __future__ import annotations

from typing import Annotated, Mapping, Any
from typing import Optional

from frozendict import frozendict
from pydantic import AfterValidator, BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PositiveInt

from dnd_character_creator.character.spells import Spells
from dnd_character_creator.choices.alignment import Alignment
from dnd_character_creator.choices.background_creatrion.background import (
    Background,
)
from dnd_character_creator.choices.class_creation.character_class import (
    Class,
)
from dnd_character_creator.choices.equipment_creation.armor import ArmorName
from dnd_character_creator.choices.equipment_creation.weapons import WeaponName
from dnd_character_creator.choices.invocations.eldritch_invocation import (
    WarlockPact,
)
from dnd_character_creator.choices.race_creation.main_race import Race
from dnd_character_creator.choices.sex import Sex
from dnd_character_creator.choices.stats_creation.statistic import Statistic
from dnd_character_creator.feats import Feat


def _conv_to_frozendict(value: Any) -> Any:
    if not isinstance(value, Mapping):
        return value
    return frozendict(value)


class Character(BaseModel):
    model_config = ConfigDict(frozen=True)

    sex: Sex
    backstory: str
    level: int = Field(ge=1, le=20)
    age: PositiveInt
    classes: Annotated[Mapping[Class, PositiveInt], AfterValidator(_conv_to_frozendict)] = frozendict()
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
    feats: tuple[Feat, ...] = Field(
        description="Feats from a list fitting description of the character if"
        " race is variant human at least one must be different "
        "than ability score improvement",
        default=(),
    )
    sub_race: Optional[str] = None
    sub_class: Optional[str] = None
    warlock_pact: Optional[WarlockPact] = None
    armor: Optional[ArmorName] = Field(
        None,
        description="You would typically have clothes for spell casters. You "
        "have a total of 'amount_of_gold_for_equipment' to spend "
        "for both armor and weapons. Barbarians and Monks usually "
        "don't use armor either.",
    )
    weapons: tuple[WeaponName, ...] = Field(
        description="You would typically leave it empty for spell casters. "
        "You have a total of 'amount_of_gold_for_equipment' to "
        "spend for both armor and weapons.",
        default=(),
    )
    other_equipment: tuple[str, ...] = Field(
        default=(),
        description="All alchemical supplies, medicines, potions etc.",
    )
    spells: Spells = Field(default_factory=Spells)
