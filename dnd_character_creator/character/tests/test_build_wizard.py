from __future__ import annotations

import random

import pytest
from dnd_character_creator.character.blueprint.building_blocks import (
    LevelAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    PriorityStatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomAnyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomSkillChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver import (
    AllChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser.random import (
    RandomEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_builder import (
    InitialBuilder,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler import (
    RandomInitialDataFiller,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.health_increase import (
    HealthIncreaseAverage,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.level_incrementer import (
    LevelIncrementer,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.level_up import (
    LevelUp,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.level_up_multiple import (
    LevelUpMultiple,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.spell_assignment import (
    RandomSpellAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.magical_item_assigner import (
    MagicalItemAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.standar_array import (
    StandardArray,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner import (
    RandomSubclassAssigner,
)
from dnd_character_creator.character.builder import Builder
from dnd_character_creator.character.character import Character
from dnd_character_creator.character.magical_item.items import MAGICAL_ITEMS
from dnd_character_creator.character.magical_item.level import Level
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.character.race.subraces import Subrace
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.choices.stats_creation.statistic import Statistic


@pytest.mark.integration
class TestBuildWizard:
    def test_build_wizard(self):
        stats_priority = (
            Statistic.INTELLIGENCE,
            Statistic.CONSTITUTION,
            Statistic.CHARISMA,
            Statistic.WISDOM,
            Statistic.DEXTERITY,
            Statistic.STRENGTH,
        )
        level = 16
        all_choices_resolver = AllChoicesResolver(
            blocks=(
                RandomAnyChoiceResolver(),
                PriorityStatChoiceResolver(priority=stats_priority),
                RandomSkillChoiceResolver(),
                RandomInitialDataFiller(),
                RandomEquipmentChooser(),
            ),
        )
        level_up = LevelUp(
            blocks=(
                LevelIncrementer(class_=Class.WIZARD),
                HealthIncreaseAverage(class_=Class.WIZARD),
                RandomSpellAssigner(class_=Class.WIZARD),
                all_choices_resolver,
            ),
        )

        builder = (
            Builder()
            .add(
                InitialBuilder(
                    blocks=(
                        LevelAssigner(level=level),
                        StandardArray(stats_priority=stats_priority),
                        RaceAssigner(
                            race=Race.HUMAN,
                            subrace=Subrace.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK,
                        ),
                        all_choices_resolver,
                        level_up,
                    )
                )
            )
            .add(
                LevelUpMultiple(
                    blocks=tuple(level_up for _ in range(level - 1))
                )
            )
            .add(RandomSubclassAssigner(class_=Class.WIZARD))
            .add(
                MagicalItemAssigner(
                    magical_item=random.choice(
                        tuple(
                            item
                            for item in MAGICAL_ITEMS
                            if item.level == Level.VERY_RARE
                        )
                    )
                )
            )
            .add(
                MagicalItemAssigner(
                    magical_item=random.choice(
                        tuple(
                            item
                            for item in MAGICAL_ITEMS
                            if item.level == Level.RARE
                        )
                    )
                )
            )
            .add(
                MagicalItemAssigner(
                    magical_item=random.choice(
                        tuple(
                            item
                            for item in MAGICAL_ITEMS
                            if item.level == Level.RARE
                        )
                    )
                )
            )
            .add(
                MagicalItemAssigner(
                    magical_item=random.choice(
                        tuple(
                            item
                            for item in MAGICAL_ITEMS
                            if item.level == Level.LEGENDARY
                        )
                    )
                )
            )
            .add(
                MagicalItemAssigner(
                    magical_item=random.choice(
                        tuple(
                            item
                            for item in MAGICAL_ITEMS
                            if item.level == Level.UNCOMMON
                        )
                    )
                )
            )
        )
        wizard = builder.build()
        assert isinstance(wizard, Character)
        assert wizard.weapons
        assert wizard.other_equipment
        assert wizard.magical_items
        print(
            wizard.model_dump_json(
                indent=2,
                exclude_defaults=True,
            )
        )
