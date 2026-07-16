import pytest

from dnd.character.ac_modifier import BarbarianUnarmoredDefenseAcModifier
from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    D12HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_1 import (
    BarbarianLevel1,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_2 import (
    BarbarianLevel2,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_4 import (
    BarbarianLevel4,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_5 import (
    BarbarianLevel5,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_7 import (
    BarbarianLevel7,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_8 import (
    BarbarianLevel8,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_9 import (
    BarbarianLevel9,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_11 import (
    BarbarianLevel11,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_12 import (
    BarbarianLevel12,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_13 import (
    BarbarianLevel13,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_15 import (
    BarbarianLevel15,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_16 import (
    BarbarianLevel16,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_17 import (
    BarbarianLevel17,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_18 import (
    BarbarianLevel18,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_19 import (
    BarbarianLevel19,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.level_20 import (
    BarbarianLevel20,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.ancestral_guardian.level_3 import (
    BarbarianLevel3AncestralGuardian,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.ancestral_guardian.level_6 import (
    BarbarianLevel6AncestralGuardian,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.ancestral_guardian.level_10 import (
    BarbarianLevel10AncestralGuardian,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.ancestral_guardian.level_14 import (
    BarbarianLevel14AncestralGuardian,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.battlerager.level_3 import (
    BarbarianLevel3Battlerager,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.battlerager.level_6 import (
    BarbarianLevel6Battlerager,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.battlerager.level_10 import (
    BarbarianLevel10Battlerager,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.battlerager.level_14 import (
    BarbarianLevel14Battlerager,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.beast.level_3 import (
    BarbarianLevel3Beast,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.beast.level_6 import (
    BarbarianLevel6Beast,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.beast.level_10 import (
    BarbarianLevel10Beast,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.beast.level_14 import (
    BarbarianLevel14Beast,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.berserker.level_3 import (
    BarbarianLevel3Berserker,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.berserker.level_6 import (
    BarbarianLevel6Berserker,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.berserker.level_10 import (
    BarbarianLevel10Berserker,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.berserker.level_14 import (
    BarbarianLevel14Berserker,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.giant.level_3 import (
    BarbarianLevel3Giant,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.giant.level_6 import (
    BarbarianLevel6Giant,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.giant.level_10 import (
    BarbarianLevel10Giant,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.giant.level_14 import (
    BarbarianLevel14Giant,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.storm_herald.level_3 import (
    BarbarianLevel3StormHerald,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.storm_herald.level_6 import (
    BarbarianLevel6StormHerald,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.storm_herald.level_10 import (
    BarbarianLevel10StormHerald,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.storm_herald.level_14 import (
    BarbarianLevel14StormHerald,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.totem_warrior.level_3 import (
    BarbarianLevel3TotemWarrior,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.totem_warrior.level_6 import (
    BarbarianLevel6TotemWarrior,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.totem_warrior.level_10 import (
    BarbarianLevel10TotemWarrior,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.totem_warrior.level_14 import (
    BarbarianLevel14TotemWarrior,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.wild_magic.level_3 import (
    BarbarianLevel3WildMagic,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.wild_magic.level_6 import (
    BarbarianLevel6WildMagic,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.wild_magic.level_10 import (
    BarbarianLevel10WildMagic,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.wild_magic.level_14 import (
    BarbarianLevel14WildMagic,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.zealot.level_3 import (
    BarbarianLevel3Zealot,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.zealot.level_6 import (
    BarbarianLevel6Zealot,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.zealot.level_10 import (
    BarbarianLevel10Zealot,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.zealot.level_14 import (
    BarbarianLevel14Zealot,
)
from dnd.character.blueprint.states.barbarian.base import BarbarianBlueprint
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.race.race import Race
from dnd.character.stats import Stats

_BARB_HEALTH = D12HealthIncreaseAverage()

_STATS = Stats(
    strength=15,
    dexterity=13,
    constitution=14,
    intelligence=8,
    wisdom=12,
    charisma=10,
)
_INPUT_BP = Blueprint(race=Race.HUMAN, stats=_STATS, health_base=6)
_BARB_L1_BP = BarbarianBlueprint(race=Race.HUMAN, stats=_STATS, health_base=12)
_BARB_L2_BP = BarbarianBlueprint(race=Race.HUMAN, stats=_STATS, health_base=19)
_BARB_L3_BP = BarbarianBlueprint(race=Race.HUMAN, stats=_STATS, health_base=26)
_BARB_BP = BarbarianBlueprint(race=Race.HUMAN, stats=_STATS, health_base=60)


@pytest.mark.unit
def test_barbarian_level1_apply() -> None:
    block = BarbarianLevel1(health_increase=_BARB_HEALTH)
    result = block.apply(_INPUT_BP)
    assert result is not None
    assert isinstance(result, BarbarianBlueprint)
    assert any(
        isinstance(m, BarbarianUnarmoredDefenseAcModifier) for m in result.ac_modifiers
    )


@pytest.mark.unit
def test_barbarian_level2_apply() -> None:
    block = BarbarianLevel2(health_increase=_BARB_HEALTH)
    result = block.apply(_BARB_L1_BP)
    assert result is not None
    assert isinstance(result, BarbarianBlueprint)


@pytest.mark.unit
@pytest.mark.parametrize(
    "block",
    [
        BarbarianLevel5(health_increase=_BARB_HEALTH),
        BarbarianLevel7(health_increase=_BARB_HEALTH),
        BarbarianLevel9(health_increase=_BARB_HEALTH),
        BarbarianLevel11(health_increase=_BARB_HEALTH),
        BarbarianLevel13(health_increase=_BARB_HEALTH),
        BarbarianLevel15(health_increase=_BARB_HEALTH),
        BarbarianLevel17(health_increase=_BARB_HEALTH),
        BarbarianLevel18(health_increase=_BARB_HEALTH),
        BarbarianLevel20(health_increase=_BARB_HEALTH),
    ],
)
def test_barbarian_shared_level_apply(block: BuildingBlock) -> None:
    result = block.apply(_BARB_BP)
    assert result is not None


@pytest.mark.unit
@pytest.mark.parametrize(
    "block",
    [
        BarbarianLevel4(health_increase=_BARB_HEALTH),
        BarbarianLevel8(health_increase=_BARB_HEALTH),
        BarbarianLevel12(health_increase=_BARB_HEALTH),
        BarbarianLevel16(health_increase=_BARB_HEALTH),
        BarbarianLevel19(health_increase=_BARB_HEALTH),
    ],
)
def test_barbarian_feat_granting_level_apply(block: BuildingBlock) -> None:
    result = block.apply(_BARB_BP)
    assert result is not None


@pytest.mark.unit
@pytest.mark.parametrize(
    "block",
    [
        BarbarianLevel3AncestralGuardian(health_increase=_BARB_HEALTH),
        BarbarianLevel3Battlerager(health_increase=_BARB_HEALTH),
        BarbarianLevel3Beast(health_increase=_BARB_HEALTH),
        BarbarianLevel3Berserker(health_increase=_BARB_HEALTH),
        BarbarianLevel3Giant(health_increase=_BARB_HEALTH),
        BarbarianLevel3StormHerald(health_increase=_BARB_HEALTH),
        BarbarianLevel3TotemWarrior(health_increase=_BARB_HEALTH),
        BarbarianLevel3WildMagic(health_increase=_BARB_HEALTH),
        BarbarianLevel3Zealot(health_increase=_BARB_HEALTH),
    ],
)
def test_barbarian_level3_subclass_apply(block: BuildingBlock) -> None:
    result = block.apply(_BARB_L2_BP)
    assert result is not None
    assert isinstance(result, BarbarianBlueprint)


@pytest.mark.unit
@pytest.mark.parametrize(
    "block",
    [
        BarbarianLevel6AncestralGuardian(health_increase=_BARB_HEALTH),
        BarbarianLevel10AncestralGuardian(health_increase=_BARB_HEALTH),
        BarbarianLevel14AncestralGuardian(health_increase=_BARB_HEALTH),
        BarbarianLevel6Battlerager(health_increase=_BARB_HEALTH),
        BarbarianLevel10Battlerager(health_increase=_BARB_HEALTH),
        BarbarianLevel14Battlerager(health_increase=_BARB_HEALTH),
        BarbarianLevel6Beast(health_increase=_BARB_HEALTH),
        BarbarianLevel10Beast(health_increase=_BARB_HEALTH),
        BarbarianLevel14Beast(health_increase=_BARB_HEALTH),
        BarbarianLevel6Berserker(health_increase=_BARB_HEALTH),
        BarbarianLevel10Berserker(health_increase=_BARB_HEALTH),
        BarbarianLevel14Berserker(health_increase=_BARB_HEALTH),
        BarbarianLevel6Giant(health_increase=_BARB_HEALTH),
        BarbarianLevel10Giant(health_increase=_BARB_HEALTH),
        BarbarianLevel14Giant(health_increase=_BARB_HEALTH),
        BarbarianLevel6StormHerald(health_increase=_BARB_HEALTH),
        BarbarianLevel10StormHerald(health_increase=_BARB_HEALTH),
        BarbarianLevel14StormHerald(health_increase=_BARB_HEALTH),
        BarbarianLevel6TotemWarrior(health_increase=_BARB_HEALTH),
        BarbarianLevel10TotemWarrior(health_increase=_BARB_HEALTH),
        BarbarianLevel14TotemWarrior(health_increase=_BARB_HEALTH),
        BarbarianLevel6WildMagic(health_increase=_BARB_HEALTH),
        BarbarianLevel10WildMagic(health_increase=_BARB_HEALTH),
        BarbarianLevel14WildMagic(health_increase=_BARB_HEALTH),
        BarbarianLevel6Zealot(health_increase=_BARB_HEALTH),
        BarbarianLevel10Zealot(health_increase=_BARB_HEALTH),
        BarbarianLevel14Zealot(health_increase=_BARB_HEALTH),
    ],
)
def test_barbarian_subclass_feature_level_apply(block: BuildingBlock) -> None:
    result = block.apply(_BARB_BP)
    assert result is not None
