from __future__ import annotations

from abc import ABC

from pydantic import ConfigDict

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)


class InitialDataFiller(BuildingBlock, ABC):
    model_config = ConfigDict(frozen=True)
