from __future__ import annotations

import pytest
from dnd_character_creator.character.blueprint.building_blocks import (
    AIMagicalItemChooser,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    AIPartialBuilderAssigner,
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
    RandomLanguageChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    RandomMagicalItemChooser,
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
    AIAllChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver import (
    AllChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.ai import (
    AIAllNonStatChoicesResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.base_resolver import (
    AllChoicesResolverBase,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser.random import (
    RandomEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver.max_first import (
    MaxFirstResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver.max_if_not_maxed import (
    MaxIfNotMaxedResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_builder import (
    InitialBuilder,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler import (
    RandomInitialDataFiller,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler.base_filler import (
    InitialDataFiller,
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
from dnd_character_creator.character.blueprint.building_blocks.subclass_assigner import (
    SubclassAssigner,
)
from dnd_character_creator.character.builder import Builder
from dnd_character_creator.character.character import Character
from dnd_character_creator.character.checkpoint import InMemoryIncrementStorage
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.character.race.subraces import Subrace
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.choices.class_creation.character_class import (
    SorcererSubclass,
)
from dnd_character_creator.choices.stats_creation.statistic import Statistic
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


@pytest.mark.integration
class TestBuildMulticlass:
    # Common test configuration
    STATS_PRIORITY = (
        Statistic.INTELLIGENCE,
        Statistic.CONSTITUTION,
        Statistic.WISDOM,
        Statistic.DEXTERITY,
        Statistic.CHARISMA,
        Statistic.STRENGTH,
    )
    LEVEL = 16
    SORC_LEVEL = 6
    RACE = Race.HUMAN
    SUBRACE = Subrace.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK
    WIZARD_CLASS = Class.WIZARD
    SORC_CLASS = Class.SORCERER
    sorc_subclasses = (
        SorcererSubclass.DRACONIC_BLOODLINE,
        SorcererSubclass.STORM_SORCERY,
    )

    @classmethod
    def _create_level_up(cls, all_choices_resolver, class_: Class):
        """Create standard level up block for wizard tests."""
        return LevelUp(
            blocks=(
                LevelIncrementer(class_=class_),
                HealthIncreaseAverage(class_=class_),
                RandomSpellAssigner(class_=class_),
                all_choices_resolver,
            ),
        )

    @classmethod
    def _build_multiclass(
        cls,
        magical_item_chooser,
        all_choices_resolver: AllChoicesResolverBase,
        initial_data_filler: InitialDataFiller,
        wiz_subclass_assigner: SubclassAssigner,
        sorc_subclass_assigner: SubclassAssigner,
    ):
        """Build a wizard character with the specified magical item chooser.

        Args:
            magical_item_chooser: MagicalItemChooserBase instance.
            all_choices_resolver: Optional custom AllChoicesResolverBase.
                If None, uses standard random resolver.

        Returns:
            Built wizard character.
        """
        level_up_wizard = cls._create_level_up(
            all_choices_resolver, class_=Class.WIZARD
        )
        level_up_sorc = cls._create_level_up(
            all_choices_resolver, class_=Class.SORCERER
        )

        builder = (
            Builder(increment_storage=InMemoryIncrementStorage())
            .add(
                InitialBuilder(
                    blocks=(
                        LevelAssigner(level=cls.LEVEL),
                        StandardArray(stats_priority=cls.STATS_PRIORITY),
                        RaceAssigner(
                            race=cls.RACE,
                            subrace=cls.SUBRACE,
                        ),
                        all_choices_resolver,
                        level_up_wizard,
                    )
                )
            )
            .add(initial_data_filler)
            .add(
                LevelUpMultiple(
                    blocks=tuple(
                        level_up_wizard
                        for _ in range(cls.LEVEL - cls.SORC_LEVEL - 1)
                    )
                )
            )
            .add(
                LevelUpMultiple(
                    blocks=tuple(level_up_sorc for _ in range(cls.SORC_LEVEL))
                )
            )
            .add(wiz_subclass_assigner)
            .add(sorc_subclass_assigner)
            .add(magical_item_chooser)
        )
        return builder.build()

    def test_build_multiclass(self):
        """Test wizard build with random magical item selection."""
        magical_item_chooser = RandomMagicalItemChooser(
            n_uncommon=1,
            n_rare=2,
            n_very_rare=1,
            n_legendary=1,
            seed=42,
        )
        wizard = self._build_multiclass(
            magical_item_chooser,
            AllChoicesResolver(
                blocks=(
                    RandomLanguageChoiceResolver(),
                    RandomSkillProficiencyChoiceResolver(),
                    MaxFirstResolver(
                        priority=self.STATS_PRIORITY,
                        then=RandomFeatChoiceResolver(),
                    ),
                    RandomToolProficiencyChoiceResolver(),
                    PriorityStatChoiceResolver(priority=self.STATS_PRIORITY),
                    RandomSkillChoiceResolver(),
                    RandomEquipmentChooser(),
                ),
            ),
            RandomInitialDataFiller(),
            RandomSubclassAssigner(class_=self.WIZARD_CLASS),
            RandomSubclassAssigner(
                class_=self.SORC_CLASS,
                available_subclasses=self.sorc_subclasses,
            ),
        ).character

        assert isinstance(wizard, Character)
        assert wizard.weapons
        assert wizard.other_equipment
        assert wizard.magical_items
        assert (
            len(wizard.magical_items) == 5
        )  # 1 uncommon + 2 rare + 1 very_rare + 1 legendary
        print(
            wizard.model_dump_json(
                indent=2,
                exclude_defaults=True,
            )
        )

    @pytest.mark.requires_api_key
    def test_build_multiclass_with_ai(self):
        """Test wizard build with AI-powered choices (all choices including magical items)."""
        # Create LLM for AI-powered choices
        llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

        # Use AI for ALL choices (languages, skills, feats, stats, magical items)
        all_choices_resolver = AIAllChoicesResolver(
            blocks=(
                PriorityStatChoiceResolver(priority=self.STATS_PRIORITY),
                RandomEquipmentChooser(),
                MaxIfNotMaxedResolver(priority=self.STATS_PRIORITY),
                AIAllNonStatChoicesResolver(llm=llm),
            )
        )

        # Use AI for magical item selection
        magical_item_chooser = AIMagicalItemChooser(
            llm=llm,
            n_uncommon=2,
            n_rare=1,
            n_very_rare=1,
        )

        wizard = self._build_multiclass(
            magical_item_chooser,
            all_choices_resolver,
            AIPartialBuilderAssigner(
                # description="Rządna władzy czarodziejka gotowa złamać wszelkie zasady by osiągnąć cel, preferuje manipulację i magię błyskawic",
                description="Gwałtowna jak burza magini o wielkiej sile rażenia, z precyzją pozbywa się swoich wrogów, używając błyskawic",
                llm=llm,
            ),
        ).character

        assert isinstance(wizard, Character)
        assert wizard.weapons
        assert wizard.other_equipment
        assert wizard.magical_items
        assert (
            len(wizard.magical_items) == 4
        )  # 2 uncommon + 1 rare + 1 very_rare

        # Verify that AI selected appropriate items for a wizard
        # (this is a soft check - AI should pick synergistic items)
        item_names = [item.name for item in wizard.magical_items]
        print(f"\nAI-selected magical items: {item_names}")
        print(
            wizard.model_dump_json(
                indent=2,
                exclude_defaults=True,
            )
        )
