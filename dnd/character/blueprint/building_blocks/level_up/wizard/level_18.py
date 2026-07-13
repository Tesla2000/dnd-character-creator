from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardLevel18UpgradeLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType


class WizardLevel18(
    WizardLevel18UpgradeLevelBase[
        Literal[SecondSubclassPostLevel.SEVENTEENTH],
        Literal[SecondSubclassPostLevel.EIGHTEENTH],
    ]
):
    """Increments wizard to level 18 and transitions to WizardLevel18Blueprint."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_18] = BuildingBlockType.WIZARD_LEVEL_18

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 18}),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.PASSIVE,
                        name="Spell Mastery",
                        description=(
                            "Choose one 1st-level and one 2nd-level wizard spell in your "
                            "spellbook. You can cast those spells at their lowest level "
                            "without expending a spell slot when you have them prepared. "
                            "You can exchange one or both choices during a long rest."
                        ),
                    ),
                ),
            }
        )
