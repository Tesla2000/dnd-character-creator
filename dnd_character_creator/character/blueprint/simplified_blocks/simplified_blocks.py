from collections import Counter
from collections.abc import Mapping
from itertools import chain
from typing import Any
from typing import Self

from dnd_character_creator.character.blueprint.building_blocks import (
    LevelAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    PriorityStatChoiceResolver,
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
    RandomMagicalItemChooser,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomSkillChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomToolProficiencyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver import (
    AllChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver import (
    AnyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    Blocks,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser import (
    AnyEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser import (
    RandomEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver import (
    AnyFeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver.max_first import (
    MaxFirstResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_builder import (
    InitialBuilder,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_builder import (
    InitialBuilderBlocks,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler import (
    AnyInitialDataFiller,
)
from dnd_character_creator.character.blueprint.building_blocks.language_choice_resolver import (
    AnyLanguageChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.health_increase import (
    AnyHealthIncrease,
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
from dnd_character_creator.character.blueprint.building_blocks.level_up.level_up import (
    LevelUpBlocks,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.spell_assignment import (
    AnySpellAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.level_up.spell_assignment import (
    RandomSpellAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.magical_item_chooser import (
    AnyMagicalItemChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.race_assigner import (
    AnyRaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.race_assigner import (
    RandomRaceAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.skill_choice_resolver import (
    AnySkillChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stat_choice_resolver import (
    AnyStatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_builder import (
    AnyStatsBuilder,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd_character_creator.character.blueprint.building_blocks.stats_priority import (
    StatsPriority,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner import (
    AnySubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner import (
    RandomSubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner.optional import (
    OptionalSubclassAssigner,
)
from dnd_character_creator.character.blueprint.building_blocks.tool_proficiency_choice_resolver import (
    AnyToolProficiencyChoiceResolver,
)
from dnd_character_creator.character.blueprint.simplified_blocks.class_to_stats_priority import (
    CLASS_TO_STATS_PRIORITY,
)
from dnd_character_creator.character.character import ClassLevel
from dnd_character_creator.choices.class_creation.character_class import Class
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import model_validator
from pydantic import ModelWrapValidatorHandler


class Classes(BaseModel):
    model_config = ConfigDict(frozen=True)
    class_levels: Mapping[Class, ClassLevel] = Field(min_length=1)
    main_class: Class = Field(
        default_factory=lambda validated_data: max(
            validated_data["class_levels"],
            key=validated_data["class_levels"].__getitem__,
        ),
        exclude=True,
    )

    @model_validator(mode="after")
    def _validate_max_level(self) -> Self:
        total_level = self.get_total_level()
        if total_level > 20:
            raise ValueError(
                f"Total level of classes {self.class_levels} is greater than 20"
            )
        return self

    def get_total_level(self) -> ClassLevel:
        return sum(self.class_levels.values())


class SimplifiedBlocks(CombinedBlock):
    classes: Classes
    stats_priority: StatsPriority = Field(
        default_factory=lambda validated_data: CLASS_TO_STATS_PRIORITY[
            validated_data["classes"].main_class
        ]
    )
    language_choice_resolver: AnyLanguageChoiceResolver = Field(
        default_factory=RandomLanguageChoiceResolver
    )
    skill_choice_resolver: AnySkillChoiceResolver = Field(
        default_factory=RandomSkillChoiceResolver
    )
    feat_choice_resolver: AnyFeatChoiceResolver = Field(
        default_factory=lambda validated_data: MaxFirstResolver(
            priority=validated_data["stats_priority"],
            then=RandomFeatChoiceResolver(),
        )
    )
    tool_proficiencies_resolver: AnyToolProficiencyChoiceResolver = Field(
        default_factory=RandomToolProficiencyChoiceResolver
    )
    stat_choice_resolver: AnyStatChoiceResolver = Field(
        default_factory=lambda validated_data: PriorityStatChoiceResolver(
            priority=validated_data["stats_priority"]
        )
    )
    equipment_chooser: AnyEquipmentChooser = Field(
        default_factory=RandomEquipmentChooser
    )
    all_choices_resolver: AnyChoiceResolver = Field(
        default_factory=lambda validated_data: AllChoicesResolver(
            blocks=(
                validated_data["language_choice_resolver"],
                validated_data["skill_choice_resolver"],
                validated_data["feat_choice_resolver"],
                validated_data["tool_proficiencies_resolver"],
                validated_data["stat_choice_resolver"],
                validated_data["equipment_chooser"],
            ),
        )
    )
    level_incrementers: tuple[LevelIncrementer, ...] = Field(
        default_factory=lambda validated_data: tuple(
            chain.from_iterable(
                (
                    level * (LevelIncrementer(class_=class_),)
                    for class_, level in validated_data[
                        "classes"
                    ].class_levels.items()
                )
            )
        )
    )

    @model_validator(mode="after")
    def _verify_correct_number_of_increments(self) -> Self:
        if len(self.level_incrementers) != self.classes.get_total_level():
            raise ValueError(
                f"Number of level increments {len(self.level_incrementers)} doesn't match level {self.classes.get_total_level()}"
            )
        return self

    @model_validator(mode="after")
    def _validate_increments_match_classes(self) -> Self:
        increment_classes = dict(
            Counter(increment.class_ for increment in self.level_incrementers)
        )
        class_levels = dict(self.classes.class_levels)
        if increment_classes == class_levels:
            return self
        raise ValueError(f"{increment_classes=} don't match {class_levels=}")

    health_increases: tuple[AnyHealthIncrease, ...] = Field(
        default_factory=lambda validated_data: tuple(
            chain.from_iterable(
                (
                    level * (HealthIncreaseAverage(class_=class_),)
                    for class_, level in validated_data[
                        "classes"
                    ].class_levels.items()
                )
            )
        )
    )

    @model_validator(mode="after")
    def _verify_correct_number_of_health_increases(self) -> Self:
        if len(self.health_increases) != self.classes.get_total_level():
            raise ValueError(
                f"Number of health increases {len(self.health_increases)} doesn't match level {self.classes.get_total_level()}"
            )
        return self

    @model_validator(mode="after")
    def _validate_health_increases_match_classes(self) -> Self:
        increases_classes = dict(
            Counter(increase.class_ for increase in self.health_increases)
        )
        class_levels = dict(self.classes.class_levels)
        if increases_classes == class_levels:
            return self
        raise ValueError(f"{increases_classes=} don't match {class_levels=}")

    spell_assigners: tuple[AnySpellAssigner, ...] = Field(
        default_factory=lambda validated_data: tuple(
            chain.from_iterable(
                (
                    level * (RandomSpellAssigner(class_=class_),)
                    for class_, level in validated_data[
                        "classes"
                    ].class_levels.items()
                )
            )
        )
    )

    @model_validator(mode="after")
    def _verify_correct_number_of_spell_assignments(self) -> Self:
        if len(self.spell_assigners) != self.classes.get_total_level():
            raise ValueError(
                f"Number of health increases {len(self.spell_assigners)} doesn't match level {self.classes.get_total_level()}"
            )
        return self

    @model_validator(mode="after")
    def _validate_spell_assigners_match_classes(self) -> Self:
        spell_assignment_classes = dict(
            Counter(increase.class_ for increase in self.spell_assigners)
        )
        class_levels = dict(self.classes.class_levels)
        if spell_assignment_classes == class_levels:
            return self
        raise ValueError(
            f"{spell_assignment_classes=} don't match {class_levels=}"
        )

    level_ups: tuple[LevelUp, ...] = Field(
        default_factory=lambda validated_data: tuple(
            LevelUp(
                blocks=LevelUpBlocks(
                    level_increment=level,
                    health_increase=health,
                    spell_assigner=spell,
                    all_choice_resolver=validated_data["all_choices_resolver"],
                ),
            )
            for level, health, spell in zip(
                validated_data["level_incrementers"],
                validated_data["health_increases"],
                validated_data["spell_assigners"],
            )
        )
    )

    @model_validator(mode="after")
    def _validate_level_up_classes_correspondence(self) -> Self:
        invalid_level_ups = []
        for level, level_up in enumerate(self.level_ups, 1):
            blocks = level_up.blocks
            if (
                blocks.level_increment.class_
                == blocks.health_increase.class_
                == blocks.spell_assigner.class_
            ):
                continue
            invalid_level_ups.append(
                f"Level increment classes don't match for {level=}"
            )
        if invalid_level_ups:
            raise ValueError("\n".join(invalid_level_ups))
        return self

    stats_builder: AnyStatsBuilder = Field(
        default_factory=lambda validated_data: StandardArray(
            stats_priority=validated_data["stats_priority"]
        )
    )
    race_assigner: AnyRaceAssigner = Field(default_factory=RandomRaceAssigner)
    initial_builder: InitialBuilder = Field(
        default_factory=lambda validated_data: InitialBuilder(
            blocks=InitialBuilderBlocks(
                level_assigner=LevelAssigner(
                    level=validated_data["classes"].get_total_level()
                ),
                stats_builder=validated_data["stats_builder"],
                race_assigner=validated_data["race_assigner"],
                all_choices_resolver=validated_data["all_choices_resolver"],
            )
        )
    )
    initial_data_filler: AnyInitialDataFiller = Field(
        default_factory=RandomInitialDataFiller
    )
    subclass_assigners: tuple[AnySubclassAssigner, ...] = Field(
        default_factory=lambda validated_data: tuple(
            OptionalSubclassAssigner(
                class_=class_, assigner=RandomSubclassAssigner(class_=class_)
            )
            for class_ in validated_data["classes"].class_levels
        )
    )
    magical_items_assigner: AnyMagicalItemChooser = Field(
        default_factory=RandomMagicalItemChooser
    )
    blocks: Blocks = ()

    @model_validator(mode="wrap")
    @classmethod
    def _create_blocks(
        cls, data: Any, handler: ModelWrapValidatorHandler[Self]
    ) -> Self:
        self: Self = handler(data)
        if self.blocks or not isinstance(data, dict):
            return self
        return handler(
            {
                **data,
                "blocks": (
                    self.initial_builder,
                    self.initial_data_filler,
                    CombinedBlock(blocks=self.level_ups),
                    CombinedBlock(blocks=self.subclass_assigners),
                    self.magical_items_assigner,
                ),
            }
        )
