from __future__ import annotations

from typing import Annotated
from typing import Union

from dnd.character.blueprint.building_blocks.get_discriminator import (
    get_discriminator,
)
from dnd.character.blueprint.building_blocks.tool_proficiency_choice_resolver.ai import (
    AIToolProficiencyChoiceResolver,
)
from dnd.character.blueprint.building_blocks.tool_proficiency_choice_resolver.random import (
    RandomToolProficiencyChoiceResolver,
)
from dnd.character.blueprint.state import HasToolProficiencies
from pydantic import Tag

AnyToolProficiencyChoiceResolver = Annotated[
    Union[
        Annotated[
            RandomToolProficiencyChoiceResolver[HasToolProficiencies],
            Tag(RandomToolProficiencyChoiceResolver.get_block_type()),
        ],
        Annotated[
            AIToolProficiencyChoiceResolver[HasToolProficiencies],
            Tag(AIToolProficiencyChoiceResolver.get_block_type()),
        ],
    ],
    get_discriminator(),
]

__all__ = [
    "RandomToolProficiencyChoiceResolver",
    "AIToolProficiencyChoiceResolver",
    "AnyToolProficiencyChoiceResolver",
]
