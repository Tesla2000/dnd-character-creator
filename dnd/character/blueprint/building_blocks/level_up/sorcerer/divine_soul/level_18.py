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


class SorcererLevel18DivineSoul(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.SEVENTEENTH],
            Literal[SorcererSubclass.DIVINE_SOUL],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.EIGHTEENTH],
            Literal[SorcererSubclass.DIVINE_SOUL],
        ],
    ]
):
    """Increments sorcerer to level 18 and grants Divine Soul origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_18_DIVINE_SOUL] = (
        BuildingBlockType.SORCERER_LEVEL_18_DIVINE_SOUL
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 18}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Unearthly Recovery",
                        description=(
                            "When you have fewer than half your hit point maximum remaining, "
                            "regain hit points equal to half your hit point maximum. "
                            "Recharge: long rest."
                        ),
                    ),
                ),
            }
        )
