from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING, Literal

from typing import Self
from uuid_string import UUIDString

from dnd.character._ability_name import AbilityName
from dnd.character.actions.attack_bonus_modifier._base import _AttackBonusModifier
from dnd.character.actions.attack_bonus_modifier._type import AttackBonusModifierType
from dnd._combat_event import AnyCombatEvent, RageEndsEvent

if TYPE_CHECKING:
    from dnd.fight.fight_character import FightCharacter


class _RageAttackBonusModifier(_AttackBonusModifier):
    type: Literal[AttackBonusModifierType.RAGE] = AttackBonusModifierType.RAGE
    owner_id: UUIDString

    def apply[SlotT: IntEnum](
        self,
        attacker: FightCharacter[SlotT],
        _defender: FightCharacter[SlotT],
    ) -> int:
        return 2 if AbilityName.RAGE in attacker.active_features else 0

    def on_event[T: IntEnum](
        self, event: AnyCombatEvent[T]
    ) -> tuple[Self | None, tuple[AnyCombatEvent[T], ...]]:
        match event:
            case RageEndsEvent() if event.target_id == self.owner_id:
                return None, ()
            case _:
                return self, ()
