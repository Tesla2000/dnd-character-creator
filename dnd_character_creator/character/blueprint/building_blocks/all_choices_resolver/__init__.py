"""All choices resolver package.

Provides two implementations:
- AllChoicesResolver: Chains individual resolvers (composable)
- AIAllChoicesResolver: Makes all choices in single LLM call (holistic)
"""

from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.ai import (
    AIAllChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.base import (
    AllChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.base_resolver import (
    AllChoicesResolverBase,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.choice_package import (
    ChoicePackage,
)

__all__ = [
    "AllChoicesResolver",
    "AIAllChoicesResolver",
    "AllChoicesResolverBase",
    "ChoicePackage",
]
