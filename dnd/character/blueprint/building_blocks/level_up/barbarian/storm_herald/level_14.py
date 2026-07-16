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


class BarbarianLevel14StormHerald(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.THIRTEENTH], BarbarianSubclass
        ],
        ClassSubclassLevel[
            Literal[ThirdSubclassPostLevel.FOURTEENTH], BarbarianSubclass
        ],
    ]
):
    """Grants Storm Herald level 14 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_14_STORM_HERALD] = (
        BuildingBlockType.BARBARIAN_LEVEL_14_STORM_HERALD
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 14}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.REACTION,
                        name="Raging Storm",
                        description=(
                            "At 14th level, the power of the storm you channel grows "
                            "mightier, lashing out at your foes. The effect is based on "
                            "your chosen environment: Desert (when you hit with an attack, "
                            "the target must succeed on a Dexterity saving throw or gain "
                            "vulnerability to fire damage until the start of your next turn), "
                            "Sea (when you hit a creature with an attack, you can use your "
                            "reaction to force it to make a Strength saving throw or be "
                            "knocked prone), Tundra (whenever the effect of your Storm Aura "
                            "is activated, you can choose one creature you can see in the "
                            "aura. That creature must succeed on a Strength saving throw or "
                            "be restrained until the start of your next turn)."
                        ),
                    ),
                ),
            }
        )
