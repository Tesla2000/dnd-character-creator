from __future__ import annotations

import pytest
from frozendict import frozendict

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks import (
    EquipmentAdder,
)
from dnd_character_creator.character.blueprint.building_blocks import FeatAdder
from dnd_character_creator.character.blueprint.building_blocks import (
    LevelAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    LevelUpClass,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    WeaponAdder,
)
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.choices.equipment_creation.weapons import WeaponName
from dnd_character_creator.feats import Feat


class TestFeatAdder:
    """Tests for FeatAdder building block."""

    def test_add_single_feat(self):
        """Test adding a single feat to empty feat list."""
        adder = FeatAdder(feat=Feat.TOUGH)
        blueprint = Blueprint()

        gen = adder.get_change(blueprint)
        diff = next(gen)

        assert diff.feats == (Feat.TOUGH,)

    def test_add_multiple_feats(self):
        """Test adding multiple feats sequentially."""
        blueprint = Blueprint()

        # Add first feat
        adder1 = FeatAdder(feat=Feat.TOUGH)
        gen1 = adder1.get_change(blueprint)
        diff1 = next(gen1)
        blueprint = blueprint.model_copy(
            update=diff1.model_dump(exclude_unset=True)
        )

        # Add second feat
        adder2 = FeatAdder(feat=Feat.ALERT)
        gen2 = adder2.get_change(blueprint)
        diff2 = next(gen2)
        blueprint = blueprint.model_copy(
            update=diff2.model_dump(exclude_unset=True)
        )

        # Add third feat
        adder3 = FeatAdder(feat=Feat.LUCKY)
        gen3 = adder3.get_change(blueprint)
        diff3 = next(gen3)

        assert diff3.feats == (Feat.TOUGH, Feat.ALERT, Feat.LUCKY)

    def test_add_duplicate_feat_raises_error(self):
        """Test that adding a duplicate feat raises ValueError."""
        blueprint = Blueprint(feats=(Feat.TOUGH,))

        adder = FeatAdder(feat=Feat.TOUGH)
        gen = adder.get_change(blueprint)

        with pytest.raises(ValueError, match="already exists"):
            next(gen)

    def test_feat_immutability(self):
        """Test that feats tuple is immutable."""
        blueprint = Blueprint()

        adder = FeatAdder(feat=Feat.ALERT)
        gen = adder.get_change(blueprint)
        diff = next(gen)

        # Should be a tuple
        assert isinstance(diff.feats, tuple)

        # Original blueprint should be unchanged
        assert blueprint.feats == ()

    def test_add_all_common_feats(self):
        """Test adding multiple different feats."""
        feats_to_add = [
            Feat.TOUGH,
            Feat.ALERT,
            Feat.LUCKY,
            Feat.RESILIENT,
            Feat.WAR_CASTER,
        ]

        blueprint = Blueprint()

        for feat in feats_to_add:
            adder = FeatAdder(feat=feat)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.feats == tuple(feats_to_add)
        assert len(blueprint.feats) == 5


class TestWeaponAdder:
    """Tests for WeaponAdder building block."""

    def test_add_single_weapon(self):
        """Test adding a single weapon to empty weapons list."""
        adder = WeaponAdder(weapon=WeaponName.LONGSWORD)
        blueprint = Blueprint()

        gen = adder.get_change(blueprint)
        diff = next(gen)

        assert diff.weapons == (WeaponName.LONGSWORD,)

    def test_add_multiple_weapons(self):
        """Test adding multiple weapons sequentially."""
        blueprint = Blueprint()

        weapons = [
            WeaponName.LONGSWORD,
            WeaponName.SHORTBOW,
            WeaponName.DAGGER,
        ]

        for weapon in weapons:
            adder = WeaponAdder(weapon=weapon)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.weapons == tuple(weapons)

    def test_add_duplicate_weapons_allowed(self):
        """Test that duplicate weapons are allowed."""
        blueprint = Blueprint()

        # Add first dagger
        adder1 = WeaponAdder(weapon=WeaponName.DAGGER)
        gen1 = adder1.get_change(blueprint)
        diff1 = next(gen1)
        blueprint = blueprint.model_copy(
            update=diff1.model_dump(exclude_unset=True)
        )

        # Add second dagger (duplicate)
        adder2 = WeaponAdder(weapon=WeaponName.DAGGER)
        gen2 = adder2.get_change(blueprint)
        diff2 = next(gen2)
        blueprint = blueprint.model_copy(
            update=diff2.model_dump(exclude_unset=True)
        )

        # Add third dagger
        adder3 = WeaponAdder(weapon=WeaponName.DAGGER)
        gen3 = adder3.get_change(blueprint)
        diff3 = next(gen3)

        assert diff3.weapons == (
            WeaponName.DAGGER,
            WeaponName.DAGGER,
            WeaponName.DAGGER,
        )

    def test_weapon_immutability(self):
        """Test that weapons tuple is immutable."""
        blueprint = Blueprint()

        adder = WeaponAdder(weapon=WeaponName.GREATSWORD)
        gen = adder.get_change(blueprint)
        diff = next(gen)

        # Should be a tuple
        assert isinstance(diff.weapons, tuple)

        # Original blueprint should be unchanged
        assert blueprint.weapons == ()

    def test_mixed_weapon_types(self):
        """Test adding various weapon types."""
        blueprint = Blueprint()

        weapons = [
            WeaponName.LONGSWORD,
            WeaponName.DAGGER,
            WeaponName.SHORTBOW,
            WeaponName.DAGGER,  # Duplicate
            WeaponName.GREATSWORD,
        ]

        for weapon in weapons:
            adder = WeaponAdder(weapon=weapon)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.weapons == tuple(weapons)
        assert len(blueprint.weapons) == 5


class TestEquipmentAdder:
    """Tests for EquipmentAdder building block."""

    def test_add_single_item(self):
        """Test adding a single item to empty equipment list."""
        adder = EquipmentAdder(item="Rope, hempen (50 feet)")
        blueprint = Blueprint()

        gen = adder.get_change(blueprint)
        diff = next(gen)

        assert diff.other_equipment == ("Rope, hempen (50 feet)",)

    def test_add_multiple_items(self):
        """Test adding multiple items sequentially."""
        blueprint = Blueprint()

        items = [
            "Torch",
            "Bedroll",
            "Rations (1 day)",
            "Waterskin",
        ]

        for item in items:
            adder = EquipmentAdder(item=item)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.other_equipment == tuple(items)

    def test_add_duplicate_items_allowed(self):
        """Test that duplicate items are allowed."""
        blueprint = Blueprint()

        # Add multiple torches
        for _ in range(3):
            adder = EquipmentAdder(item="Torch")
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.other_equipment == ("Torch", "Torch", "Torch")

    def test_equipment_immutability(self):
        """Test that equipment tuple is immutable."""
        blueprint = Blueprint()

        adder = EquipmentAdder(item="Healing potion")
        gen = adder.get_change(blueprint)
        diff = next(gen)

        # Should be a tuple
        assert isinstance(diff.other_equipment, tuple)

        # Original blueprint should be unchanged
        assert blueprint.other_equipment == ()

    def test_complex_item_names(self):
        """Test adding items with complex names."""
        blueprint = Blueprint()

        items = [
            "Rope, hempen (50 feet)",
            "Potion of healing (2d4+2)",
            "Thieves' tools",
            "Alchemist's supplies",
        ]

        for item in items:
            adder = EquipmentAdder(item=item)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.other_equipment == tuple(items)


class TestClassAssigner:
    """Tests for updated ClassAssigner building block."""

    def test_add_single_class_level(self):
        """Test adding one level to a class."""
        blueprint = Blueprint(level=5)

        adder = LevelUpClass(class_=Class.FIGHTER)
        gen = adder.get_change(blueprint)
        diff = next(gen)

        assert isinstance(diff.classes, frozendict)
        assert diff.classes[Class.FIGHTER] == 1

    def test_add_multiple_levels_same_class(self):
        """Test adding multiple levels to the same class."""
        blueprint = Blueprint(level=10)

        # Add first level
        adder1 = LevelUpClass(class_=Class.FIGHTER)
        gen1 = adder1.get_change(blueprint)
        diff1 = next(gen1)
        blueprint = blueprint.model_copy(
            update=diff1.model_dump(exclude_unset=True)
        )

        # Add second level
        adder2 = LevelUpClass(class_=Class.FIGHTER)
        gen2 = adder2.get_change(blueprint)
        diff2 = next(gen2)
        blueprint = blueprint.model_copy(
            update=diff2.model_dump(exclude_unset=True)
        )

        # Add third level
        adder3 = LevelUpClass(class_=Class.FIGHTER)
        gen3 = adder3.get_change(blueprint)
        diff3 = next(gen3)

        assert diff3.classes[Class.FIGHTER] == 3

    def test_multiclass_character(self):
        """Test creating a multiclass character."""
        blueprint = Blueprint(level=10)

        classes_to_add = [
            (Class.FIGHTER, 5),  # 5 levels
            (Class.WIZARD, 3),  # 3 levels
            (Class.ROGUE, 2),  # 2 levels
        ]

        for class_, levels in classes_to_add:
            for _ in range(levels):
                adder = LevelUpClass(class_=class_)
                gen = adder.get_change(blueprint)
                diff = next(gen)
                blueprint = blueprint.model_copy(
                    update=diff.model_dump(exclude_unset=True)
                )

        assert blueprint.classes[Class.FIGHTER] == 5
        assert blueprint.classes[Class.WIZARD] == 3
        assert blueprint.classes[Class.ROGUE] == 2
        assert sum(blueprint.classes.values()) == 10

    def test_exceeding_character_level_raises_error(self):
        """Test that exceeding character level raises ValueError."""
        blueprint = Blueprint(level=5)

        # Add 5 levels successfully
        for _ in range(5):
            adder = LevelUpClass(class_=Class.FIGHTER)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        # Try to add 6th level (should fail)
        adder = LevelUpClass(class_=Class.FIGHTER)
        gen = adder.get_change(blueprint)

        with pytest.raises(ValueError, match="exceed character level"):
            next(gen)

    def test_class_assignment_without_level_set(self):
        """Test that assigning class without level set raises error."""
        blueprint = Blueprint()  # No level set

        adder = LevelUpClass(class_=Class.WIZARD)
        gen = adder.get_change(blueprint)

        with pytest.raises(ValueError, match="exceed character level"):
            next(gen)

    def test_class_immutability(self):
        """Test that classes frozendict is immutable."""
        blueprint = Blueprint(level=5)

        adder = LevelUpClass(class_=Class.PALADIN)
        gen = adder.get_change(blueprint)
        diff = next(gen)

        # Should be frozendict
        assert isinstance(diff.classes, frozendict)

        # Should not be modifiable
        with pytest.raises(TypeError):
            diff.classes[Class.BARBARIAN] = 1

    def test_all_classes(self):
        """Test adding levels to various classes."""
        blueprint = Blueprint(level=20)

        classes = [
            Class.FIGHTER,
            Class.WIZARD,
            Class.ROGUE,
            Class.CLERIC,
            Class.BARBARIAN,
        ]

        for class_ in classes:
            for _ in range(4):  # 4 levels each = 20 total
                adder = LevelUpClass(class_=class_)
                gen = adder.get_change(blueprint)
                diff = next(gen)
                blueprint = blueprint.model_copy(
                    update=diff.model_dump(exclude_unset=True)
                )

        assert len(blueprint.classes) == 5
        assert all(level == 4 for level in blueprint.classes.values())
        assert sum(blueprint.classes.values()) == 20


class TestAdderIntegration:
    """Integration tests combining multiple adders."""

    def test_build_complete_character_equipment(self):
        """Test building a character with all types of adders."""
        blueprint = Blueprint(level=10)

        # Add classes
        for _ in range(5):
            adder = LevelUpClass(class_=Class.FIGHTER)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        # Add feats
        for feat in [Feat.TOUGH, Feat.ALERT, Feat.LUCKY]:
            adder = FeatAdder(feat=feat)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        # Add weapons
        for weapon in [
            WeaponName.LONGSWORD,
            WeaponName.SHORTBOW,
            WeaponName.DAGGER,
        ]:
            adder = WeaponAdder(weapon=weapon)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        # Add equipment
        for item in ["Rope, hempen (50 feet)", "Torch", "Bedroll"]:
            adder = EquipmentAdder(item=item)
            gen = adder.get_change(blueprint)
            diff = next(gen)
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        # Verify all additions
        assert blueprint.classes[Class.FIGHTER] == 5
        assert blueprint.feats == (Feat.TOUGH, Feat.ALERT, Feat.LUCKY)
        assert blueprint.weapons == (
            WeaponName.LONGSWORD,
            WeaponName.SHORTBOW,
            WeaponName.DAGGER,
        )
        assert blueprint.other_equipment == (
            "Rope, hempen (50 feet)",
            "Torch",
            "Bedroll",
        )

    def test_order_matters_for_class_assignment(self):
        """Test that LevelAssigner must come before ClassAssigner."""
        blueprint = Blueprint()

        # Try to add class before setting level
        adder = LevelUpClass(class_=Class.WIZARD)
        gen = adder.get_change(blueprint)

        with pytest.raises(ValueError):
            next(gen)

        # Now set level first
        level_adder = LevelAssigner(level=5)
        level_gen = level_adder.get_change(blueprint)
        level_diff = next(level_gen)
        blueprint = blueprint.model_copy(
            update=level_diff.model_dump(exclude_unset=True)
        )

        # Now class assignment should work
        adder = LevelUpClass(class_=Class.WIZARD)
        gen = adder.get_change(blueprint)
        diff = next(gen)

        assert diff.classes[Class.WIZARD] == 1
