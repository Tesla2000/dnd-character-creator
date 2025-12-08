from __future__ import annotations

from typing import Generator

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint


class NameAssigner(BuildingBlock):
    """Assigns a name to the character."""

    name: str

    def _get_change(
        self, blueprint: Blueprint
    ) -> Blueprint:
        """Yield the name difference."""
        return Blueprint(name=self.name)
