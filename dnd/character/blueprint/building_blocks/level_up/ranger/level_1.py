from typing import Literal

from pydantic import Field

from dnd.character._ability_name import AbilityName
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.ranger.base import (
    RangerUpgradeLevelBase,
)
from dnd.character.blueprint.building_blocks.skill_choice_resolver import (
    AnySkillChoiceResolver,
)
from dnd.character.blueprint.building_blocks.skill_choice_resolver.random import (
    RandomSkillChoiceResolver,
)
from dnd.character.blueprint.sentinels import ClassPreSubclassLevel
from dnd.character.blueprint.sentinels import ThirdSubclassPreLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import ArmorProficiency
from dnd.other_profficiencies import WeaponProficiency
from dnd.skill_proficiency import Skill


class RangerLevel1(
    RangerUpgradeLevelBase[
        ClassPreSubclassLevel[Literal[ThirdSubclassPreLevel.ZEROTH], None],
        ClassPreSubclassLevel[Literal[ThirdSubclassPreLevel.FIRST], None],
    ]
):
    """Increments ranger to level 1 and grants first-level proficiencies and choices."""

    type: Literal[BuildingBlockType.RANGER_LEVEL_1] = BuildingBlockType.RANGER_LEVEL_1
    skill_choice_resolver: AnySkillChoiceResolver = Field(
        default_factory=RandomSkillChoiceResolver
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        is_first_class = blueprint.classes.total_level() == 0
        update: dict[str, object] = {
            "classes": blueprint.classes.model_copy(update={"ranger": 1}),
            "armor_proficiencies": blueprint.armor_proficiencies
            | frozenset(
                {
                    ArmorProficiency.LIGHT_ARMOR,
                    ArmorProficiency.MEDIUM_ARMOR,
                    ArmorProficiency.SHIELDS,
                }
            ),
            "weapon_proficiencies": blueprint.weapon_proficiencies
            | frozenset(
                {
                    WeaponProficiency.SIMPLE_WEAPON,
                    WeaponProficiency.MARTIAL_WEAPON,
                }
            ),
            "actions": blueprint.actions
            + (AbilityName.FAVORED_ENEMY, AbilityName.NATURAL_EXPLORER),
        }
        if is_first_class:
            update["saving_throw_proficiencies"] = (
                blueprint.saving_throw_proficiencies
                + (Statistic.STRENGTH, Statistic.DEXTERITY)
            )
            update["n_skill_choices"] = blueprint.n_skill_choices + 3
            update["skills_to_choose_from"] = frozenset(
                {
                    Skill.ANIMAL_HANDLING,
                    Skill.ATHLETICS,
                    Skill.INSIGHT,
                    Skill.INVESTIGATION,
                    Skill.NATURE,
                    Skill.PERCEPTION,
                    Skill.STEALTH,
                    Skill.SURVIVAL,
                }
            )
        result = blueprint.model_copy(update=update)
        return self.skill_choice_resolver.apply(result) if is_first_class else result
