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


class BarbarianLevel10AncestralGuardian(
    BarbarianSubclassFeatureLevelBase[
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.NINTH], BarbarianSubclass],
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.TENTH], BarbarianSubclass],
    ]
):
    """Grants Ancestral Guardian level 10 subclass feature."""

    type: Literal[BuildingBlockType.BARBARIAN_LEVEL_10_ANCESTRAL_GUARDIAN] = (
        BuildingBlockType.BARBARIAN_LEVEL_10_ANCESTRAL_GUARDIAN
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"barbarian": 10}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.ACTION,
                        name="Consult the Spirits",
                        description=(
                            "At 10th level, you gain the ability to consult with your ancestral "
                            "spirits. When you do so, you cast the augury or clairvoyance spell, "
                            "without using a spell slot or material components. Rather than "
                            "creating a spherical sensor, this use of clairvoyance invisibly "
                            "summons one of your ancestral spirits to the chosen location. "
                            "Wisdom is your spellcasting ability for these spells. After you "
                            "cast either spell in this way, you can't use this feature again "
                            "until you finish a short or long rest."
                        ),
                    ),
                ),
            }
        )
