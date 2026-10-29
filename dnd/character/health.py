from __future__ import annotations

from abc import abstractmethod

from dnd.character.base import ModifiedCharacter
from dnd.character.base import Modifier


class HealthModifier(Modifier):
    """Anything that adds to max hit points. Every source of max HP subclasses this."""

    @abstractmethod
    def apply(self, character: ModifiedCharacter) -> int: ...
