from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSubclassFeatureLevelBase,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.sentinels import SorcererSubclassLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType
from dnd.choices.class_creation.character_class import SorcererSubclass


class SorcererLevel6DraconicBloodline(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.FIFTH],
            Literal[SorcererSubclass.DRACONIC_BLOODLINE],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.SIXTH],
            Literal[SorcererSubclass.DRACONIC_BLOODLINE],
        ],
    ]
):
    """Increments sorcerer to level 6 and grants Draconic Bloodline origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_6_DRACONIC_BLOODLINE] = (
        BuildingBlockType.SORCERER_LEVEL_6_DRACONIC_BLOODLINE
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Elemental Affinity",
                        description=(
                            "When you cast a spell dealing your dragon ancestor's damage "
                            "type, add your Charisma modifier to the damage. Spend 1 sorcery "
                            "point to gain resistance to that damage type for 1 hour."
                        ),
                    ),
                ),
            }
        )
