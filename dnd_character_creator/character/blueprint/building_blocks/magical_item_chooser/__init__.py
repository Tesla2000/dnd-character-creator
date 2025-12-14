"""Magical item chooser package.

Provides implementations for selecting magical items:
- RandomMagicalItemChooser: Random level-by-level selection with optional seed
- AIMagicalItemChooser: Holistic AI-powered selection
- MagicalItemChooserBase: Abstract base for all choosers
"""

from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks.magical_item_chooser.ai import (
    AIMagicalItemChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.magical_item_chooser.base_chooser import (
    MagicalItemChooserBase,
)
from dnd_character_creator.character.blueprint.building_blocks.magical_item_chooser.random import (
    RandomMagicalItemChooser,
)

__all__ = [
    "RandomMagicalItemChooser",
    "AIMagicalItemChooser",
    "MagicalItemChooserBase",
]
