import pytest
from dnd.character.character import Character
from dnd.character.classes import Class
from dnd.character.classes import ClassModifier
from dnd.character.feature import ToughModifier
from dnd.character.health import HealthModifier
from dnd.character.magical_item import AmuletOfHealth
from dnd.character.magical_item import ConstitutionMinimum
from dnd.character.stats import Stats
from dnd.character.subrace import DwarvenToughnessModifier
from dnd.character.subrace import StandardHumanPlayersHandbookRace
from dnd.choices.stats_creation.statistic import Statistic
from dnd.getters import StatGetter
from dnd.getters import StatModifierGetter
from dnd.getters import MaxHealthGetter


def character_with(
    constitution: int,
    wizard_levels: int,
    magical_items: tuple[AmuletOfHealth, ...] = (),
) -> Character:
    modifier = ClassModifier()
    for _ in range(wizard_levels):
        modifier.level_up(Class.WIZARD)
    return Character(
        class_modifier=modifier,
        race_modifier=StandardHumanPlayersHandbookRace(),
        stats=Stats(
            strength=10,
            dexterity=10,
            constitution=constitution,
            intelligence=10,
            wisdom=10,
            charisma=10,
        ),
        magical_items=magical_items,
    )


@pytest.mark.unit
def test_health_modifier_base_is_abstract() -> None:
    with pytest.raises(TypeError):
        HealthModifier()


@pytest.mark.unit
def test_tough_adds_two_per_level() -> None:
    assert ToughModifier().apply(character_with(constitution=10, wizard_levels=3)) == 6


@pytest.mark.unit
def test_dwarven_toughness_adds_one_per_level() -> None:
    character = character_with(constitution=10, wizard_levels=3)
    assert DwarvenToughnessModifier().apply(character) == 3


@pytest.mark.unit
def test_amulet_of_health_only_raises_constitution_to_nineteen() -> None:
    assert list(AmuletOfHealth().get_modifiers()) == [
        ConstitutionMinimum(statistic=Statistic.CONSTITUTION, minimum=19)
    ]


@pytest.mark.unit
def test_amulet_of_health_sets_effective_constitution_to_at_least_nineteen() -> None:
    character = character_with(
        constitution=10, wizard_levels=1, magical_items=(AmuletOfHealth(),)
    )
    assert StatGetter(statistic=Statistic.CONSTITUTION).get(character) == 19
    assert StatModifierGetter(statistic=Statistic.CONSTITUTION).get(character) == 4


@pytest.mark.unit
def test_constitution_minimum_applies_its_floor() -> None:
    character = character_with(constitution=10, wizard_levels=1)
    floor = ConstitutionMinimum(statistic=Statistic.CONSTITUTION, minimum=19)
    assert floor.apply(character) == 19


@pytest.mark.unit
def test_amulet_of_health_keeps_higher_constitution() -> None:
    character = character_with(
        constitution=20, wizard_levels=1, magical_items=(AmuletOfHealth(),)
    )
    assert StatGetter(statistic=Statistic.CONSTITUTION).get(character) == 20


@pytest.mark.unit
def test_constitution_modifier_adds_to_every_level_of_max_health() -> None:
    without_amulet = character_with(constitution=10, wizard_levels=2)
    with_amulet = character_with(
        constitution=10, wizard_levels=2, magical_items=(AmuletOfHealth(),)
    )
    assert MaxHealthGetter().get(without_amulet) == 6 + 4
    assert MaxHealthGetter().get(with_amulet) == (6 + 4) + (4 + 4)
