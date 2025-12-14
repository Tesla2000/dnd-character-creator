"""Base class for all magical item choosers."""

from __future__ import annotations

from abc import ABC

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from pydantic import ConfigDict


class MagicalItemChooserBase(BuildingBlock, ABC):
    """Abstract base class for choosers that select magical items.

    Implementations must select magical items based on rarity counts:
    - n_common, n_uncommon, n_rare, etc.

    This base class provides a common type for both random choosers
    (RandomMagicalItemChooser) and holistic AI choosers (AIMagicalItemChooser).

    - RandomMagicalItemChooser: Selects items level-by-level
    - AIMagicalItemChooser: Selects all items in a single holistic LLM call

    Subclasses implement _get_change() to define selection logic.
    """

    model_config = ConfigDict(frozen=True)

    n_common: int = 0
    n_uncommon: int = 0
    n_rare: int = 0
    n_very_rare: int = 0
    n_legendary: int = 0
    n_artifact: int = 0
    n_unique: int = 0
    n_mistery: int = 0
