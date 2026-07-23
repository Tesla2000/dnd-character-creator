from abc import ABC
from abc import abstractmethod
from typing import Protocol

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import NonNegativeInt


class _HealthModifierContext(Protocol):
    @property
    def level(self) -> int: ...

    @property
    def constitution_modifier(self) -> int: ...


class _HealthModifier(BaseModel, ABC):
    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def apply(self, context: _HealthModifierContext) -> NonNegativeInt: ...
