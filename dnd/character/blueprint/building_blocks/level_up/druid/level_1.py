from typing import Literal

from pydantic import Field

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.druid.base import (
    DruidUpgradeLevelBase,
)
from dnd.character.blueprint.building_blocks.skill_choice_resolver import (
    AnySkillChoiceResolver,
)
from dnd.character.blueprint.building_blocks.skill_choice_resolver.random import (
    RandomSkillChoiceResolver,
)
from dnd.character.blueprint.sentinels import DruidPreSubclassLevel
from dnd.character.blueprint.sentinels import SecondSubclassPreLevel
from dnd.character.blueprint.states.state import _BPT
from dnd.choices.language import Language
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import ArmorProficiency
from dnd.other_profficiencies import ToolProficiency
from dnd.other_profficiencies import WeaponProficiency
from dnd.skill_proficiency import Skill


class DruidLevel1(
    DruidUpgradeLevelBase[
        DruidPreSubclassLevel[Literal[SecondSubclassPreLevel.FIRST], None],
    ]
):
    """Increments druid to level 1 and grants first-level proficiencies and choices."""

    type: Literal[BuildingBlockType.DRUID_LEVEL_1] = BuildingBlockType.DRUID_LEVEL_1
    skill_choice_resolver: AnySkillChoiceResolver = Field(
        default_factory=RandomSkillChoiceResolver
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        is_first_class = blueprint.classes.total_level() == 0
        update: dict[str, object] = {
            "classes": blueprint.classes.model_copy(update={"druid": 1}),
            "languages": blueprint.languages + (Language.DRUIDIC,),
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
                    WeaponProficiency.CLUB,
                    WeaponProficiency.DAGGER,
                    WeaponProficiency.DART,
                    WeaponProficiency.JAVELIN,
                    WeaponProficiency.MACE,
                    WeaponProficiency.QUARTERSTAFF,
                    WeaponProficiency.SCIMITAR,
                    WeaponProficiency.SICKLE,
                    WeaponProficiency.SLING,
                    WeaponProficiency.SPEAR,
                }
            ),
            "tool_proficiencies": blueprint.tool_proficiencies
            + (ToolProficiency.HERBALISM_KIT,),
        }
        if is_first_class:
            update["n_skill_choices"] = blueprint.n_skill_choices + 2
            update["skills_to_choose_from"] = frozenset(
                {
                    Skill.ARCANA,
                    Skill.ANIMAL_HANDLING,
                    Skill.INSIGHT,
                    Skill.MEDICINE,
                    Skill.NATURE,
                    Skill.PERCEPTION,
                    Skill.RELIGION,
                    Skill.SURVIVAL,
                }
            )
            update["saving_throw_proficiencies"] = (
                blueprint.saving_throw_proficiencies
                + (Statistic.INTELLIGENCE, Statistic.WISDOM)
            )
        result = blueprint.model_copy(update=update)
        return self.skill_choice_resolver.apply(result) if is_first_class else result
