from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from pydantic import BaseModel
from pydantic import ConfigDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd.character.character import Character


class Getter(BaseModel, ABC):
    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def get(self, character: Character) -> object: ...
