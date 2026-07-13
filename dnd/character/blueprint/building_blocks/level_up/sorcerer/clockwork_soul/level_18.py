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


class SorcererLevel18ClockworkSoul(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.SEVENTEENTH],
            Literal[SorcererSubclass.CLOCKWORK_SOUL],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.EIGHTEENTH],
            Literal[SorcererSubclass.CLOCKWORK_SOUL],
        ],
    ]
):
    """Increments sorcerer to level 18 and grants Clockwork Soul origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_18_CLOCKWORK_SOUL] = (
        BuildingBlockType.SORCERER_LEVEL_18_CLOCKWORK_SOUL
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 18}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Clockwork Cavalcade",
                        description=(
                            "Summon spirits of order in a 30-foot cube: restore up to 100 "
                            "HP among chosen creatures (any distribution), end ongoing spells "
                            "of 3rd level or lower, and repair all damaged objects. Recharge: "
                            "long rest or 7 sorcery points."
                        ),
                    ),
                ),
            }
        )
