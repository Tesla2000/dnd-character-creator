from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.choices.sex import Sex
from pydantic import Field


class SexAssigner(BuildingBlock):
    """Assigns a sex to the character."""

    sex: Sex = Field(description="Character's biological sex")

    def get_change(self, blueprint: Blueprint) -> Blueprint:
        """Yield the sex difference."""
        return Blueprint(sex=self.sex)
