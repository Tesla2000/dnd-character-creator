from typing import Literal

from dnd.character._ability_name import AbilityName
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.base import (
    RangerSubclassAssignLevelBase,
)
from dnd.character.blueprint.states.state import _BPT
from dnd.character.spells.spell_slots import WizardFirstLevel
from dnd.choices.class_creation.character_class import RangerSubclass
from dnd.choices.stats_creation.statistic import Statistic


class RangerLevel3GloomStalker(
    RangerSubclassAssignLevelBase[Literal[RangerSubclass.GLOOM_STALKER]]
):
    """Assigns the Gloom Stalker Conclave subclass at level 3."""

    type: Literal[BuildingBlockType.RANGER_LEVEL_3_GLOOM_STALKER] = (
        BuildingBlockType.RANGER_LEVEL_3_GLOOM_STALKER
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"ranger": 3}),
                "subclasses": blueprint.subclasses + (RangerSubclass.GLOOM_STALKER,),
                "actions": blueprint.actions
                + (
                    AbilityName.PRIMEVAL_AWARENESS,
                    AbilityName.DREAD_AMBUSHER,
                    AbilityName.UMBRAL_SIGHT,
                ),
                "initiative_bonus": blueprint.initiative_bonus
                + blueprint.stats.get_modifier(Statistic.WISDOM),
                "spells": blueprint.spells.model_copy(
                    update={
                        "first_level_spells": blueprint.spells.first_level_spells
                        + (WizardFirstLevel.DISGUISE_SELF,)
                    }
                ),
            }
        )
