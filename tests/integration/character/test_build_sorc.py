from __future__ import annotations

import sys


import pytest
from dnd.character.blueprint.building_blocks import (
    LevelAssigner,
)
from dnd.character.blueprint.building_blocks import (
    PriorityStatChoiceResolver,
)
from dnd.character.blueprint.building_blocks import (
    RaceAssigner,
)
from dnd.character.blueprint.building_blocks import (
    RandomFeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks import (
    RandomLanguageChoiceResolver,
)
from dnd.character.blueprint.building_blocks import (
    RandomMagicalItemChooser,
)
from dnd.character.blueprint.building_blocks import (
    RandomSkillChoiceResolver,
)
from dnd.character.blueprint.building_blocks import (
    RandomToolProficiencyChoiceResolver,
)
from dnd.character.blueprint.building_blocks.all_choices_resolver import (
    AllChoicesResolver,
)
from dnd.character.blueprint.building_blocks.all_choices_resolver.base_resolver import (
    AllChoicesResolverBase,
)
from dnd.character.blueprint.building_blocks.equipment_chooser.random import (
    RandomEquipmentChooser,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.max_first import (
    MaxFirstResolver,
)
from dnd.character.blueprint.building_blocks.initial_builder import (
    InitialBuilder,
)
from dnd.character.blueprint.building_blocks.initial_data_filler import (
    RandomInitialDataFiller,
)
from dnd.character.blueprint.building_blocks.initial_data_filler.base_filler import (
    InitialDataFiller,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.level_incrementer import (
    SorcererLevelIncrementer,
)
from dnd.character.blueprint.building_blocks.level_up.level_up import (
    LevelUp,
)
from dnd.character.blueprint.building_blocks.level_up.level_up_multiple import (
    LevelUpMultiple,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment import (
    SorcererRandomSpellAssigner,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment.base import (
    SorcererSpellAssigner,
)
from dnd.character.blueprint.building_blocks.magical_item_chooser.base_chooser import (
    MagicalItemChooserBase,
)
from dnd.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd.character.blueprint.building_blocks.subclass_assigner import (
    RandomSubclassAssigner,
)
from dnd.character.blueprint.building_blocks.subclass_assigner.base import (
    SubclassAssigner,
)
from dnd.character.blueprint.state import Blueprint
from dnd.character.character import Character
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.race.race import Race
from dnd.character.race.subraces import SubraceName
from dnd.choices.class_creation.character_class import Class
from dnd.choices.class_creation.character_class import (
    SorcererSubclass,
)
from dnd.choices.stats_creation.statistic import Statistic

SpellAssigner = SorcererSpellAssigner


@pytest.mark.integration
class TestBuildSorcerer:
    STATS_PRIORITY = (
        Statistic.CHARISMA,
        Statistic.CONSTITUTION,
        Statistic.WISDOM,
        Statistic.DEXTERITY,
        Statistic.INTELLIGENCE,
        Statistic.STRENGTH,
    )
    LEVEL = 16
    RACE = Race.HUMAN
    SUBRACE = SubraceName.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK
    CLASS = Class.SORCERER
    SUBCLASSES = (
        SorcererSubclass.DRACONIC_BLOODLINE,
        SorcererSubclass.STORM_SORCERY,
    )

    @classmethod
    def _create_level_up(
        cls,
        all_choices_resolver: AllChoicesResolverBase,
        class_: Class,
        spell_assigner: SpellAssigner,
    ) -> LevelUp:
        return LevelUp(
            level_increment=SorcererLevelIncrementer(),
            health_increase=HealthIncreaseAverage(class_=class_),
            spell_assigner=spell_assigner,
            all_choice_resolver=all_choices_resolver,
        )

    @classmethod
    def _build_sorc(
        cls,
        magical_item_chooser: MagicalItemChooserBase,
        all_choices_resolver: AllChoicesResolverBase,
        initial_data_filler: InitialDataFiller,
        subclass_assigner: SubclassAssigner,
        spell_assigner: SpellAssigner,
    ) -> PresentableCharacter:
        level_up = cls._create_level_up(
            all_choices_resolver,
            class_=cls.CLASS,
            spell_assigner=spell_assigner,
        )
        blueprint = Blueprint()
        blueprint = InitialBuilder(
            level_assigner=LevelAssigner(level=cls.LEVEL),
            stats_builder=StandardArray(stats_priority=cls.STATS_PRIORITY),
            race_assigner=RaceAssigner(
                race=cls.RACE,
                subrace=cls.SUBRACE,
            ),
            all_choices_resolver=all_choices_resolver,
        ).apply(blueprint)
        blueprint = initial_data_filler.apply(blueprint)
        blueprint = LevelUpMultiple(
            blocks=tuple(level_up for _ in range(cls.LEVEL - 1))
        ).apply(blueprint)
        blueprint = subclass_assigner.apply(blueprint)
        blueprint = magical_item_chooser.apply(blueprint)
        return PresentableCharacter.from_blueprint(blueprint)

    def test_build_sorcerer(self) -> None:
        magical_item_chooser = RandomMagicalItemChooser(
            n_uncommon=1,
            n_rare=2,
            n_very_rare=1,
            n_legendary=1,
            seed=42,
        )
        result = self._build_sorc(
            magical_item_chooser,
            AllChoicesResolver(
                language_choice_resolver=RandomLanguageChoiceResolver(),
                skill_choice_resolver=RandomSkillChoiceResolver(),
                feat_choice_resolver=MaxFirstResolver(
                    priority=self.STATS_PRIORITY,
                    then=RandomFeatChoiceResolver(),
                ),
                tool_proficiency_choice_resolver=RandomToolProficiencyChoiceResolver(),
                stat_choice_resolver=PriorityStatChoiceResolver(
                    priority=self.STATS_PRIORITY
                ),
                equipment_chooser=RandomEquipmentChooser(),
            ),
            RandomInitialDataFiller(),
            RandomSubclassAssigner(
                class_=self.CLASS,
                available_subclasses=self.SUBCLASSES,
            ),
            SorcererRandomSpellAssigner(),
        )
        sorcerer = result
        assert isinstance(sorcerer, Character)
        assert sorcerer.weapons
        assert sorcerer.other_equipment
        assert sorcerer.magical_items
        assert len(sorcerer.magical_items) == 5
        sys.stdout.write(
            sorcerer.model_dump_json(
                indent=2,
                exclude_defaults=True,
            )
        )
