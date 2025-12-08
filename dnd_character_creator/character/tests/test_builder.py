from __future__ import annotations

import pytest
from dnd_character_creator.character.blueprint.building_blocks import (
    AgeAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    AlignmentAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    BackgroundAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    LevelAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    NameAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    SexAssigner,
)
from dnd_character_creator.character.builder import Builder
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.choices.alignment import Alignment
from dnd_character_creator.choices.background_creatrion.background import (
    Background,
)
from dnd_character_creator.choices.sex import Sex
from pydantic import ValidationError


class TestBuilder:
    """Tests for Builder class."""

    def test_builder_empty_blocks(self):
        """Test Builder with no building blocks."""
        builder = Builder([])

        # Should fail validation - missing required fields
        with pytest.raises(ValidationError):
            builder.build()

    def test_builder_single_block(self):
        """Test Builder with a single block."""
        builder = Builder([NameAssigner(name="Test")])

        # Should fail - only has name, missing other required fields
        with pytest.raises(ValidationError):
            builder.build()

    def test_builder_core_parameters_only(self):
        """Test Builder with only core parameter blocks."""
        builder = Builder(
            [
                NameAssigner(name="Thorin"),
                SexAssigner(sex=Sex.MALE),
                AgeAssigner(age=195),
                RaceAssigner(race=Race.DWARF),
                BackgroundAssigner(background=Background.SOLDIER),
                AlignmentAssigner(alignment=Alignment.LAWFUL_GOOD),
                LevelAssigner(level=10),
            ]
        )

        # Should still fail - missing personality fields, appearance, etc.
        with pytest.raises(ValidationError) as exc_info:
            builder.build()

        # Verify it's because of missing required fields
        assert "backstory" in str(exc_info.value) or "Field required" in str(
            exc_info.value
        )

    def test_builder_with_combined_block(self):
        """Test Builder using CombinedBlock."""
        combined = CombinedBlock(
            blocks=(
                NameAssigner(name="Legolas"),
                RaceAssigner(race=Race.ELF),
                LevelAssigner(level=15),
            )
        )

        builder = Builder([combined])

        # Should fail - missing other required fields
        with pytest.raises(ValidationError):
            builder.build()

    def test_builder_with_add_operator_combined(self):
        """Test Builder with blocks combined via + operator."""
        combined = (
            NameAssigner(name="Gimli")
            + RaceAssigner(race=Race.DWARF)
            + LevelAssigner(level=12)
        )

        builder = Builder([combined])

        # Should fail - missing required fields
        with pytest.raises(ValidationError):
            builder.build()

    def test_builder_add_method(self):
        """Test Builder.add() method."""
        builder = (
            Builder()
            .add(NameAssigner(name="Gandalf"))
            .add(RaceAssigner(race=Race.HUMAN))
            .add(LevelAssigner(level=20))
        )

        # Should fail - missing required fields
        with pytest.raises(ValidationError):
            builder.build()

    def test_builder_sequential_application(self):
        """Test that blocks are applied sequentially."""
        builder = Builder(
            [
                NameAssigner(name="First"),
                NameAssigner(name="Second"),
                NameAssigner(name="Third"),
            ]
        )

        # Can't build full character, but we can test the blueprint
        # by accessing internal state
        blueprint = builder._init_character()
        for block in builder._building_blocks:
            for diff in CombinedBlock(blocks=tuple([block])).get_change(
                blueprint
            ):
                blueprint = blueprint.model_copy(
                    update=diff.model_dump(exclude_unset=True)
                )

        # Last value should win
        assert blueprint.name == "Third"

    def test_builder_override_behavior(self):
        """Test that later blocks override earlier ones."""
        builder = Builder(
            [
                RaceAssigner(race=Race.HUMAN),
                RaceAssigner(race=Race.ELF),
                RaceAssigner(race=Race.DWARF),
            ]
        )

        blueprint = builder._init_character()
        for block in builder._building_blocks:
            for diff in CombinedBlock(blocks=tuple([block])).get_change(
                blueprint
            ):
                blueprint = blueprint.model_copy(
                    update=diff.model_dump(exclude_unset=True)
                )

        assert blueprint.race == Race.DWARF

    def test_builder_mixed_blocks_and_combined(self):
        """Test Builder with mix of individual and combined blocks."""
        combined = NameAssigner(name="Frodo") + RaceAssigner(
            race=Race.HALFLING
        )

        builder = Builder(
            [
                combined,
                LevelAssigner(level=5),
                AlignmentAssigner(alignment=Alignment.NEUTRAL_GOOD),
            ]
        )

        blueprint = builder._init_character()
        for block in builder._building_blocks:
            for diff in CombinedBlock(blocks=tuple([block])).get_change(
                blueprint
            ):
                blueprint = blueprint.model_copy(
                    update=diff.model_dump(exclude_unset=True)
                )

        assert blueprint.name == "Frodo"
        assert blueprint.race == Race.HALFLING
        assert blueprint.level == 5
        assert blueprint.alignment == Alignment.NEUTRAL_GOOD

    def test_builder_nested_combined_blocks(self):
        """Test Builder with nested CombinedBlocks."""
        inner1 = CombinedBlock(
            blocks=(
                NameAssigner(name="Samwise"),
                RaceAssigner(race=Race.HALFLING),
            )
        )

        inner2 = CombinedBlock(
            blocks=(
                LevelAssigner(level=3),
                SexAssigner(sex=Sex.MALE),
            )
        )

        outer = CombinedBlock(blocks=(inner1, inner2))

        builder = Builder([outer])

        blueprint = builder._init_character()
        for block in builder._building_blocks:
            for diff in CombinedBlock(blocks=tuple([block])).get_change(
                blueprint
            ):
                blueprint = blueprint.model_copy(
                    update=diff.model_dump(exclude_unset=True)
                )

        assert blueprint.name == "Samwise"
        assert blueprint.race == Race.HALFLING
        assert blueprint.level == 3
        assert blueprint.sex == Sex.MALE

    def test_builder_immutability(self):
        """Test that Builder doesn't mutate the original blueprint."""
        builder = Builder(
            [
                NameAssigner(name="Merry"),
                RaceAssigner(race=Race.HALFLING),
            ]
        )

        original_blueprint = builder._init_character()

        # Apply blocks manually
        final_blueprint = original_blueprint
        for block in builder._building_blocks:
            for diff in CombinedBlock(blocks=tuple([block])).get_change(
                final_blueprint
            ):
                final_blueprint = final_blueprint.model_copy(
                    update=diff.model_dump(exclude_unset=True)
                )

        # Original should be unchanged
        assert original_blueprint.name is None
        assert original_blueprint.race is None

        # Final should be updated
        assert final_blueprint.name == "Merry"
        assert final_blueprint.race == Race.HALFLING

    def test_builder_generator_protocol(self):
        """Test that Builder correctly consumes generators."""

        # Create a custom block that yields multiple times
        class MultiYieldBlock(CombinedBlock):
            def get_change(self, blueprint):
                # First yield
                (
                    yield NameAssigner(name="Step1")
                    .get_change(blueprint)
                    .__next__()
                )
                # Can inspect current state here if needed
                # Second yield
                yield RaceAssigner(race=Race.HUMAN).get_change(
                    blueprint
                ).__next__()

        builder = Builder([MultiYieldBlock(blocks=())])

        blueprint = builder._init_character()
        count = 0
        for block in builder._building_blocks:
            for diff in block.get_change(blueprint):
                blueprint = blueprint.model_copy(
                    update=diff.model_dump(exclude_unset=True)
                )
                count += 1

        assert count == 2
        assert blueprint.name == "Step1"
        assert blueprint.race == Race.HUMAN

    def test_builder_all_blocks_in_sequence(self):
        """Test applying all core parameter blocks in sequence."""
        builder = Builder(
            [
                NameAssigner(name="Boromir"),
                SexAssigner(sex=Sex.MALE),
                AgeAssigner(age=41),
                RaceAssigner(race=Race.HUMAN),
                BackgroundAssigner(background=Background.NOBLE),
                AlignmentAssigner(alignment=Alignment.LAWFUL_NEUTRAL),
                LevelAssigner(level=8),
            ]
        )

        blueprint = builder._init_character()
        for block in builder._building_blocks:
            for diff in CombinedBlock(blocks=tuple([block])).get_change(
                blueprint
            ):
                blueprint = blueprint.model_copy(
                    update=diff.model_dump(exclude_unset=True)
                )

        # Verify all core fields are set
        assert blueprint.name == "Boromir"
        assert blueprint.sex == Sex.MALE
        assert blueprint.age == 41
        assert blueprint.race == Race.HUMAN
        assert blueprint.background == Background.NOBLE
        assert blueprint.alignment == Alignment.LAWFUL_NEUTRAL
        assert blueprint.level == 8

    def test_builder_internal_combined_block_usage(self):
        """Test that Builder internally uses CombinedBlock correctly."""
        builder = Builder(
            [
                NameAssigner(name="Test1"),
                RaceAssigner(race=Race.ELF),
                LevelAssigner(level=5),
            ]
        )

        # The build method creates a CombinedBlock internally
        # Test that it works by checking the blueprint after applying
        blueprint = builder._init_character()

        # This mimics what build() does internally
        for diff in CombinedBlock(
            blocks=tuple(builder._building_blocks)
        ).get_change(blueprint):
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.name == "Test1"
        assert blueprint.race == Race.ELF
        assert blueprint.level == 5


class TestBuilderIntegration:
    """Integration tests for Builder with real usage patterns."""

    def test_builder_typical_usage_pattern(self):
        """Test typical usage: combine AI with manual overrides."""
        # Simulate typical pattern: some manual assignments
        builder = Builder(
            [
                RaceAssigner(race=Race.DWARF),
                LevelAssigner(level=15),
                NameAssigner(name="Dwalin"),
                SexAssigner(sex=Sex.MALE),
                AgeAssigner(age=178),
                BackgroundAssigner(background=Background.SOLDIER),
                AlignmentAssigner(alignment=Alignment.LAWFUL_GOOD),
            ]
        )

        blueprint = builder._init_character()
        for diff in CombinedBlock(
            blocks=tuple(builder._building_blocks)
        ).get_change(blueprint):
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.race == Race.DWARF
        assert blueprint.level == 15
        assert blueprint.name == "Dwalin"

    def test_builder_override_in_sequence(self):
        """Test that you can set a value and then override it."""
        builder = Builder(
            [
                RaceAssigner(race=Race.HUMAN),  # First choice
                NameAssigner(name="Someone"),
                RaceAssigner(race=Race.ELF),  # Changed mind
            ]
        )

        blueprint = builder._init_character()
        for diff in CombinedBlock(
            blocks=tuple(builder._building_blocks)
        ).get_change(blueprint):
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.race == Race.ELF  # Last one wins
        assert blueprint.name == "Someone"

    def test_builder_combined_blocks_override(self):
        """Test override behavior with CombinedBlocks."""
        initial = NameAssigner(name="Original") + RaceAssigner(race=Race.HUMAN)
        override = NameAssigner(name="Changed")

        builder = Builder([initial, override])

        blueprint = builder._init_character()
        for diff in CombinedBlock(
            blocks=tuple(builder._building_blocks)
        ).get_change(blueprint):
            blueprint = blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert blueprint.name == "Changed"
        assert blueprint.race == Race.HUMAN
