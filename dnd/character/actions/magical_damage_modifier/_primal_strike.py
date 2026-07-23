from __future__ import annotations

from typing import Literal

from dnd.character.actions.magical_damage_modifier._base import _MagicalDamageModifier
from dnd.character.actions.magical_damage_modifier._type import (
    MagicalDamageModifierType,
)


class _PrimalStrikeMagicalDamageModifier(_MagicalDamageModifier):
    type: Literal[MagicalDamageModifierType.PRIMAL_STRIKE] = (
        MagicalDamageModifierType.PRIMAL_STRIKE
    )
