from __future__ import annotations

from typing import Generator

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.choices.sex import Sex


class SexAssigner(BuildingBlock):
    """Assigns a sex to the character."""

    sex: Sex

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Yield the sex difference."""
        yield Blueprint(sex=self.sex)
