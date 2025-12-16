"""Subclass assignment building blocks.

This package provides building blocks for assigning subclasses to characters,
including both random and AI-powered selection strategies.
"""

from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.ai import (
    AISubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.base import (
    SubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.random import (
    RandomSubclassAssigner,
)

__all__ = [
    "AISubclassAssigner",
    "RandomSubclassAssigner",
    "SubclassAssigner",
]
