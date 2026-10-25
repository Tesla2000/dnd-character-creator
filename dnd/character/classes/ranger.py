from __future__ import annotations

from abc import ABC
from dnd.character.classes.base import ClassLevelBase
from dnd.character.classes.base import Die
from dnd.character.classes.enums import Class
from dnd.character.classes.enums import RangerSubclass
from dnd.character.level import Level
from typing import TYPE_CHECKING
from typing import assert_never

if TYPE_CHECKING:
    from dnd.character.classes.modifier import ClassModifier


class RangerLevelBase(ClassLevelBase, ABC):
    class_ = Class.RANGER
    hit_die = Die.D10


class RangerLevel1(RangerLevelBase):
    number = Level.FIRST


class RangerLevel2(RangerLevelBase):
    number = Level.SECOND


class RangerLevel3(RangerLevelBase):
    number = Level.THIRD


class RangerLevel4(RangerLevelBase):
    number = Level.FOURTH


class RangerLevel5(RangerLevelBase):
    number = Level.FIFTH


class RangerLevel6(RangerLevelBase):
    number = Level.SIXTH


class RangerLevel7(RangerLevelBase):
    number = Level.SEVENTH


class RangerLevel8(RangerLevelBase):
    number = Level.EIGHTH


class RangerLevel9(RangerLevelBase):
    number = Level.NINTH


class RangerLevel10(RangerLevelBase):
    number = Level.TENTH


class RangerLevel11(RangerLevelBase):
    number = Level.ELEVENTH


class RangerLevel12(RangerLevelBase):
    number = Level.TWELFTH


class RangerLevel13(RangerLevelBase):
    number = Level.THIRTEENTH


class RangerLevel14(RangerLevelBase):
    number = Level.FOURTEENTH


class RangerLevel15(RangerLevelBase):
    number = Level.FIFTEENTH


class RangerLevel16(RangerLevelBase):
    number = Level.SIXTEENTH


class RangerLevel17(RangerLevelBase):
    number = Level.SEVENTEENTH


class RangerLevel18(RangerLevelBase):
    number = Level.EIGHTEENTH


class RangerLevel19(RangerLevelBase):
    number = Level.NINETEENTH


class RangerLevel20(RangerLevelBase):
    number = Level.TWENTIETH


class RangerSubclassField:
    def __get__(
        self, owner: ClassModifier | None, objtype: type | None = None
    ) -> RangerSubclass:
        if owner is None:
            return RangerSubclass.BEAST_MASTER
        return owner._ranger_subclass

    def __set__(self, owner: ClassModifier, value: RangerSubclass) -> None:
        owner._ranger_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: RangerSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return RangerLevel1()
            case Level.SECOND:
                return RangerLevel2()
            case Level.THIRD:
                return RangerLevel3()
            case Level.FOURTH:
                return RangerLevel4()
            case Level.FIFTH:
                return RangerLevel5()
            case Level.SIXTH:
                return RangerLevel6()
            case Level.SEVENTH:
                return RangerLevel7()
            case Level.EIGHTH:
                return RangerLevel8()
            case Level.NINTH:
                return RangerLevel9()
            case Level.TENTH:
                return RangerLevel10()
            case Level.ELEVENTH:
                return RangerLevel11()
            case Level.TWELFTH:
                return RangerLevel12()
            case Level.THIRTEENTH:
                return RangerLevel13()
            case Level.FOURTEENTH:
                return RangerLevel14()
            case Level.FIFTEENTH:
                return RangerLevel15()
            case Level.SIXTEENTH:
                return RangerLevel16()
            case Level.SEVENTEENTH:
                return RangerLevel17()
            case Level.EIGHTEENTH:
                return RangerLevel18()
            case Level.NINETEENTH:
                return RangerLevel19()
            case Level.TWENTIETH:
                return RangerLevel20()
            case _ as never:
                assert_never(never)
