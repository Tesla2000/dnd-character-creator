from __future__ import annotations

from abc import ABC, abstractmethod
from enum import IntEnum
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict
from typing import Self

if TYPE_CHECKING:
    from dnd.fight._combat_event import AnyCombatEvent
    from dnd.fight.fight_character import FightCharacter


class _AttackBonusModifier(BaseModel, ABC):
    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def apply(
        self,
        attacker: FightCharacter,
        _defender: FightCharacter,
    ) -> int: ...

    def on_event[T: IntEnum](
        self, event: AnyCombatEvent[T]
    ) -> tuple[Self | None, tuple[AnyCombatEvent[T], ...]]:
        return self, ()
