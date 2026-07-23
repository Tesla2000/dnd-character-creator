from typing import Literal

from pydantic import Field

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.expertise_choice_resolver import (
    AnyExpertiseChoiceResolver,
)
from dnd.character.blueprint.building_blocks.expertise_choice_resolver.random import (
    RandomExpertiseChoiceResolver,
)
from dnd.character.blueprint.building_blocks.level_up.rogue.base import (
    RogueUpgradeLevelBase,
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
from dnd.character._ability_name import AbilityName
from dnd.choices.language import Language
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import ArmorProficiency
from dnd.other_profficiencies import ToolProficiency
from dnd.other_profficiencies import WeaponProficiency
from dnd.skill_proficiency import Skill


class RogueLevel1(
    RogueUpgradeLevelBase[
        ClassPreSubclassLevel[Literal[ThirdSubclassPreLevel.ZEROTH], None],
        ClassPreSubclassLevel[Literal[ThirdSubclassPreLevel.FIRST], None],
    ]
):
    """Increments rogue to level 1 and grants first-level proficiencies and choices."""

    type: Literal[BuildingBlockType.ROGUE_LEVEL_1] = BuildingBlockType.ROGUE_LEVEL_1
    skill_choice_resolver: AnySkillChoiceResolver = Field(
        default_factory=RandomSkillChoiceResolver
    )
    expertise_choice_resolver: AnyExpertiseChoiceResolver = Field(
        default_factory=RandomExpertiseChoiceResolver
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        is_first_class = blueprint.classes.total_level() == 0
        update: dict[str, object] = {
            "classes": blueprint.classes.model_copy(update={"rogue": 1}),
            "armor_proficiencies": blueprint.armor_proficiencies
            | frozenset({ArmorProficiency.LIGHT_ARMOR}),
            "weapon_proficiencies": blueprint.weapon_proficiencies
            | frozenset(
                {
                    WeaponProficiency.SIMPLE_WEAPON,
                    WeaponProficiency.HAND_CROSSBOW,
                    WeaponProficiency.LONGSWORD,
                    WeaponProficiency.RAPIER,
                    WeaponProficiency.SHORTSWORD,
                }
            ),
            "tool_proficiencies": blueprint.tool_proficiencies
            + (ToolProficiency.THIEVES_TOOLS,),
            "languages": blueprint.languages + (Language.THIEVES_CANT,),
            "actions": blueprint.actions + (AbilityName.SNEAK_ATTACK,),
        }
        if is_first_class:
            update["saving_throw_proficiencies"] = (
                blueprint.saving_throw_proficiencies
                + (Statistic.DEXTERITY, Statistic.INTELLIGENCE)
            )
            update["n_skill_choices"] = blueprint.n_skill_choices + 4
            update["skills_to_choose_from"] = frozenset(
                {
                    Skill.ACROBATICS,
                    Skill.ATHLETICS,
                    Skill.DECEPTION,
                    Skill.INSIGHT,
                    Skill.INTIMIDATION,
                    Skill.INVESTIGATION,
                    Skill.PERCEPTION,
                    Skill.PERFORMANCE,
                    Skill.PERSUASION,
                    Skill.SLEIGHT_OF_HAND,
                    Skill.STEALTH,
                }
            )
        result = blueprint.model_copy(update=update)
        if is_first_class:
            result = self.skill_choice_resolver.apply(result)
        result = result.model_copy(
            update={
                "n_expertise_choices": 2,
                "expertise_choices_from": frozenset(result.skill_proficiencies),
            }
        )
        return self.expertise_choice_resolver.apply(result)
