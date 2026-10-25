from __future__ import annotations

from abc import ABC
from collections.abc import Generator
from dnd.character.classes.enums import Class
from dnd.character.level import Level
from dnd.character.modifiers.base import _Modifier
from dnd.character.modifiers.health import MaxHealthModifier
from dnd.character.modifiers.source import ModifierSource
from dnd.character.modifiers.source import _ModifierSource
from enum import IntEnum
from typing import ClassVar


class Die(IntEnum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20


class ClassLevelBase(ModifierSource, ABC):
    """Base for one class: its class and hit die. Each level is a subclass of this."""

    class_: ClassVar[Class]
    hit_die: ClassVar[Die]
    number: ClassVar[Level]

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield MaxHealthModifier(bonus=self.hit_die // 2 + 1)
