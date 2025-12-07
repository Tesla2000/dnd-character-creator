import pytest
from pydantic import ValidationError

from dnd_character_creator.character.blueprint.building_blocks import \
    LevelAssigner, RaceAssigner
from dnd_character_creator.character.blueprint.building_blocks.class_level_up.health_increase import \
    HealthIncreaseAverage
from dnd_character_creator.character.blueprint.building_blocks.class_level_up.level_incrementer import \
    LevelIncrementer
from dnd_character_creator.character.blueprint.building_blocks.class_level_up.level_up import \
    LevelUp
from dnd_character_creator.character.blueprint.building_blocks.class_level_up.spell_assignment import \
    RandomSpellAssigner
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.standar_array import \
    StandardArray
from dnd_character_creator.character.builder import Builder
from dnd_character_creator.character.race.subraces import Subrace
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.choices.stats_creation.statistic import Statistic


@pytest.mark.integration
class TestBuildWizard:
    def test_build_wizard(self):
        builder = Builder().add(
            LevelAssigner(level=16)
        ).add(
            StandardArray(
                stats_priority=(
                    Statistic.INTELLIGENCE,
                    Statistic.CONSTITUTION,
                    Statistic.CHARISMA,
                    Statistic.WISDOM,
                    Statistic.DEXTERITY,
                    Statistic.STRENGTH,
                )
            )
        ).add(
            RaceAssigner(
                race=Race.HUMAN,
                subrace=Subrace.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK,
            )
        ).add(
            LevelUp(
                blocks=(
                    LevelIncrementer(class_=Class.WIZARD),
                    HealthIncreaseAverage(class_=Class.WIZARD),
                    RandomSpellAssigner(class_=Class.WIZARD),
                ),
            )
        )
        with pytest.raises(ValidationError):
            builder.build()

