import random
from typing import Optional

from dnd_character_creator.character.blueprint.building_blocks.race_assigner import (
    BaseRaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.race_assigner.base_race_assigner import (
    RaceSubracePair,
)
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.character.race.subraces import RACE_TO_SUBRACES


class RandomRaceAssigner(BaseRaceAssigner):
    seed: Optional[int] = None

    def _get_race_and_subrace(self) -> RaceSubracePair:
        random.seed(self.seed)

        race = random.choice(tuple(Race))
        subrace = random.choice(RACE_TO_SUBRACES[race])
        return RaceSubracePair(race=race, subrace=subrace)
