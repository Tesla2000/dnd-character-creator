import random


from dnd.character.blueprint.building_blocks.expertise_choice_resolver.base import (
    ExpertiseChoiceResolver,
)
from dnd.character.blueprint.building_blocks.building_block import _WideBlueprint
from dnd.skill_proficiency import Skill
from typing import Literal
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from pydantic import ConfigDict
from pydantic import Field


class RandomExpertiseChoiceResolver(ExpertiseChoiceResolver):
    """Randomly selects skills to grant expertise on from available options.

    Provides deterministic randomness when seed is set, useful for
    reproducible character generation.

    Example:
        >>> resolver = RandomExpertiseChoiceResolver(seed=42)  # Reproducible
        >>> # or
        >>> resolver = RandomExpertiseChoiceResolver()  # Truly random
    """

    type: Literal[BuildingBlockType.RANDOM_EXPERTISE_CHOICE_RESOLVER] = (
        BuildingBlockType.RANDOM_EXPERTISE_CHOICE_RESOLVER
    )

    model_config = ConfigDict(frozen=True)

    seed: int | None = Field(
        default=None,
        description="Optional seed for reproducible random selection",
    )

    def _select_expertise(self, state: _WideBlueprint) -> frozenset[Skill]:
        random.seed(self.seed)
        n = state.n_expertise_choices
        available_seq = tuple(state.expertise_choices_from)
        selected = random.sample(available_seq, n)
        return frozenset(selected)
