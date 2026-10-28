from collections.abc import Callable
from typing import cast

import pytest
from dnd.character.classes import ArtificerSubclassField
from dnd.character.classes import BarbarianSubclassField
from dnd.character.classes import BardSubclassField
from dnd.character.classes import ClassLevelBase
from dnd.character.classes import ClericSubclassField
from dnd.character.classes import DruidSubclassField
from dnd.character.classes import ArtificerSubclass
from dnd.character.classes import BardSubclass
from dnd.character.classes import BarbarianSubclass
from dnd.character.classes import Class
from dnd.character.classes import ClericSubclass
from dnd.character.classes import DruidSubclass
from dnd.character.classes import FighterSubclass
from dnd.character.classes import MonkSubclass
from dnd.character.classes import PaladinSubclass
from dnd.character.classes import RangerSubclass
from dnd.character.classes import RogueSubclass
from dnd.character.classes import SorcererSubclass
from dnd.character.classes import WarlockSubclass
from dnd.character.classes import WizardSubclass
from dnd.character.classes import FighterSubclassField
from dnd.character.classes import MonkSubclassField
from dnd.character.classes import PaladinSubclassField
from dnd.character.classes import RangerSubclassField
from dnd.character.classes import RogueSubclassField
from dnd.character.classes import SorcererSubclassField
from dnd.character.classes import WarlockSubclassField
from dnd.character.classes import SchoolSlot
from dnd.character.classes import WizardSubclassField
from dnd.character.level import Level
from dnd.character.classes import HitDieModifier


def assert_levels_for[E](
    level_for: Callable[[Level, E], ClassLevelBase],
    subclasses: tuple[E, ...],
    class_: Class,
) -> None:
    for subclass in subclasses:
        for number in Level:
            level = level_for(number, subclass)
            assert level.number == number
            assert level.class_ == class_
            assert list(level.get_modifiers()) == [HitDieModifier(die=level.hit_die)]


@pytest.mark.unit
def test_artificer_levels() -> None:
    assert_levels_for(
        ArtificerSubclassField.level, tuple(ArtificerSubclass), Class.ARTIFICER
    )


@pytest.mark.unit
def test_barbarian_levels() -> None:
    assert_levels_for(
        BarbarianSubclassField.level, tuple(BarbarianSubclass), Class.BARBARIAN
    )


@pytest.mark.unit
def test_bard_levels() -> None:
    assert_levels_for(BardSubclassField.level, tuple(BardSubclass), Class.BARD)


@pytest.mark.unit
def test_cleric_levels() -> None:
    assert_levels_for(ClericSubclassField.level, tuple(ClericSubclass), Class.CLERIC)


@pytest.mark.unit
def test_druid_levels() -> None:
    assert_levels_for(DruidSubclassField.level, tuple(DruidSubclass), Class.DRUID)


@pytest.mark.unit
def test_fighter_levels() -> None:
    assert_levels_for(FighterSubclassField.level, tuple(FighterSubclass), Class.FIGHTER)


@pytest.mark.unit
def test_monk_levels() -> None:
    assert_levels_for(MonkSubclassField.level, tuple(MonkSubclass), Class.MONK)


@pytest.mark.unit
def test_paladin_levels() -> None:
    assert_levels_for(PaladinSubclassField.level, tuple(PaladinSubclass), Class.PALADIN)


@pytest.mark.unit
def test_ranger_levels() -> None:
    assert_levels_for(RangerSubclassField.level, tuple(RangerSubclass), Class.RANGER)


@pytest.mark.unit
def test_rogue_levels() -> None:
    assert_levels_for(RogueSubclassField.level, tuple(RogueSubclass), Class.ROGUE)


@pytest.mark.unit
def test_sorcerer_levels() -> None:
    assert_levels_for(
        SorcererSubclassField.level, tuple(SorcererSubclass), Class.SORCERER
    )


@pytest.mark.unit
def test_warlock_levels() -> None:
    assert_levels_for(WarlockSubclassField.level, tuple(WarlockSubclass), Class.WARLOCK)


@pytest.mark.unit
def test_wizard_levels() -> None:
    assert_levels_for(WizardSubclassField.level, tuple(WizardSubclass), Class.WIZARD)


@pytest.mark.unit
def test_wizard_level_rejects_value_outside_level_enum() -> None:
    with pytest.raises(AssertionError):
        WizardSubclassField.level(cast(Level, 0), WizardSubclass.ABJURATION)


@pytest.mark.unit
def test_wizard_school_levels_reject_value_outside_subclass_enum() -> None:
    with pytest.raises(AssertionError):
        WizardSubclassField._school_levels(cast(WizardSubclass, "not a school"))


@pytest.mark.unit
def test_wizard_school_level_rejects_value_outside_slot_enum() -> None:
    with pytest.raises(AssertionError):
        WizardSubclassField._school_level(
            cast(SchoolSlot, "not a slot"), WizardSubclass.ABJURATION
        )
