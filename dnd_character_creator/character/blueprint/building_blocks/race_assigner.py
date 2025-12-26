from __future__ import annotations

from typing import Self

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.character.race.subrace_stats.subrace_to_stats import (
    SUBRACE_STATS,
)
from dnd_character_creator.character.race.subraces import Subrace
from pydantic import model_validator


class RaceAssigner(BuildingBlock):
    """Assigns a race to the character."""

    race: Race
    subrace: Subrace

    @model_validator(mode="after")
    def _check_subrace_correctness(self) -> Self:
        # TODO: This will need to be implemented
        return self

    def get_change(self, blueprint: Blueprint) -> Blueprint:
        """Returns the race difference."""
        if blueprint.race is not None:
            raise ValueError(
                f"Couldn't assign race {self.race} and subrace {self.subrace} to {blueprint=} already has a race assigned"
            )
        subrace_stats = SUBRACE_STATS[self.subrace].add_to(blueprint)
        return subrace_stats.model_copy(
            update=Blueprint(
                race=self.race,
                subrace=self.subrace,
            ).model_dump(exclude_unset=True)
        )
