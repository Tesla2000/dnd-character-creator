from typing import assert_never

from dnd.choices.stats_creation.statistic import Statistic
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import NonNegativeInt


class Stats(BaseModel):
    """D&D character statistics.

    All stats are positive integers representing the character's ability scores.
    Typical range is 1-20 for standard characters, with racial bonuses and
    magical items potentially exceeding this.
    """

    model_config = ConfigDict(frozen=True)

    strength: NonNegativeInt
    dexterity: NonNegativeInt
    constitution: NonNegativeInt
    intelligence: NonNegativeInt
    wisdom: NonNegativeInt
    charisma: NonNegativeInt

    def get_stat(self, stat: Statistic) -> int:
        match stat:
            case Statistic.STRENGTH:
                return self.strength
            case Statistic.DEXTERITY:
                return self.dexterity
            case Statistic.CONSTITUTION:
                return self.constitution
            case Statistic.INTELLIGENCE:
                return self.intelligence
            case Statistic.WISDOM:
                return self.wisdom
            case Statistic.CHARISMA:
                return self.charisma
            case _ as never:
                assert_never(never)

    def get_modifier(self, stat: Statistic) -> int:
        return self.get_stat(stat) // 2 - 5
