from typing import Annotated
from typing import Union

from dnd.character.blueprint.building_blocks.expertise_choice_resolver.ai import (
    AIExpertiseChoiceResolver,
)
from dnd.character.blueprint.building_blocks.expertise_choice_resolver.random import (
    RandomExpertiseChoiceResolver,
)
from pydantic import Field

AnyExpertiseChoiceResolver = Annotated[
    Union[
        RandomExpertiseChoiceResolver,
        AIExpertiseChoiceResolver,
    ],
    Field(discriminator="type"),
]

__all__ = [
    "AIExpertiseChoiceResolver",
    "RandomExpertiseChoiceResolver",
    "AnyExpertiseChoiceResolver",
]
