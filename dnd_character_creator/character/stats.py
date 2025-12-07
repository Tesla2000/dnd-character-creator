from __future__ import annotations

from typing import Mapping, Self

from pydantic import BaseModel, PositiveInt, ConfigDict

from dnd_character_creator.choices.stats_creation.statistic import Statistic


class Stats(BaseModel):
    """D&D character statistics.

    All stats are positive integers representing the character's ability scores.
    Typical range is 1-20 for standard characters, with racial bonuses and
    magical items potentially exceeding this.
    """

    model_config = ConfigDict(frozen=True)

    strength: PositiveInt
    dexterity: PositiveInt
    constitution: PositiveInt
    intelligence: PositiveInt
    wisdom: PositiveInt
    charisma: PositiveInt

    @classmethod
    def from_mapping(cls, mapping: Mapping[Statistic, int]) -> Self:
        return cls(
            strength=mapping[Statistic.STRENGTH],
            dexterity=mapping[Statistic.DEXTERITY],
            constitution=mapping[Statistic.CONSTITUTION],
            intelligence=mapping[Statistic.INTELLIGENCE],
            wisdom=mapping[Statistic.WISDOM],
            charisma=mapping[Statistic.CHARISMA],
        )
