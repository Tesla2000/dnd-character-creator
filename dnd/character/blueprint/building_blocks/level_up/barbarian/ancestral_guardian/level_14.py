from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.barbarian.base import (
    BarbarianSubclassFeatureLevelBase,
)
from dnd.character.blueprint.sentinels import ClassSubclassLevel
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.choices.class_creation.character_class import BarbarianSubclass
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType


class BarbarianLevel14AncestralGuardian(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.THIRTEENTH], BarbarianSubclass
        ],
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.FOURTEENTH], BarbarianSubclass
        ],
    ]
):
    """Grants Ancestral Guardian level 14 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_14_ANCESTRAL_GUARDIAN] = (
        BuildingBlockType.BARBARIAN_LEVEL_14_ANCESTRAL_GUARDIAN
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.REACTION,
                        name="Vengeful Ancestors",
                        description=(
                            "At 14th level, your ancestral spirits grow powerful enough to "
                            "retaliate. When you use your Spirit Shield to reduce the damage "
                            "of an attack, the attacker takes an amount of force damage equal "
                            "to the damage that your Spirit Shield prevents."
                        ),
                    ),
                ),
            }
        )
