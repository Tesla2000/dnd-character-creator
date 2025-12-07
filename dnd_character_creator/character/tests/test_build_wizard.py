import pytest
from pydantic import ValidationError

from dnd_character_creator.character.blueprint.building_blocks import \
    LevelAssigner, RaceAssigner, RandomAnyChoiceResolver, \
    PriorityStatChoiceResolver, RandomSkillChoiceResolver
from dnd_character_creator.character.blueprint.building_blocks.class_level_up.health_increase import \
    HealthIncreaseAverage
from dnd_character_creator.character.blueprint.building_blocks.class_level_up.level_incrementer import \
    LevelIncrementer
from dnd_character_creator.character.blueprint.building_blocks.class_level_up.level_up import \
    LevelUp
from dnd_character_creator.character.blueprint.building_blocks.class_level_up.spell_assignment import \
    RandomSpellAssigner
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler import \
    RandomInitialDataFiller
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.standar_array import \
    StandardArray
from dnd_character_creator.character.builder import Builder
from dnd_character_creator.character.character import Character
from dnd_character_creator.character.race.subraces import Subrace
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.character.race.race import Race
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
        builder = Builder().add(
            LevelAssigner(level=16)
        ).add(
            StandardArray(
                stats_priority=stats_priority
            )
        ).add(
            RaceAssigner(
                race=Race.HUMAN,
                subrace=Subrace.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK,
            )
        ).add(
            RandomAnyChoiceResolver(),
        ).add(
            PriorityStatChoiceResolver(priority=stats_priority),
        ).add(
            RandomSkillChoiceResolver(),
        ).add(
            RandomInitialDataFiller(),
        ).add(
            LevelUp(
                blocks=(
                    LevelIncrementer(class_=Class.WIZARD),
                    HealthIncreaseAverage(class_=Class.WIZARD),
                    RandomSpellAssigner(class_=Class.WIZARD),
                ),
            )
        )
        wizard = builder.build()
        assert isinstance(wizard, Character)

