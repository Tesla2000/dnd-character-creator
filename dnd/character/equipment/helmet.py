from __future__ import annotations

from abc import ABC
from collections.abc import Generator
from dnd.character.modifiers.base import _Modifier
from dnd.character.modifiers.source import ModifierSource
from dnd.character.modifiers.source import _ModifierSource


class HelmetModifier(ModifierSource, ABC):
    """Base for helmets. Every helmet is a source, so plate armor cannot go on the head."""


class NoHelmet(HelmetModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()
