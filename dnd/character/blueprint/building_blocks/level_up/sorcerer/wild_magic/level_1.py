from typing import Literal

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererLevel1Base,
)
from dnd.character.blueprint.state import _BPT
from dnd.choices.class_creation.character_class import SorcererSubclass
from dnd.choices.equipment_creation.weapons import WeaponName
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import WeaponProficiency
from dnd.skill_proficiency import Skill


class SorcererLevel1WildMagic(SorcererLevel1Base[Literal[SorcererSubclass.WILD_MAGIC]]):
    """Increments sorcerer to level 1 and assigns Wild Magic origin."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_1_WILD_MAGIC] = (
        BuildingBlockType.SORCERER_LEVEL_1_WILD_MAGIC
    )

    def _update_blueprint(self, blueprint: _BPT) -> _BPT:
        return blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 1}),
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
                        Skill.DECEPTION,
                        Skill.INSIGHT,
                        Skill.INTIMIDATION,
                        Skill.PERSUASION,
                        Skill.RELIGION,
                    }
                ),
                "saving_throw_proficiencies": blueprint.saving_throw_proficiencies
                + (Statistic.CHARISMA, Statistic.CONSTITUTION),
                "equipment_choices": blueprint.equipment_choices
                + (
                    (WeaponName.CROSSBOW_LIGHT, WeaponName.DAGGER),
                    ("component pouch", "arcane focus"),
                    ("dungeoneer's pack", "explorer's pack"),
                ),
                "other_equipment": blueprint.other_equipment
                + (WeaponName.DAGGER, WeaponName.DAGGER),
                # TODO: add Wild Magic level-1 origin feature
            }
        )
