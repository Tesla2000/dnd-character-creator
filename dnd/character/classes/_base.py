from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Generator
from enum import IntEnum
from typing import ClassVar

from dnd.character.base import Modifier
from dnd.character.base import ModifierSource
from dnd.character.base import Priority
from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.classes._enums import Class


class Die(IntEnum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20


class HitDieModifier(Modifier):
    """The hit die of one class level. Turning dice into hit points is the health getter's job."""

    die: Die

    def apply(self, character: object) -> int:
        return self.die


class ClassLevelBase(ModifierSource, ABC):
    """Base for one class: its class and hit die. Each level is a subclass of this."""

    priority: ClassVar[Priority] = Priority.UNORDERED
    class_: ClassVar[Class]
    hit_die: ClassVar[Die]

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield HitDieModifier(die=self.hit_die)
        yield from self._get_level_modifiers()

    @abstractmethod
    def _get_level_modifiers(self) -> Generator[_Modifier | _ModifierSource]: ...
