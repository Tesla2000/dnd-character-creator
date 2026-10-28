from __future__ import annotations

from abc import ABC
from dnd.character.classes._base import ClassLevelBase
from dnd.character.classes._base import Die
from dnd.character.classes._enums import BarbarianSubclass
from dnd.character.classes._enums import Class
from dnd.character.level import Level
from enum import StrEnum
from enum import auto
from pydantic import BaseModel
from pydantic import ConfigDict
from typing import ClassVar
from typing import Protocol
from typing import assert_never


class BarbarianSlot(StrEnum):
    THIRD = auto()
    SIXTH = auto()
    TENTH = auto()
    FOURTEENTH = auto()


class BarbarianLevelBase(ClassLevelBase, ABC):
    class_ = Class.BARBARIAN
    hit_die = Die.D12


class BarbarianSubclassLevelBase(BarbarianLevelBase, ABC):
    """A barbarian level that belongs to a path, so it changes when the path changes."""

    subclass: ClassVar[BarbarianSubclass]
    slot: ClassVar[BarbarianSlot]


class BarbarianLevel1(BarbarianLevelBase):
    number = Level.FIRST


class BarbarianLevel2(BarbarianLevelBase):
    number = Level.SECOND


class BarbarianLevel4(BarbarianLevelBase):
    number = Level.FOURTH


class BarbarianLevel5(BarbarianLevelBase):
    number = Level.FIFTH


class BarbarianLevel7(BarbarianLevelBase):
    number = Level.SEVENTH


class BarbarianLevel8(BarbarianLevelBase):
    number = Level.EIGHTH


class BarbarianLevel9(BarbarianLevelBase):
    number = Level.NINTH


class BarbarianLevel11(BarbarianLevelBase):
    number = Level.ELEVENTH


class BarbarianLevel12(BarbarianLevelBase):
    number = Level.TWELFTH


class BarbarianLevel13(BarbarianLevelBase):
    number = Level.THIRTEENTH


class BarbarianLevel15(BarbarianLevelBase):
    number = Level.FIFTEENTH


class BarbarianLevel16(BarbarianLevelBase):
    number = Level.SIXTEENTH


class BarbarianLevel17(BarbarianLevelBase):
    number = Level.SEVENTEENTH


class BarbarianLevel18(BarbarianLevelBase):
    number = Level.EIGHTEENTH


class BarbarianLevel19(BarbarianLevelBase):
    number = Level.NINETEENTH


class BarbarianLevel20(BarbarianLevelBase):
    number = Level.TWENTIETH


class BarbarianLevel3AncestralGuardian(BarbarianSubclassLevelBase):
    number = Level.THIRD
    slot = BarbarianSlot.THIRD
    subclass = BarbarianSubclass.ANCESTRAL_GUARDIAN


class BarbarianLevel6AncestralGuardian(BarbarianSubclassLevelBase):
    number = Level.SIXTH
    slot = BarbarianSlot.SIXTH
    subclass = BarbarianSubclass.ANCESTRAL_GUARDIAN


class BarbarianLevel10AncestralGuardian(BarbarianSubclassLevelBase):
    number = Level.TENTH
    slot = BarbarianSlot.TENTH
    subclass = BarbarianSubclass.ANCESTRAL_GUARDIAN


class BarbarianLevel14AncestralGuardian(BarbarianSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = BarbarianSlot.FOURTEENTH
    subclass = BarbarianSubclass.ANCESTRAL_GUARDIAN


class BarbarianLevel3Battlerager(BarbarianSubclassLevelBase):
    number = Level.THIRD
    slot = BarbarianSlot.THIRD
    subclass = BarbarianSubclass.BATTLERAGER


class BarbarianLevel6Battlerager(BarbarianSubclassLevelBase):
    number = Level.SIXTH
    slot = BarbarianSlot.SIXTH
    subclass = BarbarianSubclass.BATTLERAGER


class BarbarianLevel10Battlerager(BarbarianSubclassLevelBase):
    number = Level.TENTH
    slot = BarbarianSlot.TENTH
    subclass = BarbarianSubclass.BATTLERAGER


class BarbarianLevel14Battlerager(BarbarianSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = BarbarianSlot.FOURTEENTH
    subclass = BarbarianSubclass.BATTLERAGER


class BarbarianLevel3Beast(BarbarianSubclassLevelBase):
    number = Level.THIRD
    slot = BarbarianSlot.THIRD
    subclass = BarbarianSubclass.BEAST


class BarbarianLevel6Beast(BarbarianSubclassLevelBase):
    number = Level.SIXTH
    slot = BarbarianSlot.SIXTH
    subclass = BarbarianSubclass.BEAST


class BarbarianLevel10Beast(BarbarianSubclassLevelBase):
    number = Level.TENTH
    slot = BarbarianSlot.TENTH
    subclass = BarbarianSubclass.BEAST


class BarbarianLevel14Beast(BarbarianSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = BarbarianSlot.FOURTEENTH
    subclass = BarbarianSubclass.BEAST


class BarbarianLevel3Berserker(BarbarianSubclassLevelBase):
    number = Level.THIRD
    slot = BarbarianSlot.THIRD
    subclass = BarbarianSubclass.BERSERKER


class BarbarianLevel6Berserker(BarbarianSubclassLevelBase):
    number = Level.SIXTH
    slot = BarbarianSlot.SIXTH
    subclass = BarbarianSubclass.BERSERKER


class BarbarianLevel10Berserker(BarbarianSubclassLevelBase):
    number = Level.TENTH
    slot = BarbarianSlot.TENTH
    subclass = BarbarianSubclass.BERSERKER


class BarbarianLevel14Berserker(BarbarianSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = BarbarianSlot.FOURTEENTH
    subclass = BarbarianSubclass.BERSERKER


class BarbarianLevel3Giant(BarbarianSubclassLevelBase):
    number = Level.THIRD
    slot = BarbarianSlot.THIRD
    subclass = BarbarianSubclass.GIANT


class BarbarianLevel6Giant(BarbarianSubclassLevelBase):
    number = Level.SIXTH
    slot = BarbarianSlot.SIXTH
    subclass = BarbarianSubclass.GIANT


class BarbarianLevel10Giant(BarbarianSubclassLevelBase):
    number = Level.TENTH
    slot = BarbarianSlot.TENTH
    subclass = BarbarianSubclass.GIANT


class BarbarianLevel14Giant(BarbarianSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = BarbarianSlot.FOURTEENTH
    subclass = BarbarianSubclass.GIANT


class BarbarianLevel3StormHerald(BarbarianSubclassLevelBase):
    number = Level.THIRD
    slot = BarbarianSlot.THIRD
    subclass = BarbarianSubclass.STORM_HERALD


class BarbarianLevel6StormHerald(BarbarianSubclassLevelBase):
    number = Level.SIXTH
    slot = BarbarianSlot.SIXTH
    subclass = BarbarianSubclass.STORM_HERALD


class BarbarianLevel10StormHerald(BarbarianSubclassLevelBase):
    number = Level.TENTH
    slot = BarbarianSlot.TENTH
    subclass = BarbarianSubclass.STORM_HERALD


class BarbarianLevel14StormHerald(BarbarianSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = BarbarianSlot.FOURTEENTH
    subclass = BarbarianSubclass.STORM_HERALD


class BarbarianLevel3TotemWarrior(BarbarianSubclassLevelBase):
    number = Level.THIRD
    slot = BarbarianSlot.THIRD
    subclass = BarbarianSubclass.TOTEM_WARRIOR


class BarbarianLevel6TotemWarrior(BarbarianSubclassLevelBase):
    number = Level.SIXTH
    slot = BarbarianSlot.SIXTH
    subclass = BarbarianSubclass.TOTEM_WARRIOR


class BarbarianLevel10TotemWarrior(BarbarianSubclassLevelBase):
    number = Level.TENTH
    slot = BarbarianSlot.TENTH
    subclass = BarbarianSubclass.TOTEM_WARRIOR


class BarbarianLevel14TotemWarrior(BarbarianSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = BarbarianSlot.FOURTEENTH
    subclass = BarbarianSubclass.TOTEM_WARRIOR


class BarbarianLevel3WildMagic(BarbarianSubclassLevelBase):
    number = Level.THIRD
    slot = BarbarianSlot.THIRD
    subclass = BarbarianSubclass.WILD_MAGIC


class BarbarianLevel6WildMagic(BarbarianSubclassLevelBase):
    number = Level.SIXTH
    slot = BarbarianSlot.SIXTH
    subclass = BarbarianSubclass.WILD_MAGIC


class BarbarianLevel10WildMagic(BarbarianSubclassLevelBase):
    number = Level.TENTH
    slot = BarbarianSlot.TENTH
    subclass = BarbarianSubclass.WILD_MAGIC


class BarbarianLevel14WildMagic(BarbarianSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = BarbarianSlot.FOURTEENTH
    subclass = BarbarianSubclass.WILD_MAGIC


class BarbarianLevel3Zealot(BarbarianSubclassLevelBase):
    number = Level.THIRD
    slot = BarbarianSlot.THIRD
    subclass = BarbarianSubclass.ZEALOT


class BarbarianLevel6Zealot(BarbarianSubclassLevelBase):
    number = Level.SIXTH
    slot = BarbarianSlot.SIXTH
    subclass = BarbarianSubclass.ZEALOT


class BarbarianLevel10Zealot(BarbarianSubclassLevelBase):
    number = Level.TENTH
    slot = BarbarianSlot.TENTH
    subclass = BarbarianSubclass.ZEALOT


class BarbarianLevel14Zealot(BarbarianSubclassLevelBase):
    number = Level.FOURTEENTH
    slot = BarbarianSlot.FOURTEENTH
    subclass = BarbarianSubclass.ZEALOT


class BarbarianSchoolLevels(BaseModel):
    """The four level classes a barbarian path provides, at levels 3, 6, 10 and 14."""

    model_config = ConfigDict(frozen=True)

    third: type[BarbarianSubclassLevelBase]
    sixth: type[BarbarianSubclassLevelBase]
    tenth: type[BarbarianSubclassLevelBase]
    fourteenth: type[BarbarianSubclassLevelBase]


class BarbarianOwner(Protocol):
    _levels: tuple[ClassLevelBase, ...]
    _barbarian_subclass: BarbarianSubclass


class BarbarianSubclassField:
    def __get__(
        self, owner: BarbarianOwner | None, _objtype: type | None = None
    ) -> BarbarianSubclass:
        if owner is None:
            return BarbarianSubclass.ANCESTRAL_GUARDIAN
        return owner._barbarian_subclass

    def __set__(self, owner: BarbarianOwner, value: BarbarianSubclass) -> None:
        owner._barbarian_subclass = value
        owner._levels = tuple(
            self._subclass_level(level.slot, value)
            if isinstance(level, BarbarianSubclassLevelBase)
            else level
            for level in owner._levels
        )

    @classmethod
    def _subclass_level(
        cls, slot: BarbarianSlot, subclass: BarbarianSubclass
    ) -> BarbarianSubclassLevelBase:
        levels = cls.school_levels(subclass)
        match slot:
            case BarbarianSlot.THIRD:
                return levels.third()
            case BarbarianSlot.SIXTH:
                return levels.sixth()
            case BarbarianSlot.TENTH:
                return levels.tenth()
            case BarbarianSlot.FOURTEENTH:
                return levels.fourteenth()
            case _ as never:
                assert_never(never)

    @classmethod
    def school_levels(cls, subclass: BarbarianSubclass) -> BarbarianSchoolLevels:
        match subclass:
            case BarbarianSubclass.ANCESTRAL_GUARDIAN:
                return BarbarianSchoolLevels(
                    third=BarbarianLevel3AncestralGuardian,
                    sixth=BarbarianLevel6AncestralGuardian,
                    tenth=BarbarianLevel10AncestralGuardian,
                    fourteenth=BarbarianLevel14AncestralGuardian,
                )
            case BarbarianSubclass.BATTLERAGER:
                return BarbarianSchoolLevels(
                    third=BarbarianLevel3Battlerager,
                    sixth=BarbarianLevel6Battlerager,
                    tenth=BarbarianLevel10Battlerager,
                    fourteenth=BarbarianLevel14Battlerager,
                )
            case BarbarianSubclass.BEAST:
                return BarbarianSchoolLevels(
                    third=BarbarianLevel3Beast,
                    sixth=BarbarianLevel6Beast,
                    tenth=BarbarianLevel10Beast,
                    fourteenth=BarbarianLevel14Beast,
                )
            case BarbarianSubclass.BERSERKER:
                return BarbarianSchoolLevels(
                    third=BarbarianLevel3Berserker,
                    sixth=BarbarianLevel6Berserker,
                    tenth=BarbarianLevel10Berserker,
                    fourteenth=BarbarianLevel14Berserker,
                )
            case BarbarianSubclass.GIANT:
                return BarbarianSchoolLevels(
                    third=BarbarianLevel3Giant,
                    sixth=BarbarianLevel6Giant,
                    tenth=BarbarianLevel10Giant,
                    fourteenth=BarbarianLevel14Giant,
                )
            case BarbarianSubclass.STORM_HERALD:
                return BarbarianSchoolLevels(
                    third=BarbarianLevel3StormHerald,
                    sixth=BarbarianLevel6StormHerald,
                    tenth=BarbarianLevel10StormHerald,
                    fourteenth=BarbarianLevel14StormHerald,
                )
            case BarbarianSubclass.TOTEM_WARRIOR:
                return BarbarianSchoolLevels(
                    third=BarbarianLevel3TotemWarrior,
                    sixth=BarbarianLevel6TotemWarrior,
                    tenth=BarbarianLevel10TotemWarrior,
                    fourteenth=BarbarianLevel14TotemWarrior,
                )
            case BarbarianSubclass.WILD_MAGIC:
                return BarbarianSchoolLevels(
                    third=BarbarianLevel3WildMagic,
                    sixth=BarbarianLevel6WildMagic,
                    tenth=BarbarianLevel10WildMagic,
                    fourteenth=BarbarianLevel14WildMagic,
                )
            case BarbarianSubclass.ZEALOT:
                return BarbarianSchoolLevels(
                    third=BarbarianLevel3Zealot,
                    sixth=BarbarianLevel6Zealot,
                    tenth=BarbarianLevel10Zealot,
                    fourteenth=BarbarianLevel14Zealot,
                )
            case _ as never:
                assert_never(never)

    @classmethod
    def level(cls, number: Level, subclass: BarbarianSubclass) -> ClassLevelBase:
        match number:
            case Level.FIRST:
                return BarbarianLevel1()
            case Level.SECOND:
                return BarbarianLevel2()
            case Level.THIRD:
                return cls.school_levels(subclass).third()
            case Level.FOURTH:
                return BarbarianLevel4()
            case Level.FIFTH:
                return BarbarianLevel5()
            case Level.SIXTH:
                return cls.school_levels(subclass).sixth()
            case Level.SEVENTH:
                return BarbarianLevel7()
            case Level.EIGHTH:
                return BarbarianLevel8()
            case Level.NINTH:
                return BarbarianLevel9()
            case Level.TENTH:
                return cls.school_levels(subclass).tenth()
            case Level.ELEVENTH:
                return BarbarianLevel11()
            case Level.TWELFTH:
                return BarbarianLevel12()
            case Level.THIRTEENTH:
                return BarbarianLevel13()
            case Level.FOURTEENTH:
                return cls.school_levels(subclass).fourteenth()
            case Level.FIFTEENTH:
                return BarbarianLevel15()
            case Level.SIXTEENTH:
                return BarbarianLevel16()
            case Level.SEVENTEENTH:
                return BarbarianLevel17()
            case Level.EIGHTEENTH:
                return BarbarianLevel18()
            case Level.NINETEENTH:
                return BarbarianLevel19()
            case Level.TWENTIETH:
                return BarbarianLevel20()
            case _ as never:
                assert_never(never)
