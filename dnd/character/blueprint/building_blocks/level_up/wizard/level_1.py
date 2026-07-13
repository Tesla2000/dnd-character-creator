from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.base import (
    WizardUpgradeLevelBase,
)
from dnd.character.blueprint.sentinels import SecondSubclassPreLevel
from dnd.character.blueprint.sentinels import WizardPreSubclassLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.abilities.action import BasicAction
from dnd.choices.abilities.action_type import ActionType
from dnd.choices.equipment_creation.weapons import WeaponName
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import WeaponProficiency
from dnd.skill_proficiency import Skill


class WizardLevel1(
    WizardUpgradeLevelBase[
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.ZEROTH], None],
        WizardPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
    ]
):
    """Increments wizard to level 1 and grants first-level proficiencies and choices."""

    type: Literal[BuildingBlockType.WIZARD_LEVEL_1] = BuildingBlockType.WIZARD_LEVEL_1

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"wizard": 1}),
                "weapon_proficiencies": blueprint.weapon_proficiencies
                | frozenset(
                    {
                        WeaponProficiency.DAGGER,
                        WeaponProficiency.DART,
                        WeaponProficiency.SLING,
                        WeaponProficiency.QUARTERSTAFF,
                        WeaponProficiency.LIGHT_CROSSBOW,
                    }
                ),
                "n_skill_choices": blueprint.n_skill_choices + 2,
                "skills_to_choose_from": frozenset(
                    {
                        Skill.ARCANA,
                        Skill.HISTORY,
                        Skill.INSIGHT,
                        Skill.INVESTIGATION,
                        Skill.MEDICINE,
                        Skill.RELIGION,
                    }
                ),
                "saving_throw_proficiencies": blueprint.saving_throw_proficiencies
                + (Statistic.INTELLIGENCE, Statistic.WISDOM),
                "equipment_choices": blueprint.equipment_choices
                + (
                    (WeaponName.QUARTERSTAFF, WeaponName.DAGGER),
                    ("component pouch", "arcane focus"),
                    ("scholar's pack", "explorer's pack"),
                ),
                "other_equipment": blueprint.other_equipment + ("spellbook",),
                "actions": blueprint.actions
                + (
                    BasicAction(
                        action_type=ActionType.FREE_ACTION,
                        name="Arcane Recovery",
                        description=(
                            "Once per day when you finish a short rest, you can choose "
                            "expended spell slots to recover. The slots can have a combined "
                            "level equal to or less than half your wizard level (rounded up), "
                            "and none can be 6th level or higher."
                        ),
                    ),
                ),
            }
        )
