from __future__ import annotations

from abc import ABC
from dnd.character.classes._base import ClassLevelBase
from dnd.character.classes._base import Die
from dnd.character.classes._enums import Class
from dnd.character.classes._enums import FighterSubclass
from dnd.character.level import Level
from typing import Protocol
from typing import assert_never


class FighterLevelBase(ClassLevelBase, ABC):
    class_ = Class.FIGHTER
    hit_die = Die.D10


class FighterLevel1(FighterLevelBase):
    number = Level.FIRST


class FighterLevel2(FighterLevelBase):
    number = Level.SECOND


class FighterLevel3(FighterLevelBase):
    number = Level.THIRD


class FighterLevel4(FighterLevelBase):
    number = Level.FOURTH


class FighterLevel5(FighterLevelBase):
    number = Level.FIFTH


class FighterLevel6(FighterLevelBase):
    number = Level.SIXTH


class FighterLevel7(FighterLevelBase):
    number = Level.SEVENTH


class FighterLevel8(FighterLevelBase):
    number = Level.EIGHTH


class FighterLevel9(FighterLevelBase):
    number = Level.NINTH


class FighterLevel10(FighterLevelBase):
    number = Level.TENTH


class FighterLevel11(FighterLevelBase):
    number = Level.ELEVENTH


class FighterLevel12(FighterLevelBase):
    number = Level.TWELFTH


class FighterLevel13(FighterLevelBase):
    number = Level.THIRTEENTH


class FighterLevel14(FighterLevelBase):
    number = Level.FOURTEENTH


class FighterLevel15(FighterLevelBase):
    number = Level.FIFTEENTH


class FighterLevel16(FighterLevelBase):
    number = Level.SIXTEENTH


class FighterLevel17(FighterLevelBase):
    number = Level.SEVENTEENTH


class FighterLevel18(FighterLevelBase):
    number = Level.EIGHTEENTH


class FighterLevel19(FighterLevelBase):
    number = Level.NINETEENTH


class FighterLevel20(FighterLevelBase):
    number = Level.TWENTIETH


class FighterOwner(Protocol):
    _levels: tuple[ClassLevelBase, ...]
    _fighter_subclass: FighterSubclass


class FighterSubclassField:
    def __get__(
        self, owner: FighterOwner | None, _objtype: type | None = None
    ) -> FighterSubclass:
        if owner is None:
            return FighterSubclass.ARCANE_ARCHER
        return owner._fighter_subclass

    def __set__(self, owner: FighterOwner, value: FighterSubclass) -> None:
        owner._fighter_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: FighterSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return FighterLevel1()
            case Level.SECOND:
                return FighterLevel2()
            case Level.THIRD:
                return FighterLevel3()
            case Level.FOURTH:
                return FighterLevel4()
            case Level.FIFTH:
                return FighterLevel5()
            case Level.SIXTH:
                return FighterLevel6()
            case Level.SEVENTH:
                return FighterLevel7()
            case Level.EIGHTH:
                return FighterLevel8()
            case Level.NINTH:
                return FighterLevel9()
            case Level.TENTH:
                return FighterLevel10()
            case Level.ELEVENTH:
                return FighterLevel11()
            case Level.TWELFTH:
                return FighterLevel12()
            case Level.THIRTEENTH:
                return FighterLevel13()
            case Level.FOURTEENTH:
                return FighterLevel14()
            case Level.FIFTEENTH:
                return FighterLevel15()
            case Level.SIXTEENTH:
                return FighterLevel16()
            case Level.SEVENTEENTH:
                return FighterLevel17()
            case Level.EIGHTEENTH:
                return FighterLevel18()
            case Level.NINETEENTH:
                return FighterLevel19()
            case Level.TWENTIETH:
                return FighterLevel20()
            case _ as never:
                assert_never(never)
