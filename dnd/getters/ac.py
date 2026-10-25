from __future__ import annotations

from dnd.getters.getter import Getter
from dnd.character.modifiers.ac import AcModifier
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd.character.character import Character


class AcGetter(Getter):
    base: int = 10

    def get(self, character: Character) -> int:
        return self.base + sum(
            modifier.apply(character)
            for modifier in character.modifiers
            if isinstance(modifier, AcModifier)
        )
