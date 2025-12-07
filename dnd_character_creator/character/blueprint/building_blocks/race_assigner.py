from __future__ import annotations

from typing import Generator, Self

from pydantic import model_validator

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.race.subrace_stats.subrace_to_stats import \
    SUBRACE_STATS
from dnd_character_creator.character.race.subraces import Subrace
from dnd_character_creator.character.race.race import Race


class RaceAssigner(BuildingBlock):
    """Assigns a race to the character."""

    race: Race
    subrace: Subrace

    @model_validator(mode="after")
    def _check_subrace_correctness(self) -> Self:
        # TODO: This will need to be implemented
        return self

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Yield the race difference."""
        # TODO: add stat assigners for all classes and subclasses
        subrace_stats = SUBRACE_STATS[self.subrace].apply(blueprint)
        yield subrace_stats.model_copy(
            update=Blueprint(
                race=self.race,
                subrace=self.subrace,
            ).model_dump(exclude_unset=True)
        )
