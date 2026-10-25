from __future__ import annotations

from abc import ABC
from collections.abc import Generator
from dnd.character.modifiers.base import _Modifier
from dnd.character.modifiers.source import ModifierSource
from dnd.character.modifiers.source import _ModifierSource


class CloakModifier(ModifierSource, ABC):
    """Base for cloaks. Every cloak is a source, so plate armor cannot be a cape."""


class NoCloak(CloakModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()
