from __future__ import annotations

from typing import Generator

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.choices.race_creation.main_race import Race


class RaceAssigner(BuildingBlock):
    """Assigns a race to the character."""

    race: Race

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Yield the race difference."""
        yield Blueprint(race=self.race)
