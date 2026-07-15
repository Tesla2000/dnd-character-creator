from abc import ABC
from abc import abstractmethod
from typing import Protocol

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import PositiveInt


class _HealthModifierContext(Protocol):
    @property
    def level(self) -> int: ...


class _HealthModifier(BaseModel, ABC):
    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def apply(self, context: _HealthModifierContext) -> PositiveInt: ...
