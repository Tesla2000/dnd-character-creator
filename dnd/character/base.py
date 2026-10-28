from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Generator
from enum import IntEnum
from typing import ClassVar
from typing import Never
from typing import NamedTuple

from pydantic import BaseModel
from pydantic import ConfigDict


class Priority(IntEnum):
    """Order in which a source's modifiers are applied. Lower values apply first."""

    BASE_STATS = 0
    SUBRACE = 1
    BACKGROUND = 2
    # Equipment, class, and magical items share this level. Their order does not matter,
    # so they keep the order they were added in.
    UNORDERED = 3


class _Modifier[C](ABC):
    """A leaf effect that computes its contribution from the character it is given."""

    @abstractmethod
    def apply(self, character: C) -> object: ...


class Modifier[C](_Modifier[C], BaseModel):
    model_config = ConfigDict(frozen=True)


class _ModifierSource(ABC):
    """Anything that produces modifiers, either leaf modifiers or further sources."""

    priority: ClassVar[Priority]

    @abstractmethod
    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]: ...


class ModifierSource(_ModifierSource, BaseModel, ABC):
    model_config = ConfigDict(frozen=True)


class PrioritizedNode(NamedTuple):
    """A modifier or source with the priority of the source it came from.

    Ordering compares priority only, so sorting keeps the order of equal priorities.
    """

    priority: Priority
    node: _Modifier[Never] | _ModifierSource

    def __lt__(self, other: tuple[object, ...]) -> bool:
        if not isinstance(other, PrioritizedNode):
            return NotImplemented
        return self.priority < other.priority
