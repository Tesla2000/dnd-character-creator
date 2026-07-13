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


class SorcererLevel18LunarSorcery(
    SorcererSubclassFeatureLevelBase[
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.SEVENTEENTH],
            Literal[SorcererSubclass.LUNAR_SORCERY],
        ],
        SorcererSubclassLevel[
            Literal[FirstSubclassPostLevel.EIGHTEENTH],
            Literal[SorcererSubclass.LUNAR_SORCERY],
        ],
    ]
):
    """Increments sorcerer to level 18 and grants Lunar Sorcery origin feature."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_18_LUNAR_SORCERY] = (
        BuildingBlockType.SORCERER_LEVEL_18_LUNAR_SORCERY
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 18}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.BONUS_ACTION,
                        name="Lunar Phenomenon",
                        description=(
                            "Evoke your current lunar phase. Full Moon: creatures of your "
                            "choice within 30 feet must make a Constitution save or be "
                            "blinded until your next turn. New Moon: one creature within "
                            "60 feet must make a Dexterity save or take 3d10 necrotic damage "
                            "and be cursed. Crescent Moon: you or a creature within 60 feet "
                            "gains 4d6 temporary HP. Recharge: long rest or 5 sorcery points."
                        ),
                    ),
                ),
            }
        )
