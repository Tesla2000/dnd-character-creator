from __future__ import annotations

import json

from dnd_character_creator.choices.background_creatrion.background import (
    Background,
)
from dnd_character_creator.config import Config
from scripts.wiki_scraper import (
    BackgroundTemplate,
)


def background2stats(
    background: Background, config: Config
) -> BackgroundTemplate:
    return BackgroundTemplate(
        **json.loads(
            config.background_root.joinpath(background.value)
            .with_suffix(".json")
            .read_text()
        )
    )
