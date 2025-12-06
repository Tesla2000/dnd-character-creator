from __future__ import annotations

from typing import Generator

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.choices.alignment import Alignment


class AlignmentAssigner(BuildingBlock):
    """Assigns an alignment to the character."""

    alignment: Alignment

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Yield the alignment difference."""
        yield Blueprint(alignment=self.alignment)
