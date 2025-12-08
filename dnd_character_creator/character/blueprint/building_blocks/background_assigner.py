from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.choices.background_creatrion.background import (
    Background,
)


class BackgroundAssigner(BuildingBlock):
    """Assigns a background to the character."""

    background: Background

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Yield the background difference."""
        return Blueprint(background=self.background)
