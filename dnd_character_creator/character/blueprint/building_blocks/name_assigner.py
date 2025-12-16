from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)


class NameAssigner(BuildingBlock):
    """Assigns a name to the character."""

    name: str

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Yield the name difference."""
        return Blueprint(name=self.name)
