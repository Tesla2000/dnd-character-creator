from typing import Annotated
from typing import Union

from pydantic import Field

from dnd.character.ac_modifier._barbarian_unarmored_defense import (
    _BarbarianUnarmoredDefenseAcModifier as BarbarianUnarmoredDefenseAcModifier,
)
from dnd.character.ac_modifier._base import _AcModifier as AcModifier
from dnd.character.ac_modifier._base import _AcModifierContext as AcModifierContext
from dnd.character.ac_modifier._base import _AdditiveAcModifier as AdditiveAcModifier
from dnd.character.ac_modifier._base import _CompetingAcModifier as CompetingAcModifier
from dnd.character.ac_modifier._flat import _FlatAcModifier as FlatAcModifier
from dnd.character.ac_modifier._type import AcModifierType
from dnd.character.armor.armor import Armor

AnyAcModifier = Annotated[
    Union[Armor, BarbarianUnarmoredDefenseAcModifier, FlatAcModifier],
    Field(discriminator="type"),
]

__all__ = [
    "AcModifier",
    "AcModifierContext",
    "AcModifierType",
    "AdditiveAcModifier",
    "AnyAcModifier",
    "BarbarianUnarmoredDefenseAcModifier",
    "CompetingAcModifier",
    "FlatAcModifier",
]
