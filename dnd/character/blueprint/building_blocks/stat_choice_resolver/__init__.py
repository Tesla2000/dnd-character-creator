from typing import Annotated
from typing import Union

from dnd.character.blueprint.building_blocks.stat_choice_resolver.ai import (
    AIStatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stat_choice_resolver.max import (
    MaxStatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stat_choice_resolver.priority import (
    PriorityStatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stat_choice_resolver.random import (
    RandomStatChoiceResolver,
)
from pydantic import Field

AnyStatChoiceResolver = Annotated[
    Union[
        PriorityStatChoiceResolver,
        RandomStatChoiceResolver,
        MaxStatChoiceResolver,
        AIStatChoiceResolver,
    ],
    Field(discriminator="type"),
]

__all__ = [
    "AIStatChoiceResolver",
    "MaxStatChoiceResolver",
    "PriorityStatChoiceResolver",
    "RandomStatChoiceResolver",
    "AnyStatChoiceResolver",
]
