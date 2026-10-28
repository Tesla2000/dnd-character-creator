from __future__ import annotations

from typing import Protocol

from dnd.character.health import HealthModifier


class ToughCharacter(Protocol):
    @property
    def level(self) -> int: ...


class ToughModifier(HealthModifier[ToughCharacter]):
    def apply(self, character: ToughCharacter) -> int:
        return 2 * character.level
