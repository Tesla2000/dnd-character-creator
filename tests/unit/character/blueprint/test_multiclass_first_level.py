import pytest

from dnd.character.blueprint.building_blocks.level_up.barbarian.level_1 import (
    BarbarianLevel1,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    D8HealthIncreaseAverage,
    D12HealthIncreaseAverage,
    D6HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.rogue.level_1 import (
    RogueLevel1,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.draconic_bloodline.level_1 import (
    SorcererLevel1DraconicBloodline,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.level_1 import (
    WizardLevel1,
)
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.class_levels import ClassLevels
from dnd.character.race.race import Race
from dnd.character.stats import Stats
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import ArmorProficiency
from dnd.other_profficiencies import WeaponProficiency
from dnd.skill_proficiency import Skill

_STATS = Stats(
    strength=15,
    dexterity=13,
    constitution=14,
    intelligence=8,
    wisdom=12,
    charisma=10,
)

_EMPTY_BP = Blueprint(race=Race.HUMAN, stats=_STATS, health_base=6)
_WIZARD_1_BP = _EMPTY_BP.model_copy(update={"classes": ClassLevels(wizard=1)})
_BARB_1_BP = _EMPTY_BP.model_copy(update={"classes": ClassLevels(barbarian=1)})

_BARB_HEALTH = D12HealthIncreaseAverage()
_WIZ_HEALTH = D6HealthIncreaseAverage()
_SOR_HEALTH = D6HealthIncreaseAverage()
_ROGUE_HEALTH = D8HealthIncreaseAverage()

# Rogue's expertise step reads skill_proficiencies unconditionally (even when
# multiclassing), unlike saving throws/skill choices which are first-class-only.
# _WIZARD_1_BP never ran a real skill-choice resolver, so it has zero skills --
# Rogue tests need a variant that actually has some to choose expertise from.
_WIZARD_1_BP_WITH_SKILLS = _WIZARD_1_BP.model_copy(
    update={"skill_proficiencies": (Skill.ARCANA, Skill.HISTORY)}
)


# ---------------------------------------------------------------------------
# Barbarian multiclass (character already has wizard 1)
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_barbarian_multiclass_no_strength_saving_throw() -> None:
    result = BarbarianLevel1(health_increase=_BARB_HEALTH).apply(_WIZARD_1_BP)
    assert Statistic.STRENGTH not in result.saving_throw_proficiencies


@pytest.mark.unit
def test_barbarian_multiclass_no_constitution_saving_throw() -> None:
    result = BarbarianLevel1(health_increase=_BARB_HEALTH).apply(_WIZARD_1_BP)
    assert Statistic.CONSTITUTION not in result.saving_throw_proficiencies


@pytest.mark.unit
def test_barbarian_multiclass_keeps_armor_proficiencies() -> None:
    result = BarbarianLevel1(health_increase=_BARB_HEALTH).apply(_WIZARD_1_BP)
    assert ArmorProficiency.MEDIUM_ARMOR in result.armor_proficiencies
    assert ArmorProficiency.SHIELDS in result.armor_proficiencies


@pytest.mark.unit
def test_barbarian_multiclass_keeps_weapon_proficiencies() -> None:
    result = BarbarianLevel1(health_increase=_BARB_HEALTH).apply(_WIZARD_1_BP)
    assert WeaponProficiency.MARTIAL_WEAPON in result.weapon_proficiencies
    assert WeaponProficiency.SIMPLE_WEAPON in result.weapon_proficiencies


# ---------------------------------------------------------------------------
# Barbarian as first class (positive control)
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_barbarian_first_class_grants_strength_saving_throw() -> None:
    result = BarbarianLevel1(health_increase=_BARB_HEALTH).apply(_EMPTY_BP)
    assert Statistic.STRENGTH in result.saving_throw_proficiencies


@pytest.mark.unit
def test_barbarian_first_class_grants_constitution_saving_throw() -> None:
    result = BarbarianLevel1(health_increase=_BARB_HEALTH).apply(_EMPTY_BP)
    assert Statistic.CONSTITUTION in result.saving_throw_proficiencies


@pytest.mark.unit
def test_barbarian_first_class_grants_skills() -> None:
    result = BarbarianLevel1(health_increase=_BARB_HEALTH).apply(_EMPTY_BP)
    assert len(result.skill_proficiencies) == len(_EMPTY_BP.skill_proficiencies) + 2


@pytest.mark.unit
def test_barbarian_multiclass_no_skills() -> None:
    result = BarbarianLevel1(health_increase=_BARB_HEALTH).apply(_WIZARD_1_BP)
    assert result.skill_proficiencies == _WIZARD_1_BP.skill_proficiencies


# ---------------------------------------------------------------------------
# Rogue multiclass (character already has wizard 1)
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_rogue_multiclass_no_dexterity_saving_throw() -> None:
    result = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_WIZARD_1_BP_WITH_SKILLS)
    assert Statistic.DEXTERITY not in result.saving_throw_proficiencies


@pytest.mark.unit
def test_rogue_multiclass_no_intelligence_saving_throw() -> None:
    result = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_WIZARD_1_BP_WITH_SKILLS)
    assert Statistic.INTELLIGENCE not in result.saving_throw_proficiencies


@pytest.mark.unit
def test_rogue_multiclass_no_skills() -> None:
    result = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_WIZARD_1_BP_WITH_SKILLS)
    assert result.skill_proficiencies == _WIZARD_1_BP_WITH_SKILLS.skill_proficiencies


@pytest.mark.unit
def test_rogue_multiclass_keeps_armor_proficiencies() -> None:
    result = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_WIZARD_1_BP_WITH_SKILLS)
    assert ArmorProficiency.LIGHT_ARMOR in result.armor_proficiencies


@pytest.mark.unit
def test_rogue_multiclass_keeps_weapon_proficiencies() -> None:
    result = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_WIZARD_1_BP_WITH_SKILLS)
    assert WeaponProficiency.RAPIER in result.weapon_proficiencies
    assert WeaponProficiency.SIMPLE_WEAPON in result.weapon_proficiencies


@pytest.mark.unit
def test_rogue_multiclass_still_grants_expertise() -> None:
    result = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_WIZARD_1_BP_WITH_SKILLS)
    assert len(result.skill_expertise) == 2


# ---------------------------------------------------------------------------
# Rogue as first class (positive control)
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_rogue_first_class_grants_dexterity_saving_throw() -> None:
    result = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_EMPTY_BP)
    assert Statistic.DEXTERITY in result.saving_throw_proficiencies


@pytest.mark.unit
def test_rogue_first_class_grants_intelligence_saving_throw() -> None:
    result = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_EMPTY_BP)
    assert Statistic.INTELLIGENCE in result.saving_throw_proficiencies


@pytest.mark.unit
def test_rogue_first_class_grants_skills() -> None:
    result = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_EMPTY_BP)
    assert len(result.skill_proficiencies) == len(_EMPTY_BP.skill_proficiencies) + 4


# ---------------------------------------------------------------------------
# Wizard multiclass (character already has barbarian 1)
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_wizard_multiclass_no_intelligence_saving_throw() -> None:
    result = WizardLevel1(health_increase=_WIZ_HEALTH).apply(_BARB_1_BP)
    assert Statistic.INTELLIGENCE not in result.saving_throw_proficiencies


@pytest.mark.unit
def test_wizard_multiclass_no_wisdom_saving_throw() -> None:
    result = WizardLevel1(health_increase=_WIZ_HEALTH).apply(_BARB_1_BP)
    assert Statistic.WISDOM not in result.saving_throw_proficiencies


@pytest.mark.unit
def test_wizard_multiclass_no_skills() -> None:
    result = WizardLevel1(health_increase=_WIZ_HEALTH).apply(_BARB_1_BP)
    assert result.skill_proficiencies == _BARB_1_BP.skill_proficiencies


@pytest.mark.unit
def test_wizard_multiclass_no_equipment() -> None:
    result = WizardLevel1(health_increase=_WIZ_HEALTH).apply(_BARB_1_BP)
    assert result.equipment_choices == _BARB_1_BP.equipment_choices
    assert "spellbook" not in result.other_equipment


@pytest.mark.unit
def test_wizard_multiclass_keeps_weapon_proficiencies() -> None:
    result = WizardLevel1(health_increase=_WIZ_HEALTH).apply(_BARB_1_BP)
    assert WeaponProficiency.DAGGER in result.weapon_proficiencies
    assert WeaponProficiency.QUARTERSTAFF in result.weapon_proficiencies


# ---------------------------------------------------------------------------
# Wizard as first class (positive control)
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_wizard_first_class_grants_intelligence_saving_throw() -> None:
    result = WizardLevel1(health_increase=_WIZ_HEALTH).apply(_EMPTY_BP)
    assert Statistic.INTELLIGENCE in result.saving_throw_proficiencies


@pytest.mark.unit
def test_wizard_first_class_grants_wisdom_saving_throw() -> None:
    result = WizardLevel1(health_increase=_WIZ_HEALTH).apply(_EMPTY_BP)
    assert Statistic.WISDOM in result.saving_throw_proficiencies


@pytest.mark.unit
def test_wizard_first_class_grants_equipment() -> None:
    result = WizardLevel1(health_increase=_WIZ_HEALTH).apply(_EMPTY_BP)
    assert len(result.equipment_choices) > len(_EMPTY_BP.equipment_choices)
    assert "spellbook" in result.other_equipment


# ---------------------------------------------------------------------------
# Sorcerer multiclass (character already has barbarian 1)
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_sorcerer_multiclass_no_charisma_saving_throw() -> None:
    result = SorcererLevel1DraconicBloodline(health_increase=_SOR_HEALTH).apply(
        _BARB_1_BP
    )
    assert Statistic.CHARISMA not in result.saving_throw_proficiencies


@pytest.mark.unit
def test_sorcerer_multiclass_no_constitution_saving_throw() -> None:
    result = SorcererLevel1DraconicBloodline(health_increase=_SOR_HEALTH).apply(
        _BARB_1_BP
    )
    assert Statistic.CONSTITUTION not in result.saving_throw_proficiencies


@pytest.mark.unit
def test_sorcerer_multiclass_no_skills() -> None:
    result = SorcererLevel1DraconicBloodline(health_increase=_SOR_HEALTH).apply(
        _BARB_1_BP
    )
    assert result.skill_proficiencies == _BARB_1_BP.skill_proficiencies


@pytest.mark.unit
def test_sorcerer_multiclass_no_equipment() -> None:
    result = SorcererLevel1DraconicBloodline(health_increase=_SOR_HEALTH).apply(
        _BARB_1_BP
    )
    assert result.equipment_choices == _BARB_1_BP.equipment_choices


@pytest.mark.unit
def test_sorcerer_multiclass_keeps_weapon_proficiencies() -> None:
    result = SorcererLevel1DraconicBloodline(health_increase=_SOR_HEALTH).apply(
        _BARB_1_BP
    )
    assert WeaponProficiency.DAGGER in result.weapon_proficiencies
