from __future__ import annotations

from dnd.getters.getter import Getter
from dnd.character.modifiers.darkvision import DarkvisionModifier
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd.character.character import Character


class DarkvisionGetter(Getter):
    def get(self, character: Character) -> int:
        return max(
            (
                modifier.apply(character)
                for modifier in character.modifiers
                if isinstance(modifier, DarkvisionModifier)
            ),
            default=0,
        )
