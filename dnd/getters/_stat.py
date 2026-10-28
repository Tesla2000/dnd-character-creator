from __future__ import annotations

import logging
from collections.abc import Sequence
from typing import ClassVar
from typing import Never

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.stats import BaseStatsModifier
from dnd.character.stats import Stat
from dnd.character.stats import StatLike
from dnd.character.stats import StatModifier
from dnd.character.stats import StatValue
from dnd.choices.stats_creation.statistic import Statistic
from dnd.getters._getter import Getter
from dnd.getters._getter import PrioritizedCharacter

logger = logging.getLogger(__name__)


class StatGetter(Getter[PrioritizedCharacter, StatValue]):
    statistic: ClassVar[Statistic]

    def _get(
        self,
        character: PrioritizedCharacter,
        modifiers: Sequence[_Modifier[Never] | _ModifierSource],
    ) -> StatValue:
        bases = [
            modifier.apply(character)
            for modifier in modifiers
            if isinstance(modifier, BaseStatsModifier)
        ]
        if len(bases) > 1:
            logger.warning("Base stats set %d times, using the last", len(bases))
        if not bases:
            raise ValueError(f"No base stats set, cannot read {self.statistic}")
        stat: StatLike = Stat(
            statistic=self.statistic, value=bases[-1].get_stat(self.statistic)
        )
        for modifier in modifiers:
            if (
                isinstance(modifier, StatModifier)
                and modifier.statistic == self.statistic
            ):
                stat = modifier.apply(character).reduce(stat)
        return StatValue(statistic=self.statistic, value=stat.value)


class StrengthGetter(StatGetter):
    statistic: ClassVar[Statistic] = Statistic.STRENGTH


class DexterityGetter(StatGetter):
    statistic: ClassVar[Statistic] = Statistic.DEXTERITY


class ConstitutionGetter(StatGetter):
    statistic: ClassVar[Statistic] = Statistic.CONSTITUTION


class IntelligenceGetter(StatGetter):
    statistic: ClassVar[Statistic] = Statistic.INTELLIGENCE


class WisdomGetter(StatGetter):
    statistic: ClassVar[Statistic] = Statistic.WISDOM


class CharismaGetter(StatGetter):
    statistic: ClassVar[Statistic] = Statistic.CHARISMA
