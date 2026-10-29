from __future__ import annotations

from pydantic import NonNegativeInt

from dnd.character.base import Modifier


class DarkvisionModifier(Modifier):
    range_feet: NonNegativeInt

    def apply(self, character: object) -> int:
        return self.range_feet
