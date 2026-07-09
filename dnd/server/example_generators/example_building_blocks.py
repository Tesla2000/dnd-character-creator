from dnd.character.blueprint.building_blocks import (
    LevelAssigner, AnyBuildingBlock,
)
from dnd.character.blueprint.building_blocks import (
    PriorityStatChoiceResolver,
)
from dnd.character.blueprint.building_blocks import (
    HumanRaceAssigner,
)
from dnd.character.blueprint.building_blocks import (
    RandomFeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks import (
    RandomInitialDataFiller,
)
from dnd.character.blueprint.building_blocks import (
    RandomLanguageChoiceResolver,
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
from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.equipment_chooser import (
    RandomEquipmentChooser,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.max_first import (
    MaxFirstResolver,
)
from dnd.character.blueprint.building_blocks.initial_builder import (
    InitialBuilder,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment import (
    WizardRandomSpellAssigner,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.evocation.level_2 import (
    WizardLevel2Evocation,
)
from dnd.character.blueprint.building_blocks.level_up.wizard.level_1 import (
    WizardLevel1,
)
from dnd.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd.character.race.subraces import SubraceName
from dnd.choices.class_creation.character_class import Class
from dnd.choices.stats_creation.statistic import Statistic


def example_building_blocks() -> tuple[AnyBuildingBlock, ...]:
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
        language_choice_resolver=RandomLanguageChoiceResolver(),
        skill_choice_resolver=RandomSkillChoiceResolver(),
        feat_choice_resolver=MaxFirstResolver(
            priority=stats_priority,
            then=RandomFeatChoiceResolver(),
        ),
        tool_proficiency_choice_resolver=RandomToolProficiencyChoiceResolver(),
        stat_choice_resolver=PriorityStatChoiceResolver(priority=stats_priority),
        equipment_chooser=RandomEquipmentChooser(),
    )
    health_increase = HealthIncreaseAverage(class_=class_)
    spell_assigner = WizardRandomSpellAssigner()
    return (
        InitialBuilder(
            level_assigner=LevelAssigner(level=2),
            stats_builder=StandardArray(stats_priority=stats_priority),
            race_assigner=HumanRaceAssigner(
                subrace=SubraceName.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK,
            ),
            all_choices_resolver=AllChoicesResolver(
                language_choice_resolver=RandomLanguageChoiceResolver(),
                skill_choice_resolver=RandomSkillChoiceResolver(),
                feat_choice_resolver=MaxFirstResolver(
                    priority=stats_priority,
                    then=RandomFeatChoiceResolver(),
                ),
                tool_proficiency_choice_resolver=RandomToolProficiencyChoiceResolver(),
                stat_choice_resolver=PriorityStatChoiceResolver(
                    priority=stats_priority
                ),
                equipment_chooser=RandomEquipmentChooser(),
            ),
        ),
        RandomInitialDataFiller(),
        WizardLevel1(health_increase=health_increase, spell_assigner=spell_assigner),
        WizardLevel2Evocation(
            health_increase=health_increase, spell_assigner=spell_assigner
        ),
        all_choices_resolver,
    )
