from __future__ import annotations

from abc import ABC
from dnd.character.classes._base import ClassLevelBase
from dnd.character.classes._base import Die
from dnd.character.classes._enums import Class
from dnd.character.classes._enums import SorcererSubclass
from dnd.character.level import Level
from enum import StrEnum
from enum import auto
from pydantic import BaseModel
from pydantic import ConfigDict
from typing import ClassVar
from typing import Protocol
from typing import assert_never


class SorcererSlot(StrEnum):
    FIRST = auto()
    SIXTH = auto()
    FOURTEENTH = auto()
    EIGHTEENTH = auto()


class SorcererLevelBase(ClassLevelBase, ABC):
    class_ = Class.SORCERER
    hit_die = Die.D6


class SorcererSubclassLevelBase(SorcererLevelBase, ABC):
    """A sorcerer level that belongs to an origin, so it changes when the origin changes."""

    subclass: ClassVar[SorcererSubclass]
    slot: ClassVar[SorcererSlot]


class SorcererLevel2(SorcererLevelBase):
    number = Level.SECOND


class SorcererLevel3(SorcererLevelBase):
    number = Level.THIRD


class SorcererLevel4(SorcererLevelBase):
    number = Level.FOURTH


class SorcererLevel5(SorcererLevelBase):
    number = Level.FIFTH


class SorcererLevel7(SorcererLevelBase):
    number = Level.SEVENTH


class SorcererLevel8(SorcererLevelBase):
    number = Level.EIGHTH


class SorcererLevel9(SorcererLevelBase):
    number = Level.NINTH


class SorcererLevel10(SorcererLevelBase):
    number = Level.TENTH


class SorcererLevel11(SorcererLevelBase):
    number = Level.ELEVENTH


class SorcererLevel12(SorcererLevelBase):
    number = Level.TWELFTH


class SorcererLevel13(SorcererLevelBase):
    number = Level.THIRTEENTH


class SorcererLevel15(SorcererLevelBase):
    number = Level.FIFTEENTH


class SorcererLevel16(SorcererLevelBase):
    number = Level.SIXTEENTH


class SorcererLevel17(SorcererLevelBase):
    number = Level.SEVENTEENTH


class SorcererLevel19(SorcererLevelBase):
    number = Level.NINETEENTH


class SorcererLevel20(SorcererLevelBase):
    number = Level.TWENTIETH


class SorcererLevel1AberrantMind(SorcererSubclassLevelBase):
    number = Level.FIRST
    slot = SorcererSlot.FIRST
    subclass = SorcererSubclass.ABERRANT_MIND


class SorcererLevel6AberrantMind(SorcererSubclassLevelBase):
    number = Level.SIXTH
    slot = SorcererSlot.SIXTH
    subclass = SorcererSubclass.ABERRANT_MIND


class SorcererLevel14AberrantMind(SorcererSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = SorcererSlot.FOURTEENTH
    subclass = SorcererSubclass.ABERRANT_MIND


class SorcererLevel18AberrantMind(SorcererSubclassLevelBase):
    number = Level.EIGHTEENTH
    slot = SorcererSlot.EIGHTEENTH
    subclass = SorcererSubclass.ABERRANT_MIND


class SorcererLevel1ClockworkSoul(SorcererSubclassLevelBase):
    number = Level.FIRST
    slot = SorcererSlot.FIRST
    subclass = SorcererSubclass.CLOCKWORK_SOUL


class SorcererLevel6ClockworkSoul(SorcererSubclassLevelBase):
    number = Level.SIXTH
    slot = SorcererSlot.SIXTH
    subclass = SorcererSubclass.CLOCKWORK_SOUL


class SorcererLevel14ClockworkSoul(SorcererSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = SorcererSlot.FOURTEENTH
    subclass = SorcererSubclass.CLOCKWORK_SOUL


class SorcererLevel18ClockworkSoul(SorcererSubclassLevelBase):
    number = Level.EIGHTEENTH
    slot = SorcererSlot.EIGHTEENTH
    subclass = SorcererSubclass.CLOCKWORK_SOUL


class SorcererLevel1DraconicBloodline(SorcererSubclassLevelBase):
    number = Level.FIRST
    slot = SorcererSlot.FIRST
    subclass = SorcererSubclass.DRACONIC_BLOODLINE


class SorcererLevel6DraconicBloodline(SorcererSubclassLevelBase):
    number = Level.SIXTH
    slot = SorcererSlot.SIXTH
    subclass = SorcererSubclass.DRACONIC_BLOODLINE


class SorcererLevel14DraconicBloodline(SorcererSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = SorcererSlot.FOURTEENTH
    subclass = SorcererSubclass.DRACONIC_BLOODLINE


class SorcererLevel18DraconicBloodline(SorcererSubclassLevelBase):
    number = Level.EIGHTEENTH
    slot = SorcererSlot.EIGHTEENTH
    subclass = SorcererSubclass.DRACONIC_BLOODLINE


class SorcererLevel1DivineSoul(SorcererSubclassLevelBase):
    number = Level.FIRST
    slot = SorcererSlot.FIRST
    subclass = SorcererSubclass.DIVINE_SOUL


class SorcererLevel6DivineSoul(SorcererSubclassLevelBase):
    number = Level.SIXTH
    slot = SorcererSlot.SIXTH
    subclass = SorcererSubclass.DIVINE_SOUL


class SorcererLevel14DivineSoul(SorcererSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = SorcererSlot.FOURTEENTH
    subclass = SorcererSubclass.DIVINE_SOUL


class SorcererLevel18DivineSoul(SorcererSubclassLevelBase):
    number = Level.EIGHTEENTH
    slot = SorcererSlot.EIGHTEENTH
    subclass = SorcererSubclass.DIVINE_SOUL


class SorcererLevel1LunarSorcery(SorcererSubclassLevelBase):
    number = Level.FIRST
    slot = SorcererSlot.FIRST
    subclass = SorcererSubclass.LUNAR_SORCERY


class SorcererLevel6LunarSorcery(SorcererSubclassLevelBase):
    number = Level.SIXTH
    slot = SorcererSlot.SIXTH
    subclass = SorcererSubclass.LUNAR_SORCERY


class SorcererLevel14LunarSorcery(SorcererSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = SorcererSlot.FOURTEENTH
    subclass = SorcererSubclass.LUNAR_SORCERY


class SorcererLevel18LunarSorcery(SorcererSubclassLevelBase):
    number = Level.EIGHTEENTH
    slot = SorcererSlot.EIGHTEENTH
    subclass = SorcererSubclass.LUNAR_SORCERY


class SorcererLevel1ShadowMagic(SorcererSubclassLevelBase):
    number = Level.FIRST
    slot = SorcererSlot.FIRST
    subclass = SorcererSubclass.SHADOW_MAGIC


class SorcererLevel6ShadowMagic(SorcererSubclassLevelBase):
    number = Level.SIXTH
    slot = SorcererSlot.SIXTH
    subclass = SorcererSubclass.SHADOW_MAGIC


class SorcererLevel14ShadowMagic(SorcererSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = SorcererSlot.FOURTEENTH
    subclass = SorcererSubclass.SHADOW_MAGIC


class SorcererLevel18ShadowMagic(SorcererSubclassLevelBase):
    number = Level.EIGHTEENTH
    slot = SorcererSlot.EIGHTEENTH
    subclass = SorcererSubclass.SHADOW_MAGIC


class SorcererLevel1StormSorcery(SorcererSubclassLevelBase):
    number = Level.FIRST
    slot = SorcererSlot.FIRST
    subclass = SorcererSubclass.STORM_SORCERY


class SorcererLevel6StormSorcery(SorcererSubclassLevelBase):
    number = Level.SIXTH
    slot = SorcererSlot.SIXTH
    subclass = SorcererSubclass.STORM_SORCERY


class SorcererLevel14StormSorcery(SorcererSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = SorcererSlot.FOURTEENTH
    subclass = SorcererSubclass.STORM_SORCERY


class SorcererLevel18StormSorcery(SorcererSubclassLevelBase):
    number = Level.EIGHTEENTH
    slot = SorcererSlot.EIGHTEENTH
    subclass = SorcererSubclass.STORM_SORCERY


class SorcererLevel1WildMagic(SorcererSubclassLevelBase):
    number = Level.FIRST
    slot = SorcererSlot.FIRST
    subclass = SorcererSubclass.WILD_MAGIC


class SorcererLevel6WildMagic(SorcererSubclassLevelBase):
    number = Level.SIXTH
    slot = SorcererSlot.SIXTH
    subclass = SorcererSubclass.WILD_MAGIC


class SorcererLevel14WildMagic(SorcererSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = SorcererSlot.FOURTEENTH
    subclass = SorcererSubclass.WILD_MAGIC


class SorcererLevel18WildMagic(SorcererSubclassLevelBase):
    number = Level.EIGHTEENTH
    slot = SorcererSlot.EIGHTEENTH
    subclass = SorcererSubclass.WILD_MAGIC


class SorcererSchoolLevels(BaseModel):
    """The four level classes a sorcerer origin provides, at levels 1, 6, 14 and 18."""

    model_config = ConfigDict(frozen=True)

    first: type[SorcererSubclassLevelBase]
    sixth: type[SorcererSubclassLevelBase]
    fourteenth: type[SorcererSubclassLevelBase]
    eighteenth: type[SorcererSubclassLevelBase]


class SorcererOwner(Protocol):
    _levels: tuple[ClassLevelBase, ...]
    _sorcerer_subclass: SorcererSubclass


class SorcererSubclassField:
    def __get__(
        self, owner: SorcererOwner | None, _objtype: type | None = None
    ) -> SorcererSubclass:
        if owner is None:
            return SorcererSubclass.ABERRANT_MIND
        return owner._sorcerer_subclass

    def __set__(self, owner: SorcererOwner, value: SorcererSubclass) -> None:
        owner._sorcerer_subclass = value
        owner._levels = tuple(
            self._subclass_level(level.slot, value)
            if isinstance(level, SorcererSubclassLevelBase)
            else level
            for level in owner._levels
        )

    @classmethod
    def _subclass_level(
        cls, slot: SorcererSlot, subclass: SorcererSubclass
    ) -> SorcererSubclassLevelBase:
        levels = cls.school_levels(subclass)
        match slot:
            case SorcererSlot.FIRST:
                return levels.first()
            case SorcererSlot.SIXTH:
                return levels.sixth()
            case SorcererSlot.FOURTEENTH:
                return levels.fourteenth()
            case SorcererSlot.EIGHTEENTH:
                return levels.eighteenth()
            case _ as never:
                assert_never(never)

    @classmethod
    def school_levels(cls, subclass: SorcererSubclass) -> SorcererSchoolLevels:
        match subclass:
            case SorcererSubclass.ABERRANT_MIND:
                return SorcererSchoolLevels(
                    first=SorcererLevel1AberrantMind,
                    sixth=SorcererLevel6AberrantMind,
                    fourteenth=SorcererLevel14AberrantMind,
                    eighteenth=SorcererLevel18AberrantMind,
                )
            case SorcererSubclass.CLOCKWORK_SOUL:
                return SorcererSchoolLevels(
                    first=SorcererLevel1ClockworkSoul,
                    sixth=SorcererLevel6ClockworkSoul,
                    fourteenth=SorcererLevel14ClockworkSoul,
                    eighteenth=SorcererLevel18ClockworkSoul,
                )
            case SorcererSubclass.DRACONIC_BLOODLINE:
                return SorcererSchoolLevels(
                    first=SorcererLevel1DraconicBloodline,
                    sixth=SorcererLevel6DraconicBloodline,
                    fourteenth=SorcererLevel14DraconicBloodline,
                    eighteenth=SorcererLevel18DraconicBloodline,
                )
            case SorcererSubclass.DIVINE_SOUL:
                return SorcererSchoolLevels(
                    first=SorcererLevel1DivineSoul,
                    sixth=SorcererLevel6DivineSoul,
                    fourteenth=SorcererLevel14DivineSoul,
                    eighteenth=SorcererLevel18DivineSoul,
                )
            case SorcererSubclass.LUNAR_SORCERY:
                return SorcererSchoolLevels(
                    first=SorcererLevel1LunarSorcery,
                    sixth=SorcererLevel6LunarSorcery,
                    fourteenth=SorcererLevel14LunarSorcery,
                    eighteenth=SorcererLevel18LunarSorcery,
                )
            case SorcererSubclass.SHADOW_MAGIC:
                return SorcererSchoolLevels(
                    first=SorcererLevel1ShadowMagic,
                    sixth=SorcererLevel6ShadowMagic,
                    fourteenth=SorcererLevel14ShadowMagic,
                    eighteenth=SorcererLevel18ShadowMagic,
                )
            case SorcererSubclass.STORM_SORCERY:
                return SorcererSchoolLevels(
                    first=SorcererLevel1StormSorcery,
                    sixth=SorcererLevel6StormSorcery,
                    fourteenth=SorcererLevel14StormSorcery,
                    eighteenth=SorcererLevel18StormSorcery,
                )
            case SorcererSubclass.WILD_MAGIC:
                return SorcererSchoolLevels(
                    first=SorcererLevel1WildMagic,
                    sixth=SorcererLevel6WildMagic,
                    fourteenth=SorcererLevel14WildMagic,
                    eighteenth=SorcererLevel18WildMagic,
                )
            case _ as never:
                assert_never(never)

    @classmethod
    def level(cls, number: Level, subclass: SorcererSubclass) -> ClassLevelBase:
        match number:
            case Level.FIRST:
                return cls.school_levels(subclass).first()
            case Level.SECOND:
                return SorcererLevel2()
            case Level.THIRD:
                return SorcererLevel3()
            case Level.FOURTH:
                return SorcererLevel4()
            case Level.FIFTH:
                return SorcererLevel5()
            case Level.SIXTH:
                return cls.school_levels(subclass).sixth()
            case Level.SEVENTH:
                return SorcererLevel7()
            case Level.EIGHTH:
                return SorcererLevel8()
            case Level.NINTH:
                return SorcererLevel9()
            case Level.TENTH:
                return SorcererLevel10()
            case Level.ELEVENTH:
                return SorcererLevel11()
            case Level.TWELFTH:
                return SorcererLevel12()
            case Level.THIRTEENTH:
                return SorcererLevel13()
            case Level.FOURTEENTH:
                return cls.school_levels(subclass).fourteenth()
            case Level.FIFTEENTH:
                return SorcererLevel15()
            case Level.SIXTEENTH:
                return SorcererLevel16()
            case Level.SEVENTEENTH:
                return SorcererLevel17()
            case Level.EIGHTEENTH:
                return cls.school_levels(subclass).eighteenth()
            case Level.NINETEENTH:
                return SorcererLevel19()
            case Level.TWENTIETH:
                return SorcererLevel20()
            case _ as never:
                assert_never(never)
