from __future__ import annotations
from typing import ClassVar
from typing import Never

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.base import ModifierSource
from dnd.character.base import Priority
from dnd.character.stats import FloorChange
from dnd.character.stats import StatChange
from dnd.character.stats import StatModifier
from dnd.choices.stats_creation.statistic import Statistic


class ConstitutionMinimum(StatModifier):
    """Keeps Constitution from being reduced below the minimum."""

    statistic: ClassVar[Statistic] = Statistic.CONSTITUTION
    minimum: int

    def apply(self, character: object) -> StatChange:
        return FloorChange(minimum=self.minimum)


class AmuletOfHealth(ModifierSource):
    """Constitution cannot drop below 19. The HP gain comes from the Constitution modifier."""

    priority: ClassVar[Priority] = Priority.UNORDERED

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield ConstitutionMinimum(minimum=19)
