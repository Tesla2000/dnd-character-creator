from __future__ import annotations

from abc import ABC
from dnd.character.classes._base import ClassLevelBase
from dnd.character.classes._base import Die
from dnd.character.classes._enums import Class
from dnd.character.classes._enums import WarlockSubclass
from dnd.character.level import Level
from typing import Protocol
from typing import assert_never


class WarlockLevelBase(ClassLevelBase, ABC):
    class_ = Class.WARLOCK
    hit_die = Die.D8


class WarlockLevel1(WarlockLevelBase):
    number = Level.FIRST


class WarlockLevel2(WarlockLevelBase):
    number = Level.SECOND


class WarlockLevel3(WarlockLevelBase):
    number = Level.THIRD


class WarlockLevel4(WarlockLevelBase):
    number = Level.FOURTH


class WarlockLevel5(WarlockLevelBase):
    number = Level.FIFTH


class WarlockLevel6(WarlockLevelBase):
    number = Level.SIXTH


class WarlockLevel7(WarlockLevelBase):
    number = Level.SEVENTH


class WarlockLevel8(WarlockLevelBase):
    number = Level.EIGHTH


class WarlockLevel9(WarlockLevelBase):
    number = Level.NINTH


class WarlockLevel10(WarlockLevelBase):
    number = Level.TENTH


class WarlockLevel11(WarlockLevelBase):
    number = Level.ELEVENTH


class WarlockLevel12(WarlockLevelBase):
    number = Level.TWELFTH


class WarlockLevel13(WarlockLevelBase):
    number = Level.THIRTEENTH


class WarlockLevel14(WarlockLevelBase):
    number = Level.FOURTEENTH


class WarlockLevel15(WarlockLevelBase):
    number = Level.FIFTEENTH


class WarlockLevel16(WarlockLevelBase):
    number = Level.SIXTEENTH


class WarlockLevel17(WarlockLevelBase):
    number = Level.SEVENTEENTH


class WarlockLevel18(WarlockLevelBase):
    number = Level.EIGHTEENTH


class WarlockLevel19(WarlockLevelBase):
    number = Level.NINETEENTH


class WarlockLevel20(WarlockLevelBase):
    number = Level.TWENTIETH


class WarlockOwner(Protocol):
    _levels: tuple[ClassLevelBase, ...]
    _warlock_subclass: WarlockSubclass


class WarlockSubclassField:
    def __get__(
        self, owner: WarlockOwner | None, _objtype: type | None = None
    ) -> WarlockSubclass:
        if owner is None:
            return WarlockSubclass.ARCHFEY
        return owner._warlock_subclass

    def __set__(self, owner: WarlockOwner, value: WarlockSubclass) -> None:
        owner._warlock_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: WarlockSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return WarlockLevel1()
            case Level.SECOND:
                return WarlockLevel2()
            case Level.THIRD:
                return WarlockLevel3()
            case Level.FOURTH:
                return WarlockLevel4()
            case Level.FIFTH:
                return WarlockLevel5()
            case Level.SIXTH:
                return WarlockLevel6()
            case Level.SEVENTH:
                return WarlockLevel7()
            case Level.EIGHTH:
                return WarlockLevel8()
            case Level.NINTH:
                return WarlockLevel9()
            case Level.TENTH:
                return WarlockLevel10()
            case Level.ELEVENTH:
                return WarlockLevel11()
            case Level.TWELFTH:
                return WarlockLevel12()
            case Level.THIRTEENTH:
                return WarlockLevel13()
            case Level.FOURTEENTH:
                return WarlockLevel14()
            case Level.FIFTEENTH:
                return WarlockLevel15()
            case Level.SIXTEENTH:
                return WarlockLevel16()
            case Level.SEVENTEENTH:
                return WarlockLevel17()
            case Level.EIGHTEENTH:
                return WarlockLevel18()
            case Level.NINETEENTH:
                return WarlockLevel19()
            case Level.TWENTIETH:
                return WarlockLevel20()
            case _ as never:
                assert_never(never)
