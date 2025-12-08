from __future__ import annotations

import random
from abc import ABC
from typing import Optional

from pydantic import ConfigDict

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.choices.alignment import Alignment
from dnd_character_creator.choices.background_creatrion.background import Background
from dnd_character_creator.choices.sex import Sex


class InitialDataFiller(BuildingBlock, ABC):
    model_config = ConfigDict(frozen=True)
