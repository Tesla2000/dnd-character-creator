from __future__ import annotations

import pytest

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks import (
    AgeAssigner,
    AlignmentAssigner,
    BackgroundAssigner,
    CombinedBlock,
    LevelAssigner,
    NameAssigner,
    RaceAssigner,
    SexAssigner,
)
from dnd_character_creator.choices.alignment import Alignment
from dnd_character_creator.choices.background_creatrion.background import (
    Background,
)
from dnd_character_creator.choices.race_creation.main_race import Race
from dnd_character_creator.choices.sex import Sex


class TestCombinedBlock:
    """Tests for CombinedBlock composition."""

    def test_combined_block_sequential_application(self):
        """Test that CombinedBlock applies blocks sequentially."""
        combined = CombinedBlock(
            blocks=(
                NameAssigner(name="Gandalf"),
                RaceAssigner(race=Race.HUMAN),
                LevelAssigner(level=20),
            )
        )

        blueprint = Blueprint()
        gen = combined.get_change(blueprint)

        # Get all differences
        diffs = []
        try:
            diff = next(gen)
            while True:
                diffs.append(diff)
                diff = gen.send(blueprint)
        except StopIteration:
            pass

        # Should yield 3 differences (one per block)
        assert len(diffs) == 3
        assert diffs[0].name == "Gandalf"
        assert diffs[1].race == Race.HUMAN
        assert diffs[2].level == 20

    def test_combined_block_via_add_operator(self):
        """Test combining blocks using + operator."""
        combined = NameAssigner(name="Aragorn") + RaceAssigner(race=Race.HUMAN)

        assert isinstance(combined, CombinedBlock)
        assert len(combined.blocks) == 2

        blueprint = Blueprint()
        gen = combined.get_change(blueprint)

        diffs = []
        try:
            diff = next(gen)
            while True:
                diffs.append(diff)
                diff = gen.send(blueprint)
        except StopIteration:
            pass

        assert len(diffs) == 2
        assert diffs[0].name == "Aragorn"
        assert diffs[1].race == Race.HUMAN

    def test_combined_block_chained_addition(self):
        """Test chaining multiple blocks with + operator."""
        combined = (
            NameAssigner(name="Legolas")
            + RaceAssigner(race=Race.ELF)
            + LevelAssigner(level=15)
        )

        assert isinstance(combined, CombinedBlock)
        # Should have 3 blocks total (nested CombinedBlocks get flattened logic-wise)
        blueprint = Blueprint()
        gen = combined.get_change(blueprint)

        diffs = []
        try:
            diff = next(gen)
            while True:
                diffs.append(diff)
                diff = gen.send(blueprint)
        except StopIteration:
            pass

        assert len(diffs) == 3
        assert diffs[0].name == "Legolas"
        assert diffs[1].race == Race.ELF
        assert diffs[2].level == 15

    def test_combined_block_all_core_parameters(self):
        """Test combining all core parameter assigners."""
        combined = CombinedBlock(
            blocks=(
                NameAssigner(name="Gimli"),
                SexAssigner(sex=Sex.MALE),
                AgeAssigner(age=140),
                RaceAssigner(race=Race.DWARF),
                BackgroundAssigner(background=Background.SOLDIER),
                AlignmentAssigner(alignment=Alignment.LAWFUL_GOOD),
                LevelAssigner(level=10),
            )
        )

        blueprint = Blueprint()
        gen = combined.get_change(blueprint)

        diffs = []
        try:
            diff = next(gen)
            while True:
                diffs.append(diff)
                diff = gen.send(blueprint)
        except StopIteration:
            pass

        # Should have 7 differences
        assert len(diffs) == 7
        assert diffs[0].name == "Gimli"
        assert diffs[1].sex == Sex.MALE
        assert diffs[2].age == 140
        assert diffs[3].race == Race.DWARF
        assert diffs[4].background == Background.SOLDIER
        assert diffs[5].alignment == Alignment.LAWFUL_GOOD
        assert diffs[6].level == 10

    def test_combined_block_empty_blocks(self):
        """Test CombinedBlock with no blocks."""
        combined = CombinedBlock(blocks=())

        blueprint = Blueprint()
        gen = combined.get_change(blueprint)

        diffs = []
        try:
            diff = next(gen)
            while True:
                diffs.append(diff)
                diff = gen.send(blueprint)
        except StopIteration:
            pass

        # Should yield no differences
        assert len(diffs) == 0

    def test_combined_block_single_block(self):
        """Test CombinedBlock with a single block."""
        combined = CombinedBlock(blocks=(NameAssigner(name="Solo"),))

        blueprint = Blueprint()
        gen = combined.get_change(blueprint)

        diffs = []
        try:
            diff = next(gen)
            while True:
                diffs.append(diff)
                diff = gen.send(blueprint)
        except StopIteration:
            pass

        assert len(diffs) == 1
        assert diffs[0].name == "Solo"

    def test_combined_block_override_behavior(self):
        """Test that later blocks can override earlier ones."""
        combined = CombinedBlock(
            blocks=(
                NameAssigner(name="First"),
                NameAssigner(name="Second"),
                NameAssigner(name="Third"),
            )
        )

        blueprint = Blueprint()
        gen = combined.get_change(blueprint)

        diffs = []
        try:
            diff = next(gen)
            while True:
                diffs.append(diff)
                diff = gen.send(blueprint)
        except StopIteration:
            pass

        # All three should yield
        assert len(diffs) == 3
        assert diffs[0].name == "First"
        assert diffs[1].name == "Second"
        assert diffs[2].name == "Third"

        # When applied sequentially, last one wins
        final_blueprint = blueprint
        for diff in diffs:
            final_blueprint = final_blueprint.model_copy(
                update=diff.model_dump(exclude_unset=True)
            )

        assert final_blueprint.name == "Third"

    def test_combined_block_immutability(self):
        """Test that CombinedBlock is frozen."""
        combined = CombinedBlock(blocks=(NameAssigner(name="Test"),))

        with pytest.raises(Exception):  # Pydantic raises ValidationError
            combined.blocks = (RaceAssigner(race=Race.ELF),)

    def test_nested_combined_blocks(self):
        """Test combining CombinedBlocks."""
        inner1 = CombinedBlock(
            blocks=(
                NameAssigner(name="Frodo"),
                RaceAssigner(race=Race.HALFLING),
            )
        )

        inner2 = CombinedBlock(
            blocks=(
                LevelAssigner(level=5),
                AlignmentAssigner(alignment=Alignment.NEUTRAL_GOOD),
            )
        )

        outer = CombinedBlock(blocks=(inner1, inner2))

        blueprint = Blueprint()
        gen = outer.get_change(blueprint)

        diffs = []
        try:
            diff = next(gen)
            while True:
                diffs.append(diff)
                diff = gen.send(blueprint)
        except StopIteration:
            pass

        # Should yield 4 differences total
        assert len(diffs) == 4
        assert diffs[0].name == "Frodo"
        assert diffs[1].race == Race.HALFLING
        assert diffs[2].level == 5
        assert diffs[3].alignment == Alignment.NEUTRAL_GOOD
