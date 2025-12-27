from __future__ import annotations

from typing import Annotated
from typing import Union

from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser.ai import (
    AIEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser.random import (
    RandomEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.get_discriminator import (
    get_discriminator,
)
from pydantic import Tag

AnyEquipmentChooser = Annotated[
    Union[
        Annotated[
            RandomEquipmentChooser,
            Tag(RandomEquipmentChooser.get_block_type()),
        ],
        Annotated[
            AIEquipmentChooser,
            Tag(AIEquipmentChooser.get_block_type()),
        ],
    ],
    get_discriminator(),
]

__all__ = [
    "AIEquipmentChooser",
    "RandomEquipmentChooser",
    "AnyEquipmentChooser",
]
