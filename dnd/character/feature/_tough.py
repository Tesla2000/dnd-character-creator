from __future__ import annotations

from typing import Protocol
from typing import runtime_checkable

from pydantic import ConfigDict
from pydantic import InstanceOf

from dnd.character.base import ModifiedCharacter
from dnd.character.health import HealthModifier


@runtime_checkable
class LevelOf[C](Protocol):
    def get(self, character: C) -> int: ...


class ToughModifier(HealthModifier):
    model_config = ConfigDict(frozen=True)

    level_getter: InstanceOf[LevelOf[ModifiedCharacter]]

    def apply(self, character: ModifiedCharacter) -> int:
        return 2 * self.level_getter.get(character)
