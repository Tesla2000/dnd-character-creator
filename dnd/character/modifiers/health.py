from __future__ import annotations

from dnd.character.modifiers.base import Modifier
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd.character.character import Character


class MaxHealthModifier(Modifier):
    bonus: int

    def apply(self, character: Character) -> int:
        return self.bonus


class DwarvenToughnessModifier(Modifier):
    def apply(self, character: Character) -> int:
        return character.level
