from dataclasses import dataclass
from typing import cast

import pytest
from dnd.character.armor.armor import Armor
from dnd.character.armor.category import ArmorCategory
from dnd.character.armor.names import ArmorName
from dnd.character.armor.names import SHIELD
from dnd.character.race import Race
from dnd.character.stats import Stats
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import ArmorProficiency


@dataclass(frozen=True)
class ArmorContext:
    race: Race | None
    stats: Stats
    other_equipment: tuple[str, ...]
    armor_proficiencies: frozenset[ArmorProficiency]


def context_with_dexterity(
    dexterity: int,
    proficiencies: frozenset[ArmorProficiency] = frozenset(),
    race: Race | None = None,
    other_equipment: tuple[str, ...] = (),
) -> ArmorContext:
    return ArmorContext(
        race=race,
        stats=Stats(
            strength=10,
            dexterity=dexterity,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        ),
        other_equipment=other_equipment,
        armor_proficiencies=proficiencies,
    )


def armor_of(category: ArmorCategory, base_ac: int) -> Armor:
    return Armor(
        name=ArmorName.ROBE_OF_THE_ARCHMAGI,
        category=category,
        disadvantage_on_stealth=False,
        base_ac=base_ac,
    )


@pytest.mark.unit
def test_get_stat_reads_every_statistic() -> None:
    stats = Stats(
        strength=8,
        dexterity=14,
        constitution=13,
        intelligence=12,
        wisdom=10,
        charisma=9,
    )
    assert stats.get_stat(Statistic.STRENGTH) == 8
    assert stats.get_stat(Statistic.DEXTERITY) == 14
    assert stats.get_stat(Statistic.CONSTITUTION) == 13
    assert stats.get_stat(Statistic.INTELLIGENCE) == 12
    assert stats.get_stat(Statistic.WISDOM) == 10
    assert stats.get_stat(Statistic.CHARISMA) == 9
    assert stats.get_modifier(Statistic.DEXTERITY) == 2


@pytest.mark.unit
def test_get_stat_rejects_value_outside_statistic_enum() -> None:
    stats = context_with_dexterity(14).stats
    with pytest.raises(AssertionError):
        stats.get_stat(cast(Statistic, "not a statistic"))


@pytest.mark.unit
def test_heavy_armor_with_proficiency_ignores_dexterity() -> None:
    armor = armor_of(ArmorCategory.HEAVY, base_ac=14)
    context = context_with_dexterity(
        18, proficiencies=frozenset({ArmorProficiency.HEAVY_ARMOR})
    )
    assert armor.apply(context) == 14


@pytest.mark.unit
def test_heavy_armor_without_proficiency_adds_dexterity() -> None:
    armor = armor_of(ArmorCategory.HEAVY, base_ac=14)
    assert armor.apply(context_with_dexterity(14)) == 14 + 2


@pytest.mark.unit
def test_medium_armor_with_all_armor_proficiency_caps_dexterity_at_two() -> None:
    armor = armor_of(ArmorCategory.MEDIUM, base_ac=12)
    context = context_with_dexterity(
        18, proficiencies=frozenset({ArmorProficiency.ALL_ARMOR})
    )
    assert armor.apply(context) == 12 + 2


@pytest.mark.unit
def test_medium_armor_without_proficiency_adds_full_dexterity() -> None:
    armor = armor_of(ArmorCategory.MEDIUM, base_ac=12)
    assert armor.apply(context_with_dexterity(18)) == 12 + 4


@pytest.mark.unit
def test_light_armor_adds_full_dexterity() -> None:
    armor = armor_of(ArmorCategory.LIGHT, base_ac=11)
    assert armor.apply(context_with_dexterity(16)) == 11 + 3


@pytest.mark.unit
def test_lizardfolk_natural_armor_has_a_floor_of_thirteen_plus_dexterity() -> None:
    armor = armor_of(ArmorCategory.LIGHT, base_ac=10)
    context = context_with_dexterity(14, race=Race.LIZARDFOLK)
    assert armor.apply(context) == 13 + 2


@pytest.mark.unit
def test_shield_adds_two_when_worn_and_proficient() -> None:
    armor = armor_of(ArmorCategory.LIGHT, base_ac=11)
    context = context_with_dexterity(
        12,
        proficiencies=frozenset({ArmorProficiency.SHIELDS}),
        other_equipment=(SHIELD,),
    )
    assert armor.apply(context) == 11 + 1 + 2
