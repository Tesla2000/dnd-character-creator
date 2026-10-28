from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Sequence
from typing import Never
from typing import Protocol

from pydantic import BaseModel
from pydantic import ConfigDict

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.base import PrioritizedNode


class PrioritizedCharacter(Protocol):
    @property
    def prioritized_modifiers(self) -> tuple[PrioritizedNode, ...]: ...


class Getter[C: PrioritizedCharacter, R](BaseModel, ABC):
    """Sorts the character's modifiers by priority, then calls _get with them in order."""

    model_config = ConfigDict(frozen=True)

    def get(self, character: C) -> R:
        ordered = [found.node for found in sorted(character.prioritized_modifiers)]
        return self._get(character, ordered)

    @abstractmethod
    def _get(
        self,
        character: C,
        modifiers: Sequence[_Modifier[Never] | _ModifierSource],
    ) -> R: ...
