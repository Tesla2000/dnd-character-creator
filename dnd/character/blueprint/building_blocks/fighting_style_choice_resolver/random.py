import random
from typing import Literal

from pydantic import ConfigDict
from pydantic import Field

from dnd.character.blueprint.building_blocks.building_block import _WideBlueprint
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.fighting_style_choice_resolver.base import (
    FightingStyleChoiceResolver,
)
from dnd.choices.abilities.fighting_style import FightingStyle


class RandomFightingStyleChoiceResolver(FightingStyleChoiceResolver):
    """Randomly selects a fighting style from the available options.

    Provides deterministic randomness when seed is set, useful for
    reproducible character generation.

    Example:
        >>> resolver = RandomFightingStyleChoiceResolver(seed=42)
    """

    type: Literal[BuildingBlockType.RANDOM_FIGHTING_STYLE_CHOICE_RESOLVER] = (
        BuildingBlockType.RANDOM_FIGHTING_STYLE_CHOICE_RESOLVER
    )

    model_config = ConfigDict(frozen=True)

    seed: int | None = Field(
        default=None,
        description="Optional seed for reproducible random selection",
    )

    def _select_style(self, state: _WideBlueprint) -> FightingStyle:
        random.seed(self.seed)
        return random.choice(sorted(state.fighting_styles_to_choose_from))
