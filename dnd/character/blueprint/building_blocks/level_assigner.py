from __future__ import annotations

from typing import Literal

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.state import _BPT
from dnd.character.character import Level as ClassSubclassLevel
from pydantic import Field
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)


class LevelAssigner(BuildingBlock):
    """Assigns a level to the character."""

    type: Literal[BuildingBlockType.LEVEL_ASSIGNER] = BuildingBlockType.LEVEL_ASSIGNER

    level: ClassSubclassLevel = Field(description="The character's total level (1–20)")

    def apply(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(update={"level": self.level})
