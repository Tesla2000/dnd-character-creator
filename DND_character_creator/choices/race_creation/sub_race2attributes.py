from __future__ import annotations

import json

from DND_character_creator.choices.race_creation.main_race import Race
from DND_character_creator.config import Config
from DND_character_creator.wiki_scraper.MainRaceTemplate import (
    SubRaceTemplate,
)


def sub_race2stats(
    race: Race, sub_race: str, config: Config
) -> SubRaceTemplate:
    return SubRaceTemplate(
        **json.loads(
            next(
                config.sub_races_root.joinpath(race.value).rglob(
                    f"{sub_race}.json"
                )
            ).read_text()
        )
    )
