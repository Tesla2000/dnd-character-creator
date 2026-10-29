from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Sequence
from typing import Protocol

from pydantic import BaseModel
from pydantic import ConfigDict

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource


class PrioritizedCharacter(Protocol):
    @property
    def modifiers(self) -> tuple[_Modifier | _ModifierSource, ...]: ...


class Getter[C: PrioritizedCharacter, R](BaseModel, ABC):
    """Calls _get with the character's modifiers, already ordered by priority."""

    model_config = ConfigDict(frozen=True)

    def get(self, character: C) -> R:
        return self._get(character, character.modifiers)

    @abstractmethod
    def _get(
        self,
        character: C,
        modifiers: Sequence[_Modifier | _ModifierSource],
    ) -> R: ...
