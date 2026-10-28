from typing import Annotated
from typing import Union

from pydantic import Field

from dnd.character.spell_attack_bonus._base import (
    _SpellAttackBonusModifier as SpellAttackBonusModifier,
)
from dnd.character.spell_attack_bonus._flat_bonus import FlatSpellAttackBonus
from dnd.character.spell_attack_bonus._proficiency import ProficiencyBonus
from dnd.character.spell_attack_bonus._spellcasting_ability import (
    SpellcastingAbility,
)
from dnd.character.spell_attack_bonus._type import SpellAttackBonusModifierType

AnySpellAttackBonusModifier = Annotated[
    Union[ProficiencyBonus, SpellcastingAbility, FlatSpellAttackBonus],
    Field(discriminator="type"),
]

__all__ = [
    "AnySpellAttackBonusModifier",
    "FlatSpellAttackBonus",
    "ProficiencyBonus",
    "SpellAttackBonusModifier",
    "SpellAttackBonusModifierType",
    "SpellcastingAbility",
]
