from __future__ import annotations

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks import (
    BuildingBlock,
)
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.choices.equipment_creation.weapons import WeaponName
from dnd_character_creator.choices.stats_creation.statistic import Statistic
from dnd_character_creator.feats import FeatName
from dnd_character_creator.other_profficiencies import WeaponProficiency
from dnd_character_creator.skill_proficiency import Skill
from frozendict import frozendict


class LevelIncrementer(BuildingBlock):
    class_: Class

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        existing_classes = dict(blueprint.classes)

        # Add one level to the class
        current_class_level = existing_classes.get(self.class_, 0)
        existing_classes[self.class_] = current_class_level + 1

        # Validate total levels don't exceed character level
        total_class_levels = sum(existing_classes.values())
        character_level = blueprint.level or 0

        if total_class_levels > character_level:
            raise ValueError(
                f"Total class levels ({total_class_levels}) would exceed "
                f"character level ({character_level}). "
                f"Set character level first with LevelAssigner."
            )

        if total_class_levels == 1:
            return self._handle_first_class()
        if self._is_ability_score_improvement(existing_classes[self.class_]):
            return Blueprint(
                classes=frozendict(existing_classes),
                feats=blueprint.feats + (FeatName.ANY_OF_YOUR_CHOICE,),
            )
        return Blueprint(
            classes=frozendict(existing_classes),
        )

    def _is_ability_score_improvement(self, class_level: int) -> bool:
        if self.class_ == Class.WIZARD:
            return class_level in (4, 8, 12, 16, 19)
        raise NotImplementedError()

    def _handle_first_class(self) -> Blueprint:
        if self.class_ == Class.WIZARD:
            return Blueprint(
                classes=frozendict({self.class_: 1}),
                weapon_proficiencies=(
                    WeaponProficiency.DAGGER,
                    WeaponProficiency.DART,
                    WeaponProficiency.SLING,
                    WeaponProficiency.QUARTERSTAFF,
                    WeaponProficiency.LIGHT_CROSSBOW,
                ),
                n_skill_choices=2,
                skills_to_choose_from=(
                    Skill.ARCANA,
                    Skill.HISTORY,
                    Skill.INSIGHT,
                    Skill.INVESTIGATION,
                    Skill.MEDICINE,
                    Skill.RELIGION,
                ),
                equipment_choices=(
                    (WeaponName.QUARTERSTAFF, WeaponName.DAGGER),
                    ("component pouch", "arcane focus"),
                    ("scholor's pack", "explarer's pack"),
                ),
                other_equipment=("spellbook",),
                saving_throw_proficiencies=(
                    Statistic.INTELLIGENCE,
                    Statistic.WISDOM,
                ),
            )
        raise NotImplementedError()
