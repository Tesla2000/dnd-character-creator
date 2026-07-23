import pytest

from dnd.character.blueprint.character_data import CharacterData
from dnd.character.blueprint.states._caster_info import CasterInfo
from dnd.character.blueprint.states.barbarian._info import BarbarianInfo
from dnd.character.blueprint.states.basic_presentable import PresentableBasicBlueprint
from dnd.character.blueprint.states.sorcerer._info import SorcererInfo
from dnd.character.blueprint.states.sorcerer.presentable import (
    PresentableSorcererBlueprint,
)
from dnd.character.blueprint.states.wizard._info import WizardLevel20Info
from dnd.character.blueprint.states.wizard.level18 import WizardLevel18Blueprint
from dnd.character.blueprint.states.wizard.level20 import WizardLevel20Blueprint
from dnd.character.blueprint.states.wizard.presentable import (
    PresentableWizardLevel20Blueprint,
)
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.race.race import Race
from dnd.character.spells.max_spell_levels import FULL_CASTER_SPELL_SLOTS
from dnd.character.stats import Stats

_STATS = Stats(
    strength=10,
    dexterity=10,
    constitution=10,
    intelligence=18,
    wisdom=10,
    charisma=10,
)


@pytest.mark.unit
class TestPresentableBasicBlueprint:
    def test_to_presentable_character_produces_presentable_character(self) -> None:
        bp = PresentableBasicBlueprint(
            race=Race.HUMAN,
            stats=_STATS,
            health_base=10,
            character_data=CharacterData(name="Basic Test"),
        )
        character = bp.to_presentable_character()
        assert isinstance(character, PresentableCharacter)
        assert character.stats == _STATS
        assert character.race is Race.HUMAN


@pytest.mark.unit
class TestWizardLevelBlueprints:
    def test_wizard_level18_blueprint_constructs(self) -> None:
        blueprint = WizardLevel18Blueprint()
        assert blueprint is not None

    def test_wizard_level20_blueprint_constructs(self) -> None:
        blueprint = WizardLevel20Blueprint()
        assert blueprint is not None


@pytest.mark.unit
class TestPresentableWizardLevel20Blueprint:
    def test_to_presentable_character_produces_presentable_character(self) -> None:
        bp = PresentableWizardLevel20Blueprint(
            race=Race.ELF,
            stats=_STATS,
            health_base=10,
            character_data=CharacterData(name="Wizard Test"),
            caster=CasterInfo(spell_slots=FULL_CASTER_SPELL_SLOTS[0], caster_level=1),
            wizard=WizardLevel20Info(),
        )
        character = bp.to_presentable_character()
        assert isinstance(character, PresentableCharacter)
        assert character.race is Race.ELF


@pytest.mark.unit
class TestPresentableSorcererBlueprint:
    def test_to_presentable_character_produces_presentable_character(self) -> None:
        bp = PresentableSorcererBlueprint(
            race=Race.TIEFLING,
            stats=_STATS,
            health_base=6,
            character_data=CharacterData(name="Sorcerer Test"),
            spell_slots=FULL_CASTER_SPELL_SLOTS[0],
            caster_level=1,
        )
        character = bp.to_presentable_character()
        assert isinstance(character, PresentableCharacter)
        assert character.race is Race.TIEFLING


@pytest.mark.unit
class TestSorcererInfo:
    def test_constructs_with_defaults(self) -> None:
        info = SorcererInfo()
        assert info.metamagic_options == ()
        assert info.n_metamagic_choices == 0


@pytest.mark.unit
class TestBarbarianInfo:
    def test_constructs(self) -> None:
        info = BarbarianInfo()
        assert info is not None
