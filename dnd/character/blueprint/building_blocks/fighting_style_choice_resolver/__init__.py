from dnd.character.blueprint.building_blocks.fighting_style_choice_resolver.base import (
    FightingStyleChoiceResolver,
)
from dnd.character.blueprint.building_blocks.fighting_style_choice_resolver.random import (
    RandomFightingStyleChoiceResolver,
)

AnyFightingStyleChoiceResolver = RandomFightingStyleChoiceResolver

__all__ = [
    "FightingStyleChoiceResolver",
    "RandomFightingStyleChoiceResolver",
    "AnyFightingStyleChoiceResolver",
]
