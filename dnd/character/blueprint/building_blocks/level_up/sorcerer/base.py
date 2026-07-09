from abc import ABC
from abc import abstractmethod
from typing import Literal

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.level_up.health_increase import (
    AnyHealthIncrease,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment.base import (
    SorcererSpellAssigner,
)
from dnd.character.blueprint.sentinels import AnyClassLevel
from dnd.character.blueprint.sentinels import AnySorcererLevel
from dnd.character.blueprint.sentinels import AnyStatChoices
from dnd.character.blueprint.sentinels import AnyWizardLevel
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.sentinels import FirstSubclassPreLevel
from dnd.character.blueprint.sentinels import MaybeCharacterData
from dnd.character.blueprint.sentinels import MaybeHealth
from dnd.character.blueprint.sentinels import MaybeRace
from dnd.character.blueprint.sentinels import MaybeStats
from dnd.character.blueprint.sentinels import SorcererPreSubclassLevel
from dnd.character.blueprint.sentinels import SorcererSubclassLevel
from dnd.character.blueprint.state import Blueprint
from dnd.character.blueprint.state import _BPT
from dnd.choices.class_creation.character_class import SorcererSubclass
from pydantic import PositiveInt


class SorcererLevel1Base[SubclassOut: SorcererSubclass](BuildingBlock, ABC):
    """Base for sorcerer level 1 (subclass-assigning level)."""

    health_increase: AnyHealthIncrease
    spell_assigner: SorcererSpellAssigner

    @abstractmethod
    def _update_blueprint(self, blueprint: _BPT) -> _BPT: ...

    def apply[
        _RK_: MaybeRace,
        _StK_: MaybeStats,
        _HeK_: MaybeHealth,
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WZK_: AnyWizardLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _DRK_: AnyClassLevel,
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
            _RK_,
            _StK_,
            _HeK_,
            _StCK_,
            _SkCK_,
            _WZK_,
            SorcererPreSubclassLevel[FirstSubclassPreLevel, None],
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ],
    ) -> Blueprint[
        _RK_,
        _StK_,
        PositiveInt,
        _StCK_,
        _SkCK_,
        _WZK_,
        SorcererSubclassLevel[Literal[FirstSubclassPostLevel.FIRST], SubclassOut],
        _FGK_,
        _BAK_,
        _ROK_,
        _CLK_,
        _DRK_,
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
        r3 = self.spell_assigner.apply(r2)
        return Blueprint[
            _RK_,
            _StK_,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WZK_,
            SorcererSubclassLevel[Literal[FirstSubclassPostLevel.FIRST], SubclassOut],
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(dict(r3))


class SorcererSharedLevelBase[
    LevelIn: FirstSubclassPostLevel,
    LevelOut: FirstSubclassPostLevel,
](BuildingBlock, ABC):
    """Base for post-subclass sorcerer levels shared across all subclasses."""

    health_increase: AnyHealthIncrease
    spell_assigner: SorcererSpellAssigner

    @abstractmethod
    def _update_blueprint(self, blueprint: _BPT) -> _BPT: ...

    def apply[
        SubclassT: SorcererSubclass,
        _RK_: MaybeRace,
        _StK_: MaybeStats,
        _HeK_: MaybeHealth,
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WZK_: AnyWizardLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _DRK_: AnyClassLevel,
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
            _RK_,
            _StK_,
            _HeK_,
            _StCK_,
            _SkCK_,
            _WZK_,
            SorcererSubclassLevel[LevelIn, SubclassT],
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ],
    ) -> Blueprint[
        _RK_,
        _StK_,
        PositiveInt,
        _StCK_,
        _SkCK_,
        _WZK_,
        SorcererSubclassLevel[LevelOut, SubclassT],
        _FGK_,
        _BAK_,
        _ROK_,
        _CLK_,
        _DRK_,
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
        r3 = self.spell_assigner.apply(r2)
        return Blueprint[
            _RK_,
            _StK_,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WZK_,
            SorcererSubclassLevel[LevelOut, SubclassT],
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(dict(r3))


class SorcererSubclassFeatureLevelBase[
    LevelIn: AnySorcererLevel,
    LevelOut: AnySorcererLevel,
](BuildingBlock, ABC):
    """Base for sorcerer levels 6, 14, 18 that grant subclass-specific features."""

    health_increase: AnyHealthIncrease
    spell_assigner: SorcererSpellAssigner

    @abstractmethod
    def _update_blueprint(self, blueprint: _BPT) -> _BPT: ...

    def apply[
        _RK_: MaybeRace,
        _StK_: MaybeStats,
        _HeK_: MaybeHealth,
        _StCK_: AnyStatChoices,
        _SkCK_: AnyStatChoices,
        _WZK_: AnyWizardLevel,
        _FGK_: AnyClassLevel,
        _BAK_: AnyClassLevel,
        _ROK_: AnyClassLevel,
        _CLK_: AnyClassLevel,
        _DRK_: AnyClassLevel,
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
            _RK_,
            _StK_,
            _HeK_,
            _StCK_,
            _SkCK_,
            _WZK_,
            LevelIn,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ],
    ) -> Blueprint[
        _RK_,
        _StK_,
        PositiveInt,
        _StCK_,
        _SkCK_,
        _WZK_,
        LevelOut,
        _FGK_,
        _BAK_,
        _ROK_,
        _CLK_,
        _DRK_,
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
        r3 = self.spell_assigner.apply(r2)
        return Blueprint[
            _RK_,
            _StK_,
            PositiveInt,
            _StCK_,
            _SkCK_,
            _WZK_,
            LevelOut,
            _FGK_,
            _BAK_,
            _ROK_,
            _CLK_,
            _DRK_,
            _PAK_,
            _RAK_,
            _MOK_,
            _BDK_,
            _WAK_,
            _ARK_,
            _CDK_,
        ].model_validate(dict(r3))
