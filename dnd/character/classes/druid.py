from __future__ import annotations

from abc import ABC
from dnd.character.classes.base import ClassLevelBase
from dnd.character.classes.base import Die
from dnd.character.classes.enums import Class
from dnd.character.classes.enums import DruidSubclass
from dnd.character.level import Level
from typing import TYPE_CHECKING
from typing import assert_never

if TYPE_CHECKING:
    from dnd.character.classes.modifier import ClassModifier


class DruidLevelBase(ClassLevelBase, ABC):
    class_ = Class.DRUID
    hit_die = Die.D8


class DruidLevel1(DruidLevelBase):
    number = Level.FIRST


class DruidLevel2(DruidLevelBase):
    number = Level.SECOND


class DruidLevel3(DruidLevelBase):
    number = Level.THIRD


class DruidLevel4(DruidLevelBase):
    number = Level.FOURTH


class DruidLevel5(DruidLevelBase):
    number = Level.FIFTH


class DruidLevel6(DruidLevelBase):
    number = Level.SIXTH


class DruidLevel7(DruidLevelBase):
    number = Level.SEVENTH


class DruidLevel8(DruidLevelBase):
    number = Level.EIGHTH


class DruidLevel9(DruidLevelBase):
    number = Level.NINTH


class DruidLevel10(DruidLevelBase):
    number = Level.TENTH


class DruidLevel11(DruidLevelBase):
    number = Level.ELEVENTH


class DruidLevel12(DruidLevelBase):
    number = Level.TWELFTH


class DruidLevel13(DruidLevelBase):
    number = Level.THIRTEENTH


class DruidLevel14(DruidLevelBase):
    number = Level.FOURTEENTH


class DruidLevel15(DruidLevelBase):
    number = Level.FIFTEENTH


class DruidLevel16(DruidLevelBase):
    number = Level.SIXTEENTH


class DruidLevel17(DruidLevelBase):
    number = Level.SEVENTEENTH


class DruidLevel18(DruidLevelBase):
    number = Level.EIGHTEENTH


class DruidLevel19(DruidLevelBase):
    number = Level.NINETEENTH


class DruidLevel20(DruidLevelBase):
    number = Level.TWENTIETH


class DruidSubclassField:
    def __get__(
        self, owner: ClassModifier | None, objtype: type | None = None
    ) -> DruidSubclass:
        if owner is None:
            return DruidSubclass.DREAMS
        return owner._druid_subclass

    def __set__(self, owner: ClassModifier, value: DruidSubclass) -> None:
        owner._druid_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: DruidSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return DruidLevel1()
            case Level.SECOND:
                return DruidLevel2()
            case Level.THIRD:
                return DruidLevel3()
            case Level.FOURTH:
                return DruidLevel4()
            case Level.FIFTH:
                return DruidLevel5()
            case Level.SIXTH:
                return DruidLevel6()
            case Level.SEVENTH:
                return DruidLevel7()
            case Level.EIGHTH:
                return DruidLevel8()
            case Level.NINTH:
                return DruidLevel9()
            case Level.TENTH:
                return DruidLevel10()
            case Level.ELEVENTH:
                return DruidLevel11()
            case Level.TWELFTH:
                return DruidLevel12()
            case Level.THIRTEENTH:
                return DruidLevel13()
            case Level.FOURTEENTH:
                return DruidLevel14()
            case Level.FIFTEENTH:
                return DruidLevel15()
            case Level.SIXTEENTH:
                return DruidLevel16()
            case Level.SEVENTEENTH:
                return DruidLevel17()
            case Level.EIGHTEENTH:
                return DruidLevel18()
            case Level.NINETEENTH:
                return DruidLevel19()
            case Level.TWENTIETH:
                return DruidLevel20()
            case _ as never:
                assert_never(never)
