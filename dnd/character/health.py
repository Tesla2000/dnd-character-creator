from __future__ import annotations

from abc import abstractmethod

from dnd.character.base import Modifier


class HealthModifier[C](Modifier[C]):
    """Anything that adds to max hit points. Every source of max HP subclasses this."""

    @abstractmethod
    def apply(self, character: C) -> int: ...
