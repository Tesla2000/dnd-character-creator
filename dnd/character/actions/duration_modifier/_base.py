from abc import ABC
from enum import IntEnum
from typing import ClassVar, Self

from pydantic import BaseModel, ConfigDict
from uuid_string import UUIDString

from dnd._combat_event import AnyCombatEvent


class _DurationModifier(BaseModel, ABC):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    owner_id: UUIDString

    def on_event[T: IntEnum](
        self, event: AnyCombatEvent[T]
    ) -> tuple[Self | None, tuple[AnyCombatEvent[T], ...]]:
        return self, ()
