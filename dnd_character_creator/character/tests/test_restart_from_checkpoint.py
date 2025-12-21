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
from dnd_character_creator.character.checkpoint import MemoryStorage
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.character.race.subraces import Subrace
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.choices.stats_creation.statistic import Statistic


class TestRestartFromCheckpoint:
    def test_restart_from_checkpoint(self):
        increment_storage = MemoryStorage()
        stats_priority = (
            Statistic.INTELLIGENCE,
            Statistic.CONSTITUTION,
            Statistic.WISDOM,
            Statistic.DEXTERITY,
            Statistic.CHARISMA,
            Statistic.STRENGTH,
        )
        class_ = Class.WIZARD
        RandomSpellAssigner(class_=class_)
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
        LEVEL = 16
        builder = (
            Builder(increment_storage=increment_storage)
            .add(
                InitialBuilder(
                    blocks=(
                        LevelAssigner(level=LEVEL),
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
                    blocks=tuple(level_up for _ in range(LEVEL - 1))
                )
            )
            .add(
                RandomSubclassAssigner(
                    class_=class_,
                )
            )
        )
        builder.build()
