from abc import ABC
from abc import abstractmethod

from pydantic import Field

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    AnyD8HealthIncrease,
    D8HealthIncreaseAverage,
)
from dnd.character.blueprint.building_blocks.feat_block import (
    AnyFeatBlock,
    AnyFeatSelectionBlock,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment import (
    AnyDruidSpellAssigner,
    DruidRandomSpellAssigner,
)
from dnd.character.blueprint.sentinels import AnyClassLevel
from dnd.character.blueprint.sentinels import AnyNonZeroDruidLevel
from dnd.character.blueprint.sentinels import AnySorcererLevel
from dnd.character.blueprint.sentinels import AnyStatChoices
from dnd.character.blueprint.sentinels import AnyWizardLevel
from dnd.character.blueprint.sentinels import DruidInfo
from dnd.character.blueprint.sentinels import DruidSubclassLevel
from dnd.character.blueprint.sentinels import MaybeCharacterData
from dnd.character.blueprint.sentinels import MaybeHealth
from dnd.character.blueprint.sentinels import SecondSubclassPostLevel
from dnd.character.blueprint.states._caster_info import CasterInfo
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.blueprint.states.state import _BPT
from dnd.character.blueprint.states.wizard._info import WizardInfo
from dnd.character.race.race import Race
from dnd.character.spells.max_spell_levels import FULL_CASTER_SPELL_SLOTS
from dnd.character.stats import Stats
from dnd.choices.class_creation.character_class import DruidSubclass
from pydantic import PositiveInt


class DruidUpgradeLevelBase[LevelOut: AnyNonZeroDruidLevel](BuildingBlock, ABC):
    """Base for DruidLevel1: upgrades Blueprint[Race, Stats, ...] -> Blueprint[..., DruidInfo, CasterInfo, ...]."""

    health_increase: AnyD8HealthIncrease = Field(
        default_factory=D8HealthIncreaseAverage
    )
    spell_assigner: AnyDruidSpellAssigner = Field(
        default_factory=DruidRandomSpellAssigner
    )

    @abstractmethod
    def _update_blueprint(self, blueprint: _BPT) -> _BPT: ...

    def apply[
        _HeK_: MaybeHealth,
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WIK_: WizardInfo[AnyWizardLevel] | None,
        _SOK_: AnySorcererLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _PAK_: AnyClassLevel,
        _RAK_: AnyClassLevel,
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
            None,
            _SOK_,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            None,
            _PAK_,
            _RAK_,
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
        DruidInfo[LevelOut],
        _PAK_,
        _RAK_,
        _MOK_,
        _BDK_,
        _WAK_,
        _ARK_,
        _CDK_,
    ]:
        r1 = self._update_blueprint(blueprint)
        r2 = self.health_increase.apply(r1)
        druid_info: DruidInfo[LevelOut] = DruidInfo[LevelOut].model_validate(
            {"prepared_spells": ()}
        )
        caster_info = CasterInfo(spell_slots=FULL_CASTER_SPELL_SLOTS[0])
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
            DruidInfo[LevelOut],
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(dict(r2) | {"druid": druid_info, "caster": caster_info})
        after_spells = self.spell_assigner.apply(interim)
        new_caster = after_spells.caster.increase_full_caster()
        return after_spells.model_copy(update={"caster": new_caster})


class DruidPreSubclassLevelBase[
    LevelIn: AnyNonZeroDruidLevel,
    LevelOut: AnyNonZeroDruidLevel,
](BuildingBlock, ABC):
    """Base for DruidLevel2Moon: Blueprint[..., DruidInfo[LevelIn], ...] -> Blueprint[..., DruidInfo[LevelOut], ...]."""

    health_increase: AnyD8HealthIncrease = Field(
        default_factory=D8HealthIncreaseAverage
    )
    spell_assigner: AnyDruidSpellAssigner = Field(
        default_factory=DruidRandomSpellAssigner
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
        _PAK_: AnyClassLevel,
        _RAK_: AnyClassLevel,
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
            DruidInfo[LevelIn],
            _PAK_,
            _RAK_,
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
        DruidInfo[LevelOut],
        _PAK_,
        _RAK_,
        _MOK_,
        _BDK_,
        _WAK_,
        _ARK_,
        _CDK_,
    ]:
        r1 = self._update_blueprint(blueprint)
        r2 = self.health_increase.apply(r1)
        new_druid: DruidInfo[LevelOut] = DruidInfo[LevelOut].model_validate(
            {"prepared_spells": blueprint.druid.prepared_spells}
        )
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
            DruidInfo[LevelOut],
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(
            dict(r2)
            | {
                "druid": new_druid,
                "caster": blueprint.caster,
            }
        )
        after_spells = self.spell_assigner.apply(interim)
        new_caster = after_spells.caster.increase_full_caster()
        return after_spells.model_copy(update={"caster": new_caster})


class DruidSharedLevelBase[
    LevelIn: SecondSubclassPostLevel,
    LevelOut: SecondSubclassPostLevel,
](BuildingBlock, ABC):
    """Base for post-subclass druid levels (3-20) shared across all circles."""

    health_increase: AnyD8HealthIncrease = Field(
        default_factory=D8HealthIncreaseAverage
    )
    spell_assigner: AnyDruidSpellAssigner = Field(
        default_factory=DruidRandomSpellAssigner
    )

    @abstractmethod
    def _update_blueprint(self, blueprint: _BPT) -> _BPT: ...

    def apply[
        SubclassT: DruidSubclass,
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WIK_: WizardInfo[AnyWizardLevel] | None,
        _SOK_: AnySorcererLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _PAK_: AnyClassLevel,
        _RAK_: AnyClassLevel,
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
            DruidInfo[DruidSubclassLevel[LevelIn, SubclassT]],
            _PAK_,
            _RAK_,
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
        DruidInfo[DruidSubclassLevel[LevelOut, SubclassT]],
        _PAK_,
        _RAK_,
        _MOK_,
        _BDK_,
        _WAK_,
        _ARK_,
        _CDK_,
    ]:
        r1 = self._update_blueprint(blueprint)
        r2 = self.health_increase.apply(r1)
        new_druid: DruidInfo[DruidSubclassLevel[LevelOut, SubclassT]] = DruidInfo[
            DruidSubclassLevel[LevelOut, SubclassT]
        ].model_validate({"prepared_spells": blueprint.druid.prepared_spells})
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
            DruidInfo[DruidSubclassLevel[LevelOut, SubclassT]],
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(
            dict(r2)
            | {
                "druid": new_druid,
                "caster": blueprint.caster,
            }
        )
        after_spells = self.spell_assigner.apply(interim)
        new_caster = after_spells.caster.increase_full_caster()
        return after_spells.model_copy(update={"caster": new_caster})


class DruidFeatGrantingLevelBase[
    LevelIn: SecondSubclassPostLevel,
    LevelOut: SecondSubclassPostLevel,
](DruidSharedLevelBase[LevelIn, LevelOut]):
    """Base for druid levels that grant a feat choice (4, 8, 12, 16, 19)."""

    feat_block: AnyFeatBlock = Field(default_factory=AnyFeatSelectionBlock)

    def apply[
        SubclassT: DruidSubclass,
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WIK_: WizardInfo[AnyWizardLevel] | None,
        _SOK_: AnySorcererLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _PAK_: AnyClassLevel,
        _RAK_: AnyClassLevel,
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
            DruidInfo[DruidSubclassLevel[LevelIn, SubclassT]],
            _PAK_,
            _RAK_,
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
        DruidInfo[DruidSubclassLevel[LevelOut, SubclassT]],
        _PAK_,
        _RAK_,
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


class DruidSubclassFeatureLevelBase[
    LevelIn: AnyNonZeroDruidLevel,
    LevelOut: AnyNonZeroDruidLevel,
](BuildingBlock, ABC):
    """Base for druid levels 6, 10, 14 that grant subclass-specific features."""

    health_increase: AnyD8HealthIncrease = Field(
        default_factory=D8HealthIncreaseAverage
    )
    spell_assigner: AnyDruidSpellAssigner = Field(
        default_factory=DruidRandomSpellAssigner
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
        _PAK_: AnyClassLevel,
        _RAK_: AnyClassLevel,
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
            DruidInfo[LevelIn],
            _PAK_,
            _RAK_,
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
        DruidInfo[LevelOut],
        _PAK_,
        _RAK_,
        _MOK_,
        _BDK_,
        _WAK_,
        _ARK_,
        _CDK_,
    ]:
        r1 = self._update_blueprint(blueprint)
        r2 = self.health_increase.apply(r1)
        new_druid: DruidInfo[LevelOut] = DruidInfo[LevelOut].model_validate(
            {"prepared_spells": blueprint.druid.prepared_spells}
        )
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
            DruidInfo[LevelOut],
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(
            dict(r2)
            | {
                "druid": new_druid,
                "caster": blueprint.caster,
            }
        )
        after_spells = self.spell_assigner.apply(interim)
        new_caster = after_spells.caster.increase_full_caster()
        return after_spells.model_copy(update={"caster": new_caster})
