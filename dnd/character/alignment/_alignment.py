from __future__ import annotations

from dnd.character.base import Modifier
from dnd.choices.alignment import Alignment


class AlignmentModifier(Modifier[object]):
    alignment: Alignment

    def apply(self, character: object) -> Alignment:
        return self.alignment
