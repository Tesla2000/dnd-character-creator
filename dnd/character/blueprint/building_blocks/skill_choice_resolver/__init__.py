from __future__ import annotations

from typing import Annotated
from typing import Union

from dnd.character.blueprint.building_blocks.get_discriminator import (
    get_discriminator,
)
from dnd.character.blueprint.building_blocks.skill_choice_resolver.ai import (
    AISkillChoiceResolver,
)
from dnd.character.blueprint.building_blocks.skill_choice_resolver.random import (
    RandomSkillChoiceResolver,
)
from dnd.character.blueprint.state import HasNSkillChoices
from dnd.character.blueprint.state import HasSkillProficiencies
from dnd.character.blueprint.state import HasSkillsToChooseFrom
from pydantic import Tag
from typing_protocol_intersection import ProtocolIntersection

AnySkillChoiceResolver = Annotated[
    Union[
        Annotated[
            RandomSkillChoiceResolver[
                ProtocolIntersection[
                    ProtocolIntersection[HasNSkillChoices, HasSkillsToChooseFrom],
                    HasSkillProficiencies,
                ]
            ],
            Tag(RandomSkillChoiceResolver.get_block_type()),
        ],
        Annotated[
            AISkillChoiceResolver[
                ProtocolIntersection[
                    ProtocolIntersection[HasNSkillChoices, HasSkillsToChooseFrom],
                    HasSkillProficiencies,
                ]
            ],
            Tag(AISkillChoiceResolver.get_block_type()),
        ],
    ],
    get_discriminator(),
]

__all__ = [
    "AISkillChoiceResolver",
    "RandomSkillChoiceResolver",
    "AnySkillChoiceResolver",
]
