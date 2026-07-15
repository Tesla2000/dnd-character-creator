from __future__ import annotations

from typing import Annotated
from typing import Union

from dnd.character.blueprint.building_blocks.feat_block.ability_score_improvement import (
    AbilityScoreImprovementFeatBlock,
)
from dnd.character.blueprint.building_blocks.feat_block.any_feat_selection import (
    AnyFeatSelectionBlock,
)
from pydantic import Field

AnyFeatBlock = Annotated[
    Union[
        AnyFeatSelectionBlock,
        AbilityScoreImprovementFeatBlock,
    ],
    Field(discriminator="type"),
]

__all__ = [
    "AbilityScoreImprovementFeatBlock",
    "AnyFeatBlock",
    "AnyFeatSelectionBlock",
]
