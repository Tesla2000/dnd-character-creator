from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks.race_assigner.base_race_assigner import (
    BaseRaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.race_assigner.base_race_assigner import (
    RaceSubracePair,
)
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.character.race.subraces import Subrace


class RaceAssigner(BaseRaceAssigner):
    """Assigns a race to the character."""

    race: Race
    subrace: Subrace

    def _get_race_and_subrace(self) -> RaceSubracePair:
        return RaceSubracePair(race=self.race, subrace=self.subrace)
