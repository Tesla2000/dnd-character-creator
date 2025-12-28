from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.level_up import (
    LevelUp,
)
from pydantic import Field


class LevelUpMultiple(CombinedBlock):
    input_blocks: tuple[LevelUp, ...] = Field(alias="blocks")
