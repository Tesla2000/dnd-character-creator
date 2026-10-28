from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import ClassVar

from dnd.character.base import Modifier
from dnd.character.stats._stat_change import StatChange
from dnd.choices.stats_creation.statistic import Statistic


class StatModifier(Modifier[object], ABC):
    """Changes one statistic. Modifiers for the same statistic do not replace each other."""

    statistic: ClassVar[Statistic]

    @abstractmethod
    def apply(self, character: object) -> StatChange: ...


class AddStatModifier(StatModifier, ABC):
    """Adds to or reduces one statistic. Positive amounts add, negative amounts reduce."""

    amount: int

    def apply(self, character: object) -> StatChange:
        return StatChange(amount=self.amount)


class StrengthModifier(AddStatModifier):
    statistic: ClassVar[Statistic] = Statistic.STRENGTH


class DexterityModifier(AddStatModifier):
    statistic: ClassVar[Statistic] = Statistic.DEXTERITY


class ConstitutionModifier(AddStatModifier):
    statistic: ClassVar[Statistic] = Statistic.CONSTITUTION


class IntelligenceModifier(AddStatModifier):
    statistic: ClassVar[Statistic] = Statistic.INTELLIGENCE


class WisdomModifier(AddStatModifier):
    statistic: ClassVar[Statistic] = Statistic.WISDOM


class CharismaModifier(AddStatModifier):
    statistic: ClassVar[Statistic] = Statistic.CHARISMA
