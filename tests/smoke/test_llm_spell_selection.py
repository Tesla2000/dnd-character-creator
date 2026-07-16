import pytest

from dnd.character.blueprint.building_blocks.level_up.spell_assignment.llm import (
    SorcererLLMSpellAssigner,
    WizardLLMSpellAssigner,
)
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.class_levels import ClassLevels
from dnd.character.spells.spell_slots import WizardCantrip, WizardFirstLevel
from dnd.character.spells.spell_slots import SorcererCantrip, SorcererFirstLevel


@pytest.mark.smoke
class TestWizardLLMSpellSelection:
    def test_wizard_level_1_selects_cantrips_and_first_level(self) -> None:
        assigner = WizardLLMSpellAssigner(
            character_description="Bookish scholar obsessed with transmutation magic"
        )
        state = Blueprint(classes=ClassLevels(wizard=1))
        result = assigner.apply(state)

        assert len(result.spells.cantrips) > 0
        assert all(isinstance(s, WizardCantrip) for s in result.spells.cantrips)
        assert len(result.spells.first_level_spells) > 0
        assert all(
            isinstance(s, WizardFirstLevel) for s in result.spells.first_level_spells
        )


@pytest.mark.smoke
class TestSorcererLLMSpellSelection:
    def test_sorcerer_level_1_selects_cantrips_and_first_level(self) -> None:
        assigner = SorcererLLMSpellAssigner(
            character_description="Draconic sorcerer with fire affinity"
        )
        state = Blueprint(classes=ClassLevels(sorcerer=1))
        result = assigner.apply(state)

        assert len(result.spells.cantrips) > 0
        assert all(isinstance(s, SorcererCantrip) for s in result.spells.cantrips)
        assert len(result.spells.first_level_spells) > 0
        assert all(
            isinstance(s, SorcererFirstLevel) for s in result.spells.first_level_spells
        )
