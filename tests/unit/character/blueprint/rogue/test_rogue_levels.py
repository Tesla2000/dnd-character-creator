import pytest

from dnd.character._ability_name import AbilityName
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    D8HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.rogue.level_1 import (
    RogueLevel1,
)
from dnd.character.blueprint.building_blocks.level_up.rogue.level_2 import (
    RogueLevel2,
)
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.race.race import Race
from dnd.character.stats import Stats
from dnd.choices.language import Language
from dnd.other_profficiencies import ArmorProficiency
from dnd.other_profficiencies import ToolProficiency
from dnd.other_profficiencies import WeaponProficiency

_ROGUE_HEALTH = D8HealthIncreaseAverage()

_STATS = Stats(
    strength=10,
    dexterity=16,
    constitution=13,
    intelligence=12,
    wisdom=10,
    charisma=8,
)
_INPUT_BP = Blueprint(race=Race.HUMAN, stats=_STATS, health_base=6)
_ROGUE_L1_BP = RogueLevel1(health_increase=_ROGUE_HEALTH).apply(_INPUT_BP)


@pytest.mark.unit
def test_rogue_level1_apply() -> None:
    result = _ROGUE_L1_BP
    assert result is not None
    assert result.classes.rogue == 1
    assert AbilityName.SNEAK_ATTACK in result.actions
    assert ToolProficiency.THIEVES_TOOLS in result.tool_proficiencies
    assert Language.THIEVES_CANT in result.languages
    assert ArmorProficiency.LIGHT_ARMOR in result.armor_proficiencies
    assert WeaponProficiency.SIMPLE_WEAPON in result.weapon_proficiencies
    assert WeaponProficiency.RAPIER in result.weapon_proficiencies


@pytest.mark.unit
def test_rogue_level1_grants_skills() -> None:
    result = _ROGUE_L1_BP
    assert len(result.skill_proficiencies) == len(_INPUT_BP.skill_proficiencies) + 4


@pytest.mark.unit
def test_rogue_level1_grants_expertise() -> None:
    result = _ROGUE_L1_BP
    assert len(result.skill_expertise) == 2
    assert set(result.skill_expertise) <= set(result.skill_proficiencies)
    assert result.n_expertise_choices == 0
    assert result.expertise_choices_from == frozenset()


@pytest.mark.unit
def test_rogue_level2_apply() -> None:
    block = RogueLevel2(health_increase=_ROGUE_HEALTH)
    result = block.apply(_ROGUE_L1_BP)
    assert result is not None
    assert AbilityName.CUNNING_ACTION in result.actions
    assert result.classes.rogue == 2
