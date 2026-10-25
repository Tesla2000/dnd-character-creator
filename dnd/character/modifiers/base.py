from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from pydantic import BaseModel
from pydantic import ConfigDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd.character.character import Character


class _Modifier(ABC):
    """A leaf effect that computes its contribution from the character."""

    @abstractmethod
    def apply(self, character: Character) -> object: ...


class Modifier(_Modifier, BaseModel):
    model_config = ConfigDict(frozen=True)
