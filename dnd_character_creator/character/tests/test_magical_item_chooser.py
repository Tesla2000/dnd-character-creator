"""Tests for magical item chooser building blocks."""

from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.magical_item_chooser import (
    RandomMagicalItemChooser,
)
from dnd_character_creator.character.magical_item.level import Level


class TestRandomMagicalItemChooser:
    """Test RandomMagicalItemChooser functionality."""

    def test_select_single_item(self):
        """Test selecting a single magical item."""
        blueprint = Blueprint()
        chooser = RandomMagicalItemChooser(n_uncommon=1, seed=42)

        diff_gen = chooser.get_change(blueprint)
        diff = next(diff_gen)

        updated_blueprint = blueprint.add_diff(diff)

        assert len(updated_blueprint.magical_items) == 1
        assert updated_blueprint.magical_items[0].level == Level.UNCOMMON

    def test_select_multiple_items_same_rarity(self):
        """Test selecting multiple items of the same rarity."""
        blueprint = Blueprint()
        chooser = RandomMagicalItemChooser(n_rare=3, seed=42)

        diff_gen = chooser.get_change(blueprint)
        diff = next(diff_gen)

        updated_blueprint = blueprint.add_diff(diff)

        assert len(updated_blueprint.magical_items) == 3
        assert all(
            item.level == Level.RARE
            for item in updated_blueprint.magical_items
        )

    def test_select_multiple_rarities(self):
        """Test selecting items across different rarities."""
        blueprint = Blueprint()
        chooser = RandomMagicalItemChooser(
            n_uncommon=2, n_rare=1, n_very_rare=1, seed=42
        )

        diff_gen = chooser.get_change(blueprint)
        diff = next(diff_gen)

        updated_blueprint = blueprint.add_diff(diff)

        assert len(updated_blueprint.magical_items) == 4

        # Count items by rarity
        uncommon_count = sum(
            1
            for item in updated_blueprint.magical_items
            if item.level == Level.UNCOMMON
        )
        rare_count = sum(
            1
            for item in updated_blueprint.magical_items
            if item.level == Level.RARE
        )
        very_rare_count = sum(
            1
            for item in updated_blueprint.magical_items
            if item.level == Level.VERY_RARE
        )

        assert uncommon_count == 2
        assert rare_count == 1
        assert very_rare_count == 1

    def test_no_items_selected(self):
        """Test that no items are added when all counts are 0."""
        blueprint = Blueprint()
        chooser = RandomMagicalItemChooser()

        diff_gen = chooser.get_change(blueprint)
        diff = next(diff_gen)

        updated_blueprint = blueprint.add_diff(diff)

        assert len(updated_blueprint.magical_items) == 0

    def test_seed_determinism(self):
        """Test that same seed produces same results."""
        blueprint = Blueprint()
        chooser1 = RandomMagicalItemChooser(n_uncommon=3, seed=12345)
        chooser2 = RandomMagicalItemChooser(n_uncommon=3, seed=12345)

        # First chooser
        diff_gen1 = chooser1.get_change(blueprint)
        diff1 = next(diff_gen1)
        updated_blueprint1 = blueprint.add_diff(diff1)
        # Second chooser
        diff_gen2 = chooser2.get_change(blueprint)
        diff2 = next(diff_gen2)
        updated_blueprint2 = blueprint.add_diff(diff2)

        # Should select same items in same order
        items1 = [item.name for item in updated_blueprint1.magical_items]
        items2 = [item.name for item in updated_blueprint2.magical_items]

        assert items1 == items2

    def test_duplicates_allowed(self):
        """Test that duplicates can be selected."""
        blueprint = Blueprint()
        # Request more items than available in a rare category to force duplicates
        chooser = RandomMagicalItemChooser(n_legendary=10, seed=42)

        diff_gen = chooser.get_change(blueprint)
        diff = next(diff_gen)

        updated_blueprint = blueprint.add_diff(diff)

        assert len(updated_blueprint.magical_items) == 10
