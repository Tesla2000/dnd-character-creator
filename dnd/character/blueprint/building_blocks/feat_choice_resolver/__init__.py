from __future__ import annotations

from typing import Annotated
from typing import Union

from dnd.character.blueprint.building_blocks.feat_choice_resolver.ai import (
    AIFeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.max_first import (
    MaxFirstResolver,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.max_if_not_maxed import (
    MaxIfNotMaxedResolver,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.random import (
    RandomFeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.get_discriminator import (
    get_discriminator,
)
from dnd.character.blueprint.state import HasClasses
from dnd.character.blueprint.state import HasFeats
from dnd.character.blueprint.state import HasStats
from dnd.character.blueprint.state import HasStatsCup
from pydantic import Tag
from typing_protocol_intersection import ProtocolIntersection

AnyFeatChoiceResolver = Annotated[
    Union[
        Annotated[
            RandomFeatChoiceResolver[
                ProtocolIntersection[
                    ProtocolIntersection[HasFeats, HasStats], HasClasses
                ]
            ],
            Tag(RandomFeatChoiceResolver.get_block_type()),
        ],
        Annotated[
            AIFeatChoiceResolver[
                ProtocolIntersection[
                    ProtocolIntersection[HasFeats, HasStats], HasClasses
                ]
            ],
            Tag(AIFeatChoiceResolver.get_block_type()),
        ],
        Annotated[
            MaxFirstResolver[
                ProtocolIntersection[
                    ProtocolIntersection[
                        ProtocolIntersection[HasFeats, HasStats], HasClasses
                    ],
                    HasStatsCup,
                ]
            ],
            Tag(MaxFirstResolver.get_block_type()),
        ],
        Annotated[
            MaxIfNotMaxedResolver[
                ProtocolIntersection[
                    ProtocolIntersection[
                        ProtocolIntersection[HasFeats, HasStats], HasClasses
                    ],
                    HasStatsCup,
                ]
            ],
            Tag(MaxIfNotMaxedResolver.get_block_type()),
        ],
    ],
    get_discriminator(),
]

__all__ = [
    "RandomFeatChoiceResolver",
    "AIFeatChoiceResolver",
    "MaxFirstResolver",
    "MaxIfNotMaxedResolver",
    "AnyFeatChoiceResolver",
]
