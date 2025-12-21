from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from pydantic import PositiveInt


class AgeAssigner(BuildingBlock):
    """Assigns an age to the character."""

    age: PositiveInt

    def get_change(self, blueprint: Blueprint) -> Blueprint:
        """Yield the age difference."""
        return Blueprint(age=self.age)
