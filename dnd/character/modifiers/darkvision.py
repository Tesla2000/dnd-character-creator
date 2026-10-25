from __future__ import annotations

from dnd.character.modifiers.base import Modifier
from pydantic import NonNegativeInt
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd.character.character import Character


class DarkvisionModifier(Modifier):
    range_feet: NonNegativeInt

    def apply(self, character: Character) -> int:
        return self.range_feet
