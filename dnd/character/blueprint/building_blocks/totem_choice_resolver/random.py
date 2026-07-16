import random
from typing import Literal

from pydantic import Field

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.totem_choice_resolver.base import (
    TotemChoiceResolverBase,
)
from dnd.choices.abilities.totem_animal import TotemAnimal


class RandomTotemChoiceResolver(TotemChoiceResolverBase):
    type: Literal[BuildingBlockType.RANDOM_TOTEM_CHOICE_RESOLVER] = (
        BuildingBlockType.RANDOM_TOTEM_CHOICE_RESOLVER
    )
    seed: int | None = Field(default=None)

    def resolve(self) -> TotemAnimal:
        random.seed(self.seed)
        return random.choice(list(TotemAnimal))
