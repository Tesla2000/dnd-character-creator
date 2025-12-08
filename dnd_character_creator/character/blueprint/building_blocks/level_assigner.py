from __future__ import annotations

from typing import Generator

from pydantic import Field

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint


class LevelAssigner(BuildingBlock):
    """Assigns a level to the character."""

    level: int = Field(ge=1, le=20)

    def _get_change(
        self, blueprint: Blueprint
    ) -> Blueprint:
        """Yield the level difference."""
        return Blueprint(level=self.level)
