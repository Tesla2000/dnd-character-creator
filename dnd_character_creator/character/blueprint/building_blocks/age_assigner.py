from __future__ import annotations

from typing import Generator

from pydantic import PositiveInt

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint


class AgeAssigner(BuildingBlock):
    """Assigns an age to the character."""

    age: PositiveInt

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Yield the age difference."""
        yield Blueprint(age=self.age)
