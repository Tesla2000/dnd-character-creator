from __future__ import annotations

from dnd_character_creator.choices.class_creation.character_class import (
    Class,
)
from dnd_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from frozendict import frozendict

spellcasting_ability_map: frozendict[Class, Statistic] = frozendict(
    {
        Class.BARD: Statistic.CHARISMA,
        Class.CLERIC: Statistic.WISDOM,
        Class.DRUID: Statistic.WISDOM,
        Class.FIGHTER: Statistic.INTELLIGENCE,  # For Eldritch Knight subclass
        Class.PALADIN: Statistic.CHARISMA,
        Class.RANGER: Statistic.WISDOM,
        Class.ROGUE: Statistic.INTELLIGENCE,  # For Arcane Trickster subclass
        Class.SORCERER: Statistic.CHARISMA,
        Class.WARLOCK: Statistic.CHARISMA,
        Class.WIZARD: Statistic.INTELLIGENCE,
        Class.ARTIFICER: Statistic.INTELLIGENCE,
    }
)
