from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Generator
from dnd.character.modifiers.base import _Modifier
from pydantic import BaseModel
from pydantic import ConfigDict


class _ModifierSource(ABC):
    """Anything that produces modifiers, either leaf modifiers or further sources."""

    @abstractmethod
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]: ...


class ModifierSource(_ModifierSource, BaseModel, ABC):
    model_config = ConfigDict(frozen=True)
