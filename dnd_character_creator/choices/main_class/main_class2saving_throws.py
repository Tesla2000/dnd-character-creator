from __future__ import annotations

from dnd_character_creator.choices.class_creation.character_class import (
    Class,
)
from dnd_character_creator.choices.stats_creation.statistic import (
    Statistic,
)

main_class2saving_throws = {
    Class.BARBARIAN: {Statistic.STRENGTH, Statistic.CONSTITUTION},
    Class.BARD: {Statistic.DEXTERITY, Statistic.CHARISMA},
    Class.CLERIC: {Statistic.WISDOM, Statistic.CHARISMA},
    Class.DRUID: {Statistic.INTELLIGENCE, Statistic.WISDOM},
    Class.FIGHTER: {Statistic.STRENGTH, Statistic.CONSTITUTION},
    Class.MONK: {Statistic.STRENGTH, Statistic.DEXTERITY},
    Class.PALADIN: {Statistic.WISDOM, Statistic.CHARISMA},
    Class.RANGER: {Statistic.STRENGTH, Statistic.DEXTERITY},
    Class.ROGUE: {Statistic.DEXTERITY, Statistic.INTELLIGENCE},
    Class.SORCERER: {Statistic.CONSTITUTION, Statistic.CHARISMA},
    Class.WARLOCK: {Statistic.WISDOM, Statistic.CHARISMA},
    Class.WIZARD: {Statistic.INTELLIGENCE, Statistic.WISDOM},
    Class.ARTIFICER: {Statistic.CONSTITUTION, Statistic.INTELLIGENCE},
}
