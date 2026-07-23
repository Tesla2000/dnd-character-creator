from dnd.character.actions.magical_damage_modifier._base import (
    _MagicalDamageModifier as MagicalDamageModifier,
)
from dnd.character.actions.magical_damage_modifier._primal_strike import (
    _PrimalStrikeMagicalDamageModifier as PrimalStrikeMagicalDamageModifier,
)
from dnd.character.actions.magical_damage_modifier._type import (
    MagicalDamageModifierType,
)

AnyMagicalDamageModifier = PrimalStrikeMagicalDamageModifier

__all__ = [
    "AnyMagicalDamageModifier",
    "MagicalDamageModifier",
    "MagicalDamageModifierType",
    "PrimalStrikeMagicalDamageModifier",
]
