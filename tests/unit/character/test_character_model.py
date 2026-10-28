from typing import cast

import pytest
from dnd.character.character import Character
from dnd.character.stats import Stats
from dnd.character.classes import Class
from dnd.character.classes import ClassModifier
from dnd.character.equipment import NoCloak
from dnd.character.equipment import NoHelmet
from dnd.character.armor_class import AcModifier
from dnd.character.base import _Modifier
from dnd.character.base import Modifier
from dnd.character.sight import DarkvisionModifier
from dnd.character.subrace import DwarvenToughnessModifier
from dnd.character.classes import Die
from dnd.character.classes import HitDieModifier
from dnd.character.base import _ModifierSource
from dnd.character.base import ModifierSource
from dnd.character.subrace import HighElfPlayersHandbookRace
from dnd.character.subrace import StandardHumanPlayersHandbookRace
from dnd.getters import AcGetter
from dnd.getters import DarkvisionGetter
from dnd.getters import Getter
from dnd.getters import MaxHealth
from dnd.getters import MaxHealthGetter


AVERAGE_STATS = Stats(
    strength=10,
    dexterity=10,
    constitution=10,
    intelligence=10,
    wisdom=10,
    charisma=10,
)


def character_with(*levels: Class) -> Character:
    modifier = ClassModifier()
    for class_ in levels:
        modifier.level_up(class_)
    return Character(
        class_modifier=modifier,
        race_modifier=StandardHumanPlayersHandbookRace(),
        stats=AVERAGE_STATS,
    )


@pytest.mark.unit
def test_modifier_bases_are_abstract() -> None:
    with pytest.raises(TypeError):
        Modifier()
    with pytest.raises(TypeError):
        ModifierSource()
    assert issubclass(Modifier, _Modifier)
    assert issubclass(ModifierSource, _ModifierSource)


@pytest.mark.unit
def test_leaf_modifiers_apply_their_bonus() -> None:
    character = character_with(Class.WIZARD)
    assert HitDieModifier(die=Die.D8).apply(character) == 8
    assert AcModifier(bonus=2).apply(character) == 2
    assert DarkvisionModifier(range_feet=60).apply(character) == 60


@pytest.mark.unit
def test_dwarven_toughness_applies_character_level() -> None:
    assert DwarvenToughnessModifier().apply(character_with(Class.WIZARD)) == 1


@pytest.mark.unit
def test_character_level_counts_class_levels() -> None:
    assert character_with(Class.WIZARD, Class.FIGHTER).level == 2


@pytest.mark.unit
def test_character_defaults_to_no_helmet_and_no_cloak() -> None:
    character = character_with(Class.WIZARD)
    assert isinstance(character.helmet_modifier, NoHelmet)
    assert isinstance(character.cloak_modifier, NoCloak)


@pytest.mark.unit
def test_character_modifiers_are_flattened_depth_first() -> None:
    character = Character(
        stats=AVERAGE_STATS,
        class_modifier=_fighter_one(),
        race_modifier=HighElfPlayersHandbookRace(),
    )
    assert [type(modifier) for modifier in character.modifiers] == [
        HitDieModifier,
        DarkvisionModifier,
    ]


@pytest.mark.unit
def test_character_rejects_wrong_class_modifier() -> None:
    with pytest.raises(ValueError):
        Character(
            stats=AVERAGE_STATS,
            class_modifier=cast(ClassModifier, 3),
            race_modifier=StandardHumanPlayersHandbookRace(),
        )


@pytest.mark.unit
def test_max_health_rejects_zero_and_negative() -> None:
    with pytest.raises(ValueError):
        MaxHealth(0)
    with pytest.raises(ValueError):
        MaxHealth(-1)
    assert MaxHealth(5) == 5


@pytest.mark.unit
def test_max_health_getter_sums_health_modifiers() -> None:
    assert MaxHealthGetter().get(character_with(Class.WIZARD, Class.WIZARD)) == 6 + 4


@pytest.mark.unit
def test_ac_getter_starts_from_base_and_adds_ac_modifiers() -> None:
    assert AcGetter().get(character_with(Class.WIZARD)) == 10
    assert AcGetter(base=12).get(character_with(Class.WIZARD)) == 12


@pytest.mark.unit
def test_darkvision_getter_takes_largest_and_defaults_to_zero() -> None:
    assert DarkvisionGetter().get(character_with(Class.WIZARD)) == 0
    character = Character(
        stats=AVERAGE_STATS,
        class_modifier=ClassModifier(),
        race_modifier=HighElfPlayersHandbookRace(),
    )
    assert DarkvisionGetter().get(character) == 60


@pytest.mark.unit
def test_getter_base_is_abstract() -> None:
    with pytest.raises(TypeError):
        Getter()


def _fighter_one() -> ClassModifier:
    modifier = ClassModifier()
    modifier.level_up(Class.FIGHTER)
    return modifier
