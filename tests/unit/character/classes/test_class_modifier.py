from typing import cast

import pytest
from dnd.character.character import Character
from dnd.character.stats import Stats
from dnd.character.classes import ArtificerSubclassField
from dnd.character.classes import BarbarianSubclassField
from dnd.character.classes import BardSubclassField
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
from dnd.character.classes import ClassModifier
from dnd.character.classes import MonkSubclassField
from dnd.character.classes import PaladinSubclassField
from dnd.character.classes import RangerSubclassField
from dnd.character.classes import RogueSubclassField
from dnd.character.classes import SorcererSubclassField
from dnd.character.classes import WarlockSubclassField
from dnd.character.classes import WizardSubclassField
from dnd.character.subrace import DwarvenToughnessModifier
from dnd.character.subrace import HillDwarfPlayersHandbookRace
from dnd.getters import MaxHealthGetter


AVERAGE_STATS = Stats(
    strength=10,
    dexterity=10,
    constitution=10,
    intelligence=10,
    wisdom=10,
    charisma=10,
)

CLASSES = (
    Class.ARTIFICER,
    Class.BARBARIAN,
    Class.BARD,
    Class.CLERIC,
    Class.DRUID,
    Class.FIGHTER,
    Class.MONK,
    Class.PALADIN,
    Class.RANGER,
    Class.ROGUE,
    Class.SORCERER,
    Class.WARLOCK,
    Class.WIZARD,
)


@pytest.mark.unit
@pytest.mark.parametrize("class_", CLASSES)
def test_level_up_twenty_levels_in_each_class(class_: Class) -> None:
    modifier = ClassModifier()
    for _ in range(20):
        modifier.level_up(class_)
    assert modifier.get_total_level() == 20
    assert modifier.class_level(class_) == 20


@pytest.mark.unit
def test_level_up_rejects_value_outside_class_enum() -> None:
    with pytest.raises(AssertionError):
        ClassModifier().level_up(cast(Class, "not a class"))


@pytest.mark.unit
def test_level_up_past_twenty_raises() -> None:
    modifier = ClassModifier()
    for _ in range(20):
        modifier.level_up(Class.WIZARD)
    with pytest.raises(ValueError):
        modifier.level_up(Class.WIZARD)


@pytest.mark.unit
def test_first_character_level_takes_the_maximum_hit_die() -> None:
    modifier = ClassModifier()
    modifier.level_up(Class.FIGHTER)
    character = Character(
        stats=AVERAGE_STATS,
        class_modifier=modifier,
        race_modifier=HillDwarfPlayersHandbookRace(),
    )
    assert list(modifier.get_modifiers()) == [modifier._levels[0]]
    assert MaxHealthGetter().get(character) == 10 + 1


@pytest.mark.unit
def test_later_levels_take_the_average_hit_die() -> None:
    modifier = ClassModifier()
    modifier.level_up(Class.FIGHTER)
    modifier.level_up(Class.WIZARD)
    assert [type(source).__name__ for source in modifier.get_modifiers()] == [
        "FighterLevel1",
        "WizardLevel1",
    ]


@pytest.mark.unit
def test_multiclass_counts_levels_per_class() -> None:
    modifier = ClassModifier()
    modifier.level_up(Class.FIGHTER)
    modifier.level_up(Class.WIZARD)
    modifier.level_up(Class.FIGHTER)
    assert modifier.class_level(Class.FIGHTER) == 2
    assert modifier.class_level(Class.WIZARD) == 1
    assert modifier.get_total_level() == 3


@pytest.mark.unit
def test_wizard_subclass_switch_migrates_school_levels() -> None:
    modifier = ClassModifier()
    modifier.level_up(Class.WIZARD)
    modifier.wizard_subclass = WizardSubclass.WAR_MAGIC
    modifier.level_up(Class.WIZARD)
    modifier.wizard_subclass = WizardSubclass.DIVINATION
    assert [type(level).__name__ for level in modifier._levels] == [
        "WizardLevel1",
        "WizardLevel2Divination",
    ]


@pytest.mark.unit
def test_barbarian_subclass_switch_migrates_path_levels() -> None:
    modifier = ClassModifier()
    for _ in range(3):
        modifier.level_up(Class.BARBARIAN)
    modifier.barbarian_subclass = BarbarianSubclass.BERSERKER
    modifier.barbarian_subclass = BarbarianSubclass.ZEALOT
    assert [type(level).__name__ for level in modifier._levels][-1] == (
        "BarbarianLevel3Zealot"
    )


@pytest.mark.unit
def test_sorcerer_subclass_switch_migrates_origin_levels() -> None:
    modifier = ClassModifier()
    modifier.level_up(Class.SORCERER)
    modifier.sorcerer_subclass = SorcererSubclass.WILD_MAGIC
    modifier.sorcerer_subclass = SorcererSubclass.DIVINE_SOUL
    assert [type(level).__name__ for level in modifier._levels] == [
        "SorcererLevel1DivineSoul"
    ]


@pytest.mark.unit
def test_wizard_subclass_defaults_to_first_member() -> None:
    assert (
        WizardSubclassField().__get__(None, ClassModifier) == WizardSubclass.ABJURATION
    )
    assert ClassModifier().wizard_subclass == WizardSubclass.ABJURATION


@pytest.mark.unit
def test_barbarian_subclass_defaults_to_first_member() -> None:
    assert (
        BarbarianSubclassField().__get__(None, ClassModifier)
        == BarbarianSubclass.ANCESTRAL_GUARDIAN
    )
    assert ClassModifier().barbarian_subclass == BarbarianSubclass.ANCESTRAL_GUARDIAN


@pytest.mark.unit
def test_sorcerer_subclass_defaults_to_first_member() -> None:
    assert (
        SorcererSubclassField().__get__(None, ClassModifier)
        == SorcererSubclass.ABERRANT_MIND
    )
    assert ClassModifier().sorcerer_subclass == SorcererSubclass.ABERRANT_MIND


@pytest.mark.unit
def test_skeleton_subclass_fields_store_and_read_back() -> None:
    modifier = ClassModifier()
    modifier.artificer_subclass = ArtificerSubclass.ARMORER
    modifier.bard_subclass = BardSubclass.LORE
    modifier.cleric_subclass = ClericSubclass.LIFE
    modifier.druid_subclass = DruidSubclass.MOON
    modifier.fighter_subclass = FighterSubclass.CHAMPION
    modifier.monk_subclass = MonkSubclass.OPEN_HAND
    modifier.paladin_subclass = PaladinSubclass.DEVOTION
    modifier.ranger_subclass = RangerSubclass.HUNTER
    modifier.rogue_subclass = RogueSubclass.THIEF
    modifier.warlock_subclass = WarlockSubclass.FIEND
    assert modifier.artificer_subclass == ArtificerSubclass.ARMORER
    assert modifier.bard_subclass == BardSubclass.LORE
    assert modifier.cleric_subclass == ClericSubclass.LIFE
    assert modifier.druid_subclass == DruidSubclass.MOON
    assert modifier.fighter_subclass == FighterSubclass.CHAMPION
    assert modifier.monk_subclass == MonkSubclass.OPEN_HAND
    assert modifier.paladin_subclass == PaladinSubclass.DEVOTION
    assert modifier.ranger_subclass == RangerSubclass.HUNTER
    assert modifier.rogue_subclass == RogueSubclass.THIEF
    assert modifier.warlock_subclass == WarlockSubclass.FIEND


@pytest.mark.unit
def test_skeleton_subclass_field_defaults() -> None:
    assert (
        ArtificerSubclassField().__get__(None, ClassModifier)
        == ArtificerSubclass.ALCHEMIST
    )
    assert BardSubclassField().__get__(None, ClassModifier) == BardSubclass.CREATION
    assert ClericSubclassField().__get__(None, ClassModifier) == ClericSubclass.ARCANA
    assert DruidSubclassField().__get__(None, ClassModifier) == DruidSubclass.DREAMS
    assert (
        FighterSubclassField().__get__(None, ClassModifier)
        == FighterSubclass.ARCANE_ARCHER
    )
    assert MonkSubclassField().__get__(None, ClassModifier) == MonkSubclass.MERCY
    assert (
        PaladinSubclassField().__get__(None, ClassModifier) == PaladinSubclass.ANCIENTS
    )
    assert (
        RangerSubclassField().__get__(None, ClassModifier)
        == RangerSubclass.BEAST_MASTER
    )
    assert (
        RogueSubclassField().__get__(None, ClassModifier)
        == RogueSubclass.ARCANE_TRICKSTER
    )
    assert (
        WarlockSubclassField().__get__(None, ClassModifier) == WarlockSubclass.ARCHFEY
    )


@pytest.mark.unit
def test_dwarven_toughness_counts_character_level() -> None:
    modifier = ClassModifier()
    modifier.level_up(Class.WIZARD)
    modifier.level_up(Class.WIZARD)
    character = Character(
        stats=AVERAGE_STATS,
        class_modifier=modifier,
        race_modifier=HillDwarfPlayersHandbookRace(),
    )
    assert DwarvenToughnessModifier().apply(character) == 2


@pytest.mark.unit
def test_wizard_switch_rebuilds_every_school_slot() -> None:
    modifier = ClassModifier()
    for _ in range(20):
        modifier.level_up(Class.WIZARD)
    modifier.wizard_subclass = WizardSubclass.TRANSMUTATION
    assert [
        type(level).__name__
        for level in modifier._levels
        if "Transmutation" in type(level).__name__
    ] == [
        "WizardLevel2Transmutation",
        "WizardLevel6Transmutation",
        "WizardLevel10Transmutation",
        "WizardLevel14Transmutation",
    ]


@pytest.mark.unit
def test_barbarian_switch_rebuilds_every_path_slot() -> None:
    modifier = ClassModifier()
    for _ in range(20):
        modifier.level_up(Class.BARBARIAN)
    modifier.barbarian_subclass = BarbarianSubclass.GIANT
    assert [
        type(level).__name__
        for level in modifier._levels
        if "Giant" in type(level).__name__
    ] == [
        "BarbarianLevel3Giant",
        "BarbarianLevel6Giant",
        "BarbarianLevel10Giant",
        "BarbarianLevel14Giant",
    ]


@pytest.mark.unit
def test_sorcerer_switch_rebuilds_every_origin_slot() -> None:
    modifier = ClassModifier()
    for _ in range(20):
        modifier.level_up(Class.SORCERER)
    modifier.sorcerer_subclass = SorcererSubclass.STORM_SORCERY
    assert [
        type(level).__name__
        for level in modifier._levels
        if "StormSorcery" in type(level).__name__
    ] == [
        "SorcererLevel1StormSorcery",
        "SorcererLevel6StormSorcery",
        "SorcererLevel14StormSorcery",
        "SorcererLevel18StormSorcery",
    ]
