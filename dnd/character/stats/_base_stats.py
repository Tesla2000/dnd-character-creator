from __future__ import annotations
from typing import ClassVar

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.base import Modifier
from dnd.character.base import ModifierSource
from dnd.character.base import Priority
from dnd.character.stats._stats import Stats


class BaseStatsModifier(Modifier):
    stats: Stats

    def apply(self, character: object) -> Stats:
        return self.stats


class BaseStats(ModifierSource):
    priority: ClassVar[Priority] = Priority.BASE_STATS

    stats: Stats

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield BaseStatsModifier(stats=self.stats)
