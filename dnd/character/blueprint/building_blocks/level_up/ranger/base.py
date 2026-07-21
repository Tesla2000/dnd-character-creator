from abc import ABC
from abc import abstractmethod
from typing import Literal

from pydantic import Field
from pydantic import PositiveInt

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.fighting_style_choice_resolver import (
    AnyFightingStyleChoiceResolver,
    RandomFightingStyleChoiceResolver,
)
from dnd.character.blueprint.building_blocks.feat_block import (
    AnyFeatBlock,
    AnyFeatSelectionBlock,
)
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    AnyD10HealthIncrease,
    D10HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment import (
    AnyRangerSpellAssigner,
    RangerRandomSpellAssigner,
)
from dnd.character.ac_modifier import FlatAcModifier
from dnd.character.blueprint.sentinels import AnyClassLevel
from dnd.character.blueprint.sentinels import AnyDruidLevel
from dnd.character.blueprint.sentinels import AnySorcererLevel
from dnd.character.blueprint.sentinels import AnyStatChoices
from dnd.character.blueprint.sentinels import AnyWizardLevel
from dnd.character.blueprint.sentinels import ClassPreSubclassLevel
from dnd.character.blueprint.sentinels import ClassSubclassLevel
from dnd.character.blueprint.sentinels import DruidInfo
from dnd.character.blueprint.sentinels import MaybeCharacterData
from dnd.character.blueprint.sentinels import MaybeHealth
from dnd.character.blueprint.sentinels import ThirdSubclassPostLevel
from dnd.character.blueprint.sentinels import ThirdSubclassPreLevel
from dnd.character.blueprint.states._caster_info import CasterInfo
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.blueprint.states.state import _BPT
from dnd.character.blueprint.states.wizard._info import WizardInfo
from dnd.character.race.race import Race
from dnd.character.spells.max_spell_levels import HALF_CASTER_SPELL_SLOTS
from dnd.character.stats import Stats
from dnd.choices.abilities.fighting_style import FightingStyle
from dnd.choices.class_creation.character_class import Class
from dnd.choices.class_creation.character_class import RangerSubclass


class RangerUpgradeLevelBase[LevelIn: AnyClassLevel, LevelOut: AnyClassLevel](
    BuildingBlock, ABC
):
    """Base for RangerLevel1: no spellcasting or fighting style yet."""

    health_increase: AnyD10HealthIncrease = Field(
        default_factory=D10HealthIncreaseAverage
    )

    @abstractmethod
    def _update_blueprint(self, blueprint: _BPT) -> _BPT: ...

    def apply[
        _HeK_: MaybeHealth,
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WIK_: WizardInfo[AnyWizardLevel] | None,
        _CK_: CasterInfo | None,
        _SOK_: AnySorcererLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _DRK_: DruidInfo[AnyDruidLevel] | None,
        _PAK_: AnyClassLevel,
        _MOK_: AnyClassLevel,
        _BDK_: AnyClassLevel,
        _WAK_: AnyClassLevel,
        _ARK_: AnyClassLevel,
        _CDK_: MaybeCharacterData,
    ](
        self,
        blueprint: Blueprint[
            Race,
            Stats,
            _HeK_,
            _StCK_,
            _SkCK_,
            _WIK_,
            _CK_,
            _SOK_,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            LevelIn,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ],
    ) -> Blueprint[
        Race,
        Stats,
        PositiveInt,
        _StCK_,
        _SkCK_,
        _WIK_,
        _CK_,
        _SOK_,
        _FGK_,
        _BAK_,
        _ROK_,
        _CLK_,
        _DRK_,
        _PAK_,
        LevelOut,
        _MOK_,
        _BDK_,
        _WAK_,
        _ARK_,
        _CDK_,
    ]:
        r1 = self._update_blueprint(blueprint)
        r2 = self.health_increase.apply(r1)
        return Blueprint[
            Race,
            Stats,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WIK_,
            _CK_,
            _SOK_,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            LevelOut,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(dict(r2))


class RangerSpellcastingLevelBase[LevelIn: AnyClassLevel, LevelOut: AnyClassLevel](
    BuildingBlock, ABC
):
    """Base for RangerLevel2: grants Fighting Style and starts spellcasting."""

    health_increase: AnyD10HealthIncrease = Field(
        default_factory=D10HealthIncreaseAverage
    )
    fighting_style_choice_resolver: AnyFightingStyleChoiceResolver = Field(
        default_factory=RandomFightingStyleChoiceResolver
    )
    spell_assigner: AnyRangerSpellAssigner = Field(
        default_factory=RangerRandomSpellAssigner
    )

    @abstractmethod
    def _update_blueprint(self, blueprint: _BPT) -> _BPT: ...

    def apply[
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WIK_: WizardInfo[AnyWizardLevel] | None,
        _SOK_: AnySorcererLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _DRK_: DruidInfo[AnyDruidLevel] | None,
        _PAK_: AnyClassLevel,
        _MOK_: AnyClassLevel,
        _BDK_: AnyClassLevel,
        _WAK_: AnyClassLevel,
        _ARK_: AnyClassLevel,
        _CDK_: MaybeCharacterData,
    ](
        self,
        blueprint: Blueprint[
            Race,
            Stats,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WIK_,
            None,
            _SOK_,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            LevelIn,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ],
    ) -> Blueprint[
        Race,
        Stats,
        PositiveInt,
        _StCK_,
        _SkCK_,
        _WIK_,
        CasterInfo,
        _SOK_,
        _FGK_,
        _BAK_,
        _ROK_,
        _CLK_,
        _DRK_,
        _PAK_,
        LevelOut,
        _MOK_,
        _BDK_,
        _WAK_,
        _ARK_,
        _CDK_,
    ]:
        r1 = self._update_blueprint(blueprint)
        r2 = self.health_increase.apply(r1)
        r3 = self.fighting_style_choice_resolver.apply(r2)
        if r3.fighting_style is FightingStyle.DEFENSE:
            r3 = r3.model_copy(
                update={"ac_modifiers": r3.ac_modifiers + (FlatAcModifier(amount=1),)}
            )
        caster_info = CasterInfo(spell_slots=HALF_CASTER_SPELL_SLOTS[1], caster_level=2)
        interim = Blueprint[
            Race,
            Stats,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WIK_,
            CasterInfo,
            _SOK_,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            LevelOut,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(dict(r3) | {"caster": caster_info})
        return self.spell_assigner.apply(interim)


class RangerSharedLevelBase[LevelIn: AnyClassLevel, LevelOut: AnyClassLevel](
    BuildingBlock, ABC
):
    """Base for post-level-2 ranger levels (4, 5) shared across all conclaves."""

    health_increase: AnyD10HealthIncrease = Field(
        default_factory=D10HealthIncreaseAverage
    )
    spell_assigner: AnyRangerSpellAssigner = Field(
        default_factory=RangerRandomSpellAssigner
    )

    @abstractmethod
    def _update_blueprint(self, blueprint: _BPT) -> _BPT: ...

    def apply[
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WIK_: WizardInfo[AnyWizardLevel] | None,
        _SOK_: AnySorcererLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _DRK_: DruidInfo[AnyDruidLevel] | None,
        _PAK_: AnyClassLevel,
        _MOK_: AnyClassLevel,
        _BDK_: AnyClassLevel,
        _WAK_: AnyClassLevel,
        _ARK_: AnyClassLevel,
        _CDK_: MaybeCharacterData,
    ](
        self,
        blueprint: Blueprint[
            Race,
            Stats,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WIK_,
            CasterInfo,
            _SOK_,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            LevelIn,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ],
    ) -> Blueprint[
        Race,
        Stats,
        PositiveInt,
        _StCK_,
        _SkCK_,
        _WIK_,
        CasterInfo,
        _SOK_,
        _FGK_,
        _BAK_,
        _ROK_,
        _CLK_,
        _DRK_,
        _PAK_,
        LevelOut,
        _MOK_,
        _BDK_,
        _WAK_,
        _ARK_,
        _CDK_,
    ]:
        r1 = self._update_blueprint(blueprint)
        r2 = self.health_increase.apply(r1)
        after_spells = self.spell_assigner.apply(r2)
        new_level = after_spells.classes.get_level(Class.RANGER)
        new_caster = after_spells.caster.increase_half_caster(new_level)
        return after_spells.model_copy(update={"caster": new_caster})


class RangerSubclassAssignLevelBase[SubclassOut: RangerSubclass](BuildingBlock, ABC):
    """Base for RangerLevel3*: assigns subclass and advances spellcasting."""

    health_increase: AnyD10HealthIncrease = Field(
        default_factory=D10HealthIncreaseAverage
    )
    spell_assigner: AnyRangerSpellAssigner = Field(
        default_factory=RangerRandomSpellAssigner
    )

    @abstractmethod
    def _update_blueprint(self, blueprint: _BPT) -> _BPT: ...

    def apply[
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WIK_: WizardInfo[AnyWizardLevel] | None,
        _SOK_: AnySorcererLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _DRK_: DruidInfo[AnyDruidLevel] | None,
        _PAK_: AnyClassLevel,
        _MOK_: AnyClassLevel,
        _BDK_: AnyClassLevel,
        _WAK_: AnyClassLevel,
        _ARK_: AnyClassLevel,
        _CDK_: MaybeCharacterData,
    ](
        self,
        blueprint: Blueprint[
            Race,
            Stats,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WIK_,
            CasterInfo,
            _SOK_,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            ClassPreSubclassLevel[ThirdSubclassPreLevel, None],
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ],
    ) -> Blueprint[
        Race,
        Stats,
        PositiveInt,
        _StCK_,
        _SkCK_,
        _WIK_,
        CasterInfo,
        _SOK_,
        _FGK_,
        _BAK_,
        _ROK_,
        _CLK_,
        _DRK_,
        _PAK_,
        ClassSubclassLevel[Literal[ThirdSubclassPostLevel.THIRD], SubclassOut],
        _MOK_,
        _BDK_,
        _WAK_,
        _ARK_,
        _CDK_,
    ]:
        r1 = self._update_blueprint(blueprint)
        r2 = self.health_increase.apply(r1)
        after_spells = self.spell_assigner.apply(r2)
        new_level = after_spells.classes.get_level(Class.RANGER)
        new_caster = after_spells.caster.increase_half_caster(new_level)
        return Blueprint[
            Race,
            Stats,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WIK_,
            CasterInfo,
            _SOK_,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            ClassSubclassLevel[Literal[ThirdSubclassPostLevel.THIRD], SubclassOut],
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(dict(after_spells) | {"caster": new_caster})


class RangerFeatGrantingLevelBase[
    LevelIn: AnyClassLevel,
    LevelOut: AnyClassLevel,
](RangerSharedLevelBase[LevelIn, LevelOut]):
    """Base for ranger levels that grant a feat choice (4, 8, 12, 16, 19)."""

    feat_block: AnyFeatBlock = Field(default_factory=AnyFeatSelectionBlock)

    def apply[
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WIK_: WizardInfo[AnyWizardLevel] | None,
        _SOK_: AnySorcererLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _DRK_: DruidInfo[AnyDruidLevel] | None,
        _PAK_: AnyClassLevel,
        _MOK_: AnyClassLevel,
        _BDK_: AnyClassLevel,
        _WAK_: AnyClassLevel,
        _ARK_: AnyClassLevel,
        _CDK_: MaybeCharacterData,
    ](
        self,
        blueprint: Blueprint[
            Race,
            Stats,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WIK_,
            CasterInfo,
            _SOK_,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            LevelIn,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ],
    ) -> Blueprint[
        Race,
        Stats,
        PositiveInt,
        _StCK_,
        _SkCK_,
        _WIK_,
        CasterInfo,
        _SOK_,
        _FGK_,
        _BAK_,
        _ROK_,
        _CLK_,
        _DRK_,
        _PAK_,
        LevelOut,
        _MOK_,
        _BDK_,
        _WAK_,
        _ARK_,
        _CDK_,
    ]:
        result = super().apply(blueprint)
        feat_applied = self.feat_block.apply(result)
        return result.model_copy(
            update={
                "feats": feat_applied.feats,
                "stats": feat_applied.stats,
                "n_stat_choices": feat_applied.n_stat_choices,
            }
        )
