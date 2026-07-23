from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING, Literal

from dnd.character.actions.advantage_modifier._base import (
    _AdvantageModifier,
    _GrantsAdvantageModifier,
)
from dnd.character.actions.advantage_modifier._type import AdvantageModifierType

if TYPE_CHECKING:
    from dnd.fight.fight_character import FightCharacter


class _RecklessAdvantageModifier(_AdvantageModifier):
    type: Literal[AdvantageModifierType.RECKLESS] = AdvantageModifierType.RECKLESS

    def apply[SlotT: IntEnum](
        self,
        attacker: FightCharacter[SlotT],
        _defender: FightCharacter[SlotT],
    ) -> bool:
        return True


class _RecklessGrantsAdvantageModifier(_GrantsAdvantageModifier):
    type: Literal[AdvantageModifierType.RECKLESS_GRANTS] = (
        AdvantageModifierType.RECKLESS_GRANTS
    )

    def apply[SlotT: IntEnum](
        self,
        attacker: FightCharacter[SlotT],
        _defender: FightCharacter[SlotT],
    ) -> bool:
        return True
