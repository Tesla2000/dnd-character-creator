from __future__ import annotations

from abc import ABC

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from pydantic import ConfigDict


class InitialDataFiller(BuildingBlock, ABC):
    model_config = ConfigDict(frozen=True)
