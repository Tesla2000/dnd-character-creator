from __future__ import annotations

from dnd.character.base import Modifier


class AcModifier(Modifier[object]):
    bonus: int

    def apply(self, character: object) -> int:
        return self.bonus
