from __future__ import annotations

from dnd.character.base import Modifier
from dnd.choices.sex import Sex


class SexModifier(Modifier[object]):
    sex: Sex

    def apply(self, character: object) -> Sex:
        return self.sex
