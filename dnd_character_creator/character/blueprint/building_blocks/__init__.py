from __future__ import annotations

from typing import Annotated
from typing import Self
from typing import Union

from dnd_character_creator.character.blueprint.building_blocks.age_assigner import (
    AgeAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.alignment_assigner import (
    AlignmentAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver import (
    AIAllChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver import (
    AllChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.background_assigner import (
    BackgroundAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    SerializableBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.character_base_template import (
    CharacterBaseTemplate,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_adder import (
    EquipmentAdder,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser import (
    AIEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser import (
    RandomEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_adder import (
    FeatAdder,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver import (
    AIFeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver import (
    MaxFirstResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver import (
    MaxIfNotMaxedResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver import (
    RandomFeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.feature_assigner import (
    FeatureAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.get_discriminator import (
    get_discriminator,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_builder import (
    InitialBuilder,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler import (
    AIBaseBuilderAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler import (
    AIPartialBuilderAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler import (
    RandomInitialDataFiller,
)
from dnd_character_creator.character.blueprint.building_blocks.language_choice_resolver import (
    AILanguageChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.language_choice_resolver import (
    RandomLanguageChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.level_assigner import (
    LevelAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.health_increase import (
    HealthIncreaseAverage,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.health_increase import (
    HealthIncreaseRandom,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.health_increase import (
    HealthIncreaseRandomMinTwo,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.health_increase import (
    HealthIncreaseRandomRerollOnes,
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
    LLMSpellAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.spell_assignment import (
    RandomSpellAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.magical_item_chooser import (
    AIMagicalItemChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.magical_item_chooser import (
    RandomMagicalItemChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.name_assigner import (
    NameAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.race_assigner import (
    RaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.race_assigner import (
    RandomRaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.sex_assigner import (
    SexAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.skill_choice_resolver import (
    AISkillChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.skill_choice_resolver import (
    RandomSkillChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stat_choice_resolver import (
    AIStatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stat_choice_resolver import (
    PriorityStatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner import (
    AISubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner import (
    RandomSubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.optional import (
    OptionalSubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.tool_proficiency_choice_resolver import (
    AIToolProficiencyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.tool_proficiency_choice_resolver import (
    RandomToolProficiencyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.weapon_adder import (
    WeaponAdder,
)
from pydantic import InstanceOf
from pydantic import Tag
from subclass_getter import get_unique_subclasses

AnyBuildingBlock = Annotated[
    Union.__getitem__(
        tuple(
            Annotated[class_, Tag(class_.get_block_type())]
            for class_ in get_unique_subclasses(SerializableBlock)
        )
    ),
    get_discriminator(),
]
CombinedBlock.model_rebuild()
Blocks = tuple[
    Union[AnyBuildingBlock, Self, InstanceOf[BuildingBlock]],  # noqa: F821
    ...,
]
__all__ = [
    "AgeAssigner",
    "AIBaseBuilderAssigner",
    "AIAllChoicesResolver",
    "AIEquipmentChooser",
    "AIFeatChoiceResolver",
    "AILanguageChoiceResolver",
    "AIMagicalItemChooser",
    "AIPartialBuilderAssigner",
    "AISkillChoiceResolver",
    "AIStatChoiceResolver",
    "AIToolProficiencyChoiceResolver",
    "AllChoicesResolver",
    "AlignmentAssigner",
    "BackgroundAssigner",
    "CharacterBaseTemplate",
    "EquipmentAdder",
    "FeatAdder",
    "FeatureAssigner",
    "HealthIncreaseAverage",
    "HealthIncreaseRandom",
    "HealthIncreaseRandomMinTwo",
    "HealthIncreaseRandomRerollOnes",
    "LevelAssigner",
    "LevelIncrementer",
    "LevelUp",
    "LevelUpMultiple",
    "LLMSpellAssigner",
    "MaxFirstResolver",
    "MaxIfNotMaxedResolver",
    "NameAssigner",
    "InitialBuilder",
    "OptionalSubclassAssigner",
    "PriorityStatChoiceResolver",
    "RaceAssigner",
    "RandomEquipmentChooser",
    "RandomFeatChoiceResolver",
    "RandomInitialDataFiller",
    "RandomLanguageChoiceResolver",
    "RandomMagicalItemChooser",
    "RandomRaceAssigner",
    "RandomSkillChoiceResolver",
    "RandomSpellAssigner",
    "RandomToolProficiencyChoiceResolver",
    "AISubclassAssigner",
    "RandomSubclassAssigner",
    "SexAssigner",
    "StandardArray",
    "WeaponAdder",
    "AnyBuildingBlock",
    "Blocks",
]
