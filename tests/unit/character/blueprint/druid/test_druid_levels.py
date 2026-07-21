import pytest

from dnd.character._ability_name import AbilityName
from dnd.character._fight_resource import ResourceName
from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    D8HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment import (
    DruidRandomSpellAssigner,
)
from dnd.character.blueprint.building_blocks.level_up.druid.level_1 import DruidLevel1
from dnd.character.blueprint.building_blocks.level_up.druid.level_3 import DruidLevel3
from dnd.character.blueprint.building_blocks.level_up.druid.level_4 import DruidLevel4
from dnd.character.blueprint.building_blocks.level_up.druid.level_5 import DruidLevel5
from dnd.character.blueprint.building_blocks.level_up.druid.level_7 import DruidLevel7
from dnd.character.blueprint.building_blocks.level_up.druid.moon.level_2 import (
    DruidLevel2Moon,
)
from dnd.character.blueprint.building_blocks.level_up.druid.moon.level_6 import (
    DruidLevel6Moon,
)
from dnd.character.blueprint.sentinels import DruidInfo
from dnd.character.blueprint.states._caster_info import CasterInfo
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.race.race import Race
from dnd.character.spells.max_spell_levels import FULL_CASTER_SPELL_SLOTS
from dnd.character.stats import Stats
from dnd.choices.class_creation.character_class import DruidSubclass
from dnd.choices.language import Language

_DRUID_HEALTH = D8HealthIncreaseAverage()
_DRUID_SPELLS = DruidRandomSpellAssigner()

_STATS = Stats(
    strength=10,
    dexterity=14,
    constitution=12,
    intelligence=8,
    wisdom=16,
    charisma=10,
)
_INPUT_BP = Blueprint(race=Race.HUMAN, stats=_STATS, health_base=6)
_DRUID_L1_BP = Blueprint(
    race=Race.HUMAN,
    stats=_STATS,
    health_base=8,
    druid=DruidInfo(),
    caster=CasterInfo(spell_slots=FULL_CASTER_SPELL_SLOTS[0], caster_level=1),
)
_DRUID_BP = Blueprint(
    race=Race.HUMAN,
    stats=_STATS,
    health_base=8,
    druid=DruidInfo(),
    caster=CasterInfo(spell_slots=FULL_CASTER_SPELL_SLOTS[4], caster_level=5),
    subclasses=(DruidSubclass.MOON,),
)


@pytest.mark.unit
def test_druid_level1_apply() -> None:
    block = DruidLevel1(health_increase=_DRUID_HEALTH, spell_assigner=_DRUID_SPELLS)
    result = block.apply(_INPUT_BP)
    assert result is not None
    assert isinstance(result.druid, DruidInfo)
    assert Language.DRUIDIC in result.languages
    assert result.classes.druid == 1


@pytest.mark.unit
def test_druid_level2_moon_apply() -> None:
    block = DruidLevel2Moon(
        health_increase=_DRUID_HEALTH, spell_assigner=_DRUID_SPELLS
    )
    result = block.apply(_DRUID_L1_BP)
    assert result is not None
    assert result.classes.druid == 2
    assert DruidSubclass.MOON in result.subclasses
    assert AbilityName.WILD_SHAPE in result.actions
    wild_shape = next(
        r for r in result.resource_max_uses if r.name == ResourceName.WILD_SHAPE
    )
    assert wild_shape.max_uses == 2


@pytest.mark.unit
@pytest.mark.parametrize(
    "block",
    [
        DruidLevel3(health_increase=_DRUID_HEALTH, spell_assigner=_DRUID_SPELLS),
        DruidLevel4(health_increase=_DRUID_HEALTH, spell_assigner=_DRUID_SPELLS),
        DruidLevel5(health_increase=_DRUID_HEALTH, spell_assigner=_DRUID_SPELLS),
        DruidLevel7(health_increase=_DRUID_HEALTH, spell_assigner=_DRUID_SPELLS),
    ],
)
def test_druid_shared_level_apply(block: BuildingBlock) -> None:
    result = block.apply(_DRUID_BP)
    assert result is not None


@pytest.mark.unit
def test_druid_level6_moon_apply() -> None:
    block = DruidLevel6Moon(
        health_increase=_DRUID_HEALTH, spell_assigner=_DRUID_SPELLS
    )
    result = block.apply(_DRUID_BP)
    assert result is not None
    assert result.classes.druid == 6
    assert AbilityName.PRIMAL_STRIKE in result.actions
