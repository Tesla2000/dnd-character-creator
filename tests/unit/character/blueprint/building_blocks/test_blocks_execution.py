import pytest
from pydantic import ValidationError

from dnd.character.blueprint.building_blocks.initial_data_filler.random_filler import (
    RandomInitialDataFiller,
)
from dnd.character.blueprint.building_blocks.equipment_adder import EquipmentAdder
from dnd.character.blueprint.building_blocks.feat_adder import FeatAdder
from dnd.character.blueprint.building_blocks.feat_block.feats import (
    SimpleFeatBlock,
    ToughFeatBlock,
)
from dnd.character.blueprint.building_blocks.magical_item_adder import (
    MagicalItemAdder,
)
from dnd.character.blueprint.building_blocks.magical_item_chooser.random import (
    RandomMagicalItemChooser,
)
from dnd.character.blueprint.building_blocks.null_block import NullBlock
from dnd.character.blueprint.building_blocks.stats_priority import StatsPriority
from dnd.character.blueprint.building_blocks.weapon_adder import WeaponAdder
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.ac_modifier import FlatAcModifier
from dnd.character.feature.feats import FeatName
from dnd.character.spell_attack_bonus_modifier import FlatSpellAttackBonus
from dnd.character.spell_save_dc_modifier import FlatSpellSaveDcBonus
from dnd.character.health_modifier import ToughHealthModifier
from dnd.character.stats import Stats
from dnd.choices.equipment_creation.weapons import WeaponName
from dnd.choices.stats_creation.statistic import Statistic


_PRIORITY: StatsPriority = (
    Statistic.STRENGTH,
    Statistic.DEXTERITY,
    Statistic.CONSTITUTION,
    Statistic.INTELLIGENCE,
    Statistic.WISDOM,
    Statistic.CHARISMA,
)


@pytest.mark.unit
class TestSimpleBlocks:
    def test_random_initial_data_filler_apply(self) -> None:
        block = RandomInitialDataFiller(seed=42)
        result = block.apply(Blueprint())
        assert result.character_data is not None
        assert result.character_data.name is not None
        assert result.character_data.sex is not None

    def test_null_block_apply(self) -> None:
        block = NullBlock()
        result = block.apply(Blueprint())
        assert result is not None

    def test_null_block_apply_returns_same_state(self) -> None:
        block = NullBlock()
        state = Blueprint()
        result = block.apply(state)
        assert dict(result) == dict(state)


@pytest.mark.unit
class TestEquipmentBlocks:
    def test_weapon_adder_apply(self) -> None:
        block = WeaponAdder(weapon=WeaponName.DAGGER)
        result = block.apply(Blueprint())
        assert result is not None

    def test_equipment_adder_apply(self) -> None:
        block = EquipmentAdder(item="Rope (50 feet)")
        result = block.apply(Blueprint())
        assert result is not None

    def test_feat_adder_apply(self) -> None:
        block = FeatAdder(feat=FeatName.ALERT)
        result = block.apply(Blueprint())
        assert result is not None

    def test_feat_adder_duplicate_feat_is_noop(self) -> None:
        state_with_feat = FeatAdder(feat=FeatName.ALERT).apply(Blueprint())
        result = FeatAdder(feat=FeatName.ALERT).apply(state_with_feat)
        assert result.feats == state_with_feat.feats

    def test_tough_feat_block_adds_health_modifier(self) -> None:
        stats = Stats(
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )
        result = ToughFeatBlock().apply(Blueprint(stats=stats))
        assert FeatName.TOUGH in result.feats
        assert len(result.health_modifiers) == 1
        assert isinstance(result.health_modifiers[0], ToughHealthModifier)


@pytest.mark.unit
class TestSimpleFeatBlockSubclasses:
    def test_every_simple_feat_block_adds_its_feat_name(self) -> None:
        subclasses: tuple[type[SimpleFeatBlock], ...] = tuple(
            SimpleFeatBlock.__subclasses__()
        )
        assert len(subclasses) > 0
        for block_cls in subclasses:
            block = block_cls()
            result = block.apply(Blueprint())
            assert block._feat_name() in result.feats


@pytest.mark.unit
class TestRandomMagicalItemChooser:
    def test_no_items_returns_empty(self) -> None:
        block = RandomMagicalItemChooser()
        result = block.apply(Blueprint())
        assert result is not None

    def test_select_uncommon_item(self) -> None:
        block = RandomMagicalItemChooser(n_uncommon=1, seed=42)
        result = block.apply(Blueprint())
        assert result is not None


@pytest.mark.unit
class TestMagicalItemAdder:
    def test_cloak_of_protection_adds_ac_and_saving_throw_bonus(self) -> None:
        result = MagicalItemAdder(item_name="Cloak of Protection").apply(Blueprint())
        assert [m.amount for m in result.ac_modifiers if isinstance(m, FlatAcModifier)] == [1]
        assert result.saving_throw_bonuses == Stats(
            strength=1,
            dexterity=1,
            constitution=1,
            intelligence=1,
            wisdom=1,
            charisma=1,
        )
        assert [i.name for i in result.magical_items] == ["Cloak of Protection"]

    def test_arcane_grimoire_adds_spell_save_dc_bonus(self) -> None:
        result = MagicalItemAdder(item_name="Arcane Grimoire (+1)").apply(Blueprint())
        assert result.spell_save_dc_modifiers == (FlatSpellSaveDcBonus(bonus=1),)
        assert result.spell_attack_bonus_modifiers == (FlatSpellAttackBonus(bonus=1),)

    def test_plain_item_is_only_stored(self) -> None:
        base = Blueprint()
        result = MagicalItemAdder(item_name="Bag of Holding").apply(base)
        assert result.ac_modifiers == base.ac_modifiers
        assert result.spell_save_dc_modifiers == base.spell_save_dc_modifiers
        assert result.saving_throw_bonuses == base.saving_throw_bonuses
        assert result.spell_attack_bonus_modifiers == base.spell_attack_bonus_modifiers
        assert [i.name for i in result.magical_items] == ["Bag of Holding"]

    def test_unknown_item_name_raises(self) -> None:
        with pytest.raises(ValidationError):
            MagicalItemAdder(item_name="Cloak of Nonsense")
