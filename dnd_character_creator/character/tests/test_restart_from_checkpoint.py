from unittest.mock import patch

import pytest
from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks import (
    BuildingBlock,
)
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
    RandomFeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomInitialDataFiller,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomLanguageChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomSkillChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomSkillProficiencyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomToolProficiencyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    SexAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver import (
    AllChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser import (
    RandomEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver.max_first import (
    MaxFirstResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_builder import (
    InitialBuilder,
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
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.standar_array import (
    StandardArray,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner import (
    RandomSubclassAssigner,
)
from dnd_character_creator.character.builder import Builder
from dnd_character_creator.character.checkpoint import IncrementChain
from dnd_character_creator.character.checkpoint import IncrementStorage
from dnd_character_creator.character.checkpoint import MemoryStorage
from dnd_character_creator.character.presentable_character import (
    PresentableCharacter,
)
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.character.race.subraces import Subrace
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.choices.sex import Sex
from dnd_character_creator.choices.stats_creation.statistic import Statistic


class TestRestartFromCheckpoint:
    @pytest.fixture
    def increment_storage(self) -> IncrementStorage:
        return MemoryStorage()

    @pytest.fixture
    def builder(self, increment_storage):
        stats_priority = (
            Statistic.INTELLIGENCE,
            Statistic.CONSTITUTION,
            Statistic.WISDOM,
            Statistic.DEXTERITY,
            Statistic.CHARISMA,
            Statistic.STRENGTH,
        )
        class_ = Class.WIZARD
        all_choices_resolver = AllChoicesResolver(
            blocks=(
                RandomLanguageChoiceResolver(),
                RandomSkillProficiencyChoiceResolver(),
                MaxFirstResolver(
                    priority=stats_priority,
                    then=RandomFeatChoiceResolver(),
                ),
                RandomToolProficiencyChoiceResolver(),
                PriorityStatChoiceResolver(priority=stats_priority),
                RandomSkillChoiceResolver(),
                RandomEquipmentChooser(),
            ),
        )
        spell_assigner = RandomSpellAssigner(class_=class_)
        level_up = LevelUp(
            blocks=(
                LevelIncrementer(class_=class_),
                HealthIncreaseAverage(class_=class_),
                spell_assigner,
                all_choices_resolver,
            ),
        )
        level = 16
        builder = (
            Builder(increment_storage=increment_storage)
            .add(
                InitialBuilder(
                    blocks=(
                        LevelAssigner(level=level),
                        StandardArray(stats_priority=stats_priority),
                        RaceAssigner(
                            race=Race.HUMAN,
                            subrace=Subrace.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK,
                        ),
                        AllChoicesResolver(
                            blocks=(
                                RandomLanguageChoiceResolver(),
                                RandomSkillProficiencyChoiceResolver(),
                                MaxFirstResolver(
                                    priority=stats_priority,
                                    then=RandomFeatChoiceResolver(),
                                ),
                                RandomToolProficiencyChoiceResolver(),
                                PriorityStatChoiceResolver(
                                    priority=stats_priority
                                ),
                                RandomSkillChoiceResolver(),
                                RandomEquipmentChooser(),
                            ),
                        ),
                        level_up,
                    )
                )
            )
            .add(RandomInitialDataFiller())
            .add(
                LevelUpMultiple(
                    blocks=tuple(level_up for _ in range(level - 1))
                )
            )
            .add(
                RandomSubclassAssigner(
                    class_=class_,
                )
            )
        )
        return builder

    def test_restart_from_checkpoint(self, builder, increment_storage):
        result = builder.build()
        increment_chain = increment_storage.load_chain(result.chain_id)
        n_truncated_moves = 10
        truncated_chain = increment_chain.truncate_to(
            increment_chain.length() - n_truncated_moves
        )
        with patch.object(
            IncrementChain,
            IncrementChain.add_increment.__name__,
            wraps=IncrementChain.add_increment,
            autospec=True,
        ) as mock_add_increment:
            result = builder.build(truncated_chain)
            assert isinstance(result.character, PresentableCharacter)
            assert mock_add_increment.call_count == n_truncated_moves

    def test_checkpoint_on_error(self, builder, increment_storage):
        error_message = "Error message"

        class ErrorBuildingBlock(BuildingBlock):

            def get_change(self, blueprint: Blueprint) -> Blueprint:
                raise ValueError(error_message)

        invalid_builder = builder.add(ErrorBuildingBlock())
        result = invalid_builder.build()
        assert result.error.args[0] == error_message
        increment_chain = increment_storage.load_chain(result.chain_id)
        n_truncated_moves = 1
        truncated_chain = increment_chain.truncate_to(increment_chain.length())
        valid_builder = builder.add(SexAssigner(sex=Sex.MALE))
        with patch.object(
            IncrementChain,
            IncrementChain.add_increment.__name__,
            wraps=IncrementChain.add_increment,
            autospec=True,
        ) as mock_add_increment:
            result = valid_builder.build(truncated_chain)
            assert isinstance(result.character, PresentableCharacter)
            assert mock_add_increment.call_count == n_truncated_moves
