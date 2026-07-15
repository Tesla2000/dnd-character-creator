from dnd.character.blueprint.building_blocks import (
    AnyBuildingBlock,
)
from dnd.character.blueprint.building_blocks import (
    HumanRaceAssigner,
)
from dnd.character.blueprint.building_blocks import (
    RandomInitialDataFiller,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.max_if_not_maxed import (
    MaxIfNotMaxedResolver,
)
from dnd.character.blueprint.building_blocks.language_choice_resolver.random import (
    RandomLanguageChoiceResolver,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    D6HealthIncreaseAverage,
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
from dnd.character.blueprint.building_blocks.skill_choice_resolver.random import (
    RandomSkillChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stat_choice_resolver import (
    PriorityStatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd.character.race.subraces import SubraceName
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
    health_increase = D6HealthIncreaseAverage()
    spell_assigner = WizardRandomSpellAssigner()
    return (
        StandardArray(stats_priority=stats_priority),
        HumanRaceAssigner(
            subrace=SubraceName.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK,
            stat_choice_resolver=PriorityStatChoiceResolver(priority=stats_priority),
            skill_choice_resolver=RandomSkillChoiceResolver(),
            language_choice_resolver=RandomLanguageChoiceResolver(),
            feat_choice_resolver=MaxIfNotMaxedResolver(priority=stats_priority),
        ),
        RandomInitialDataFiller(),
        WizardLevel1(health_increase=health_increase, spell_assigner=spell_assigner),
        WizardLevel2Evocation(
            health_increase=health_increase, spell_assigner=spell_assigner
        ),
    )
