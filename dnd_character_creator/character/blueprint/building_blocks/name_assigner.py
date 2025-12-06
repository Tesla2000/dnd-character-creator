from __future__ import annotations

from typing import Generator

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint


class NameAssigner(BuildingBlock):
    """Assigns a name to the character."""

    name: str

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Yield the name difference."""
        yield Blueprint(name=self.name)
