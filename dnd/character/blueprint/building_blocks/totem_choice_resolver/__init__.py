from typing import Annotated
from typing import Union

from pydantic import Field

from dnd.character.blueprint.building_blocks.totem_choice_resolver.ai import (
    AITotemChoiceResolver,
)
from dnd.character.blueprint.building_blocks.totem_choice_resolver.base import (
    TotemChoiceResolverBase,
)
from dnd.character.blueprint.building_blocks.totem_choice_resolver.random import (
    RandomTotemChoiceResolver,
)

AnyTotemChoiceResolver = Annotated[
    Union[RandomTotemChoiceResolver, AITotemChoiceResolver],
    Field(discriminator="type"),
]

__all__ = [
    "TotemChoiceResolverBase",
    "RandomTotemChoiceResolver",
    "AITotemChoiceResolver",
    "AnyTotemChoiceResolver",
]
