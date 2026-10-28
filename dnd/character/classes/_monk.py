from __future__ import annotations

from abc import ABC
from dnd.character.classes._base import ClassLevelBase
from dnd.character.classes._base import Die
from dnd.character.classes._enums import Class
from dnd.character.classes._enums import MonkSubclass
from dnd.character.level import Level
from typing import Protocol
from typing import assert_never


class MonkLevelBase(ClassLevelBase, ABC):
    class_ = Class.MONK
    hit_die = Die.D8


class MonkLevel1(MonkLevelBase):
    number = Level.FIRST


class MonkLevel2(MonkLevelBase):
    number = Level.SECOND


class MonkLevel3(MonkLevelBase):
    number = Level.THIRD


class MonkLevel4(MonkLevelBase):
    number = Level.FOURTH


class MonkLevel5(MonkLevelBase):
    number = Level.FIFTH


class MonkLevel6(MonkLevelBase):
    number = Level.SIXTH


class MonkLevel7(MonkLevelBase):
    number = Level.SEVENTH


class MonkLevel8(MonkLevelBase):
    number = Level.EIGHTH


class MonkLevel9(MonkLevelBase):
    number = Level.NINTH


class MonkLevel10(MonkLevelBase):
    number = Level.TENTH


class MonkLevel11(MonkLevelBase):
    number = Level.ELEVENTH


class MonkLevel12(MonkLevelBase):
    number = Level.TWELFTH


class MonkLevel13(MonkLevelBase):
    number = Level.THIRTEENTH


class MonkLevel14(MonkLevelBase):
    number = Level.FOURTEENTH


class MonkLevel15(MonkLevelBase):
    number = Level.FIFTEENTH


class MonkLevel16(MonkLevelBase):
    number = Level.SIXTEENTH


class MonkLevel17(MonkLevelBase):
    number = Level.SEVENTEENTH


class MonkLevel18(MonkLevelBase):
    number = Level.EIGHTEENTH


class MonkLevel19(MonkLevelBase):
    number = Level.NINETEENTH


class MonkLevel20(MonkLevelBase):
    number = Level.TWENTIETH


class MonkOwner(Protocol):
    _levels: tuple[ClassLevelBase, ...]
    _monk_subclass: MonkSubclass


class MonkSubclassField:
    def __get__(
        self, owner: MonkOwner | None, _objtype: type | None = None
    ) -> MonkSubclass:
        if owner is None:
            return MonkSubclass.MERCY
        return owner._monk_subclass

    def __set__(self, owner: MonkOwner, value: MonkSubclass) -> None:
        owner._monk_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: MonkSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return MonkLevel1()
            case Level.SECOND:
                return MonkLevel2()
            case Level.THIRD:
                return MonkLevel3()
            case Level.FOURTH:
                return MonkLevel4()
            case Level.FIFTH:
                return MonkLevel5()
            case Level.SIXTH:
                return MonkLevel6()
            case Level.SEVENTH:
                return MonkLevel7()
            case Level.EIGHTH:
                return MonkLevel8()
            case Level.NINTH:
                return MonkLevel9()
            case Level.TENTH:
                return MonkLevel10()
            case Level.ELEVENTH:
                return MonkLevel11()
            case Level.TWELFTH:
                return MonkLevel12()
            case Level.THIRTEENTH:
                return MonkLevel13()
            case Level.FOURTEENTH:
                return MonkLevel14()
            case Level.FIFTEENTH:
                return MonkLevel15()
            case Level.SIXTEENTH:
                return MonkLevel16()
            case Level.SEVENTEENTH:
                return MonkLevel17()
            case Level.EIGHTEENTH:
                return MonkLevel18()
            case Level.NINETEENTH:
                return MonkLevel19()
            case Level.TWENTIETH:
                return MonkLevel20()
            case _ as never:
                assert_never(never)
