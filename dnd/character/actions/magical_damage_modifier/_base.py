from __future__ import annotations

from abc import ABC
from enum import IntEnum
from typing import TYPE_CHECKING, ClassVar, Self

from pydantic import BaseModel, ConfigDict

from dnd.character.actions._damage_type import DamageType

if TYPE_CHECKING:
    from dnd.fight._combat_event import AnyCombatEvent

_MAGICAL_UPGRADE: dict[DamageType, DamageType] = {
    DamageType.BLUDGEONING: DamageType.MAGICAL_BLUDGEONING,
    DamageType.PIERCING: DamageType.MAGICAL_PIERCING,
    DamageType.SLASHING: DamageType.MAGICAL_SLASHING,
}


class _MagicalDamageModifier(BaseModel, ABC):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    def upgrade(self, damage_type: DamageType) -> DamageType:
        return _MAGICAL_UPGRADE.get(damage_type, damage_type)

    def on_event[T: IntEnum](
        self, event: AnyCombatEvent[T]
    ) -> tuple[Self | None, tuple[AnyCombatEvent[T], ...]]:
        return self, ()
