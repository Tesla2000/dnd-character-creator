import pytest

from dnd.character._ability_name import AbilityName
from dnd.character.blueprint.building_blocks.fighting_style_choice_resolver.random import (
    RandomFightingStyleChoiceResolver,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    D10HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.level_1 import (
    RangerLevel1,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.level_2 import (
    RangerLevel2,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.level_4 import (
    RangerLevel4,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.level_5 import (
    RangerLevel5,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.gloom_stalker.level_3 import (
    RangerLevel3GloomStalker,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment import (
    RangerRandomSpellAssigner,
)
from dnd.character.blueprint.states._caster_info import CasterInfo
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.race.race import Race
from dnd.character.spells.max_spell_levels import HALF_CASTER_SPELL_SLOTS
from dnd.character.stats import Stats
from dnd.choices.abilities.fighting_style import FightingStyle
from dnd.choices.class_creation.character_class import RangerSubclass

_RANGER_HEALTH = D10HealthIncreaseAverage()
_RANGER_SPELLS = RangerRandomSpellAssigner()
_DEFENSE_RESOLVER = RandomFightingStyleChoiceResolver()

_STATS = Stats(
    strength=10,
    dexterity=16,
    constitution=14,
    intelligence=8,
    wisdom=14,
    charisma=10,
)
_INPUT_BP = Blueprint(race=Race.HUMAN, stats=_STATS, health_base=6)
_RANGER_L1_BP = Blueprint(race=Race.HUMAN, stats=_STATS, health_base=10)
_RANGER_L2_BP = Blueprint(
    race=Race.HUMAN,
    stats=_STATS,
    health_base=10,
    caster=CasterInfo(spell_slots=HALF_CASTER_SPELL_SLOTS[1], caster_level=2),
)
_RANGER_BP = Blueprint(
    race=Race.HUMAN,
    stats=_STATS,
    health_base=10,
    caster=CasterInfo(spell_slots=HALF_CASTER_SPELL_SLOTS[3], caster_level=4),
    subclasses=(RangerSubclass.GLOOM_STALKER,),
)


@pytest.mark.unit
def test_ranger_level1_apply() -> None:
    block = RangerLevel1(health_increase=_RANGER_HEALTH)
    result = block.apply(_INPUT_BP)
    assert result is not None
    assert result.classes.ranger == 1
    assert AbilityName.FAVORED_ENEMY in result.actions
    assert AbilityName.NATURAL_EXPLORER in result.actions
    assert len(result.skill_proficiencies) == 3


@pytest.mark.unit
def test_ranger_level2_apply() -> None:
    block = RangerLevel2(
        health_increase=_RANGER_HEALTH,
        fighting_style_choice_resolver=_DEFENSE_RESOLVER,
        spell_assigner=_RANGER_SPELLS,
    )
    result = block.apply(_RANGER_L1_BP)
    assert result is not None
    assert result.classes.ranger == 2
    assert result.fighting_style in (
        FightingStyle.ARCHERY,
        FightingStyle.DEFENSE,
        FightingStyle.DUELING,
    )
    assert result.caster is not None
    assert result.caster.caster_level == 2
    assert len(result.spells.first_level_spells) == 2


@pytest.mark.unit
def test_ranger_level3_gloom_stalker_apply() -> None:
    block = RangerLevel3GloomStalker(
        health_increase=_RANGER_HEALTH, spell_assigner=_RANGER_SPELLS
    )
    result = block.apply(_RANGER_L2_BP)
    assert result is not None
    assert result.classes.ranger == 3
    assert RangerSubclass.GLOOM_STALKER in result.subclasses
    assert AbilityName.PRIMEVAL_AWARENESS in result.actions
    assert AbilityName.DREAD_AMBUSHER in result.actions
    assert AbilityName.UMBRAL_SIGHT in result.actions
    assert "Disguise Self" in result.spells.first_level_spells
    assert result.caster.caster_level == 3


@pytest.mark.unit
def test_ranger_level4_apply() -> None:
    block = RangerLevel4(health_increase=_RANGER_HEALTH, spell_assigner=_RANGER_SPELLS)
    result = block.apply(_RANGER_BP)
    assert result is not None
    assert result.classes.ranger == 4


@pytest.mark.unit
def test_ranger_level5_apply() -> None:
    block = RangerLevel5(health_increase=_RANGER_HEALTH, spell_assigner=_RANGER_SPELLS)
    result = block.apply(_RANGER_BP)
    assert result is not None
    assert result.classes.ranger == 5
    assert AbilityName.EXTRA_ATTACK in result.actions
    assert result.caster.caster_level == 5
