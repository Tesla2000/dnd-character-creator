from __future__ import annotations
from typing import ClassVar

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.base import Modifier
from dnd.character.base import ModifierSource
from dnd.character.base import Priority
from dnd.choices.background_creatrion.background import Background


class BackgroundModifier(Modifier):
    background: Background

    def apply(self, character: object) -> Background:
        return self.background


class CharacterBackground(ModifierSource):
    priority: ClassVar[Priority] = Priority.BACKGROUND

    background: Background

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield BackgroundModifier(background=self.background)
