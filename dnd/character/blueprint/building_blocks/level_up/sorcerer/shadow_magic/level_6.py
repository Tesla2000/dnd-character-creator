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


class SorcererLevel6ShadowMagic(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.FIFTH],
            Literal[SorcererSubclass.SHADOW_MAGIC],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.SIXTH],
            Literal[SorcererSubclass.SHADOW_MAGIC],
        ],
    ]
):
    """Increments sorcerer to level 6 and grants Shadow Magic origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_6_SHADOW_MAGIC] = (
        BuildingBlockType.SORCERER_LEVEL_6_SHADOW_MAGIC
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 6}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Hound of Ill Omen",
                        description=(
                            "Spend 3 sorcery points to summon a hound of ill omen (dire "
                            "wolf) targeting a creature within 120 feet. The hound can "
                            "move through solid objects and has advantage on attacks against "
                            "the target. Disappears after 5 minutes, upon reducing the "
                            "target to 0 HP, or upon your death."
                        ),
                    ),
                ),
            }
        )
