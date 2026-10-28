import importlib
import pkgutil
from types import ModuleType

import pytest
import dnd.character.subrace as race_modifiers
from dnd.character.equipment import CloakModifier
from dnd.character.equipment import NoCloak
from dnd.character.equipment import HelmetModifier
from dnd.character.equipment import NoHelmet
from dnd.character.sight import DarkvisionModifier
from dnd.character.subrace import DwarvenToughnessModifier
from dnd.character.subrace import RaceModifier
from dnd.character.subrace import HillDwarfPlayersHandbookRace
from dnd.character.subrace import HighElfPlayersHandbookRace
from dnd.character.subrace import StandardHumanPlayersHandbookRace


def race_modules() -> list[ModuleType]:
    return [
        importlib.import_module(f"{race_modifiers.__name__}.{info.name}")
        for info in pkgutil.iter_modules(race_modifiers.__path__)
        if info.name != "base"
    ]


def race_classes() -> list[type[RaceModifier]]:
    classes: list[type[RaceModifier]] = []
    for module in race_modules():
        for value in vars(module).values():
            if (
                isinstance(value, type)
                and issubclass(value, RaceModifier)
                and value.__module__ == module.__name__
                and not value.__abstractmethods__
            ):
                classes.append(value)
    return classes


@pytest.mark.unit
def test_every_race_class_builds_its_modifiers() -> None:
    classes = race_classes()
    assert len(classes) == 138
    for race_class in classes:
        modifiers = list(race_class().get_modifiers())
        assert all(
            isinstance(modifier, (DarkvisionModifier, DwarvenToughnessModifier))
            for modifier in modifiers
        )


@pytest.mark.unit
def test_hill_dwarf_has_darkvision_and_toughness() -> None:
    assert list(HillDwarfPlayersHandbookRace().get_modifiers()) == [
        DarkvisionModifier(range_feet=60),
        DwarvenToughnessModifier(),
    ]


@pytest.mark.unit
def test_high_elf_has_darkvision() -> None:
    assert list(HighElfPlayersHandbookRace().get_modifiers()) == [
        DarkvisionModifier(range_feet=60),
    ]


@pytest.mark.unit
def test_human_has_no_modifiers() -> None:
    assert list(StandardHumanPlayersHandbookRace().get_modifiers()) == []


@pytest.mark.unit
def test_race_base_is_abstract() -> None:
    with pytest.raises(TypeError):
        RaceModifier()


@pytest.mark.unit
def test_helmet_and_cloak_bases_are_abstract() -> None:
    with pytest.raises(TypeError):
        HelmetModifier()
    with pytest.raises(TypeError):
        CloakModifier()


@pytest.mark.unit
def test_no_helmet_and_no_cloak_produce_no_modifiers() -> None:
    assert list(NoHelmet().get_modifiers()) == []
    assert list(NoCloak().get_modifiers()) == []
