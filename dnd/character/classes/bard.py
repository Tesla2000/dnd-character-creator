from __future__ import annotations

from abc import ABC
from dnd.character.classes.base import ClassLevelBase
from dnd.character.classes.base import Die
from dnd.character.classes.enums import BardSubclass
from dnd.character.classes.enums import Class
from dnd.character.level import Level
from typing import TYPE_CHECKING
from typing import assert_never

if TYPE_CHECKING:
    from dnd.character.classes.modifier import ClassModifier


class BardLevelBase(ClassLevelBase, ABC):
    class_ = Class.BARD
    hit_die = Die.D8


class BardLevel1(BardLevelBase):
    number = Level.FIRST


class BardLevel2(BardLevelBase):
    number = Level.SECOND


class BardLevel3(BardLevelBase):
    number = Level.THIRD


class BardLevel4(BardLevelBase):
    number = Level.FOURTH


class BardLevel5(BardLevelBase):
    number = Level.FIFTH


class BardLevel6(BardLevelBase):
    number = Level.SIXTH


class BardLevel7(BardLevelBase):
    number = Level.SEVENTH


class BardLevel8(BardLevelBase):
    number = Level.EIGHTH


class BardLevel9(BardLevelBase):
    number = Level.NINTH


class BardLevel10(BardLevelBase):
    number = Level.TENTH


class BardLevel11(BardLevelBase):
    number = Level.ELEVENTH


class BardLevel12(BardLevelBase):
    number = Level.TWELFTH


class BardLevel13(BardLevelBase):
    number = Level.THIRTEENTH


class BardLevel14(BardLevelBase):
    number = Level.FOURTEENTH


class BardLevel15(BardLevelBase):
    number = Level.FIFTEENTH


class BardLevel16(BardLevelBase):
    number = Level.SIXTEENTH


class BardLevel17(BardLevelBase):
    number = Level.SEVENTEENTH


class BardLevel18(BardLevelBase):
    number = Level.EIGHTEENTH


class BardLevel19(BardLevelBase):
    number = Level.NINETEENTH


class BardLevel20(BardLevelBase):
    number = Level.TWENTIETH


class BardSubclassField:
    def __get__(
        self, owner: ClassModifier | None, objtype: type | None = None
    ) -> BardSubclass:
        if owner is None:
            return BardSubclass.CREATION
        return owner._bard_subclass

    def __set__(self, owner: ClassModifier, value: BardSubclass) -> None:
        owner._bard_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: BardSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return BardLevel1()
            case Level.SECOND:
                return BardLevel2()
            case Level.THIRD:
                return BardLevel3()
            case Level.FOURTH:
                return BardLevel4()
            case Level.FIFTH:
                return BardLevel5()
            case Level.SIXTH:
                return BardLevel6()
            case Level.SEVENTH:
                return BardLevel7()
            case Level.EIGHTH:
                return BardLevel8()
            case Level.NINTH:
                return BardLevel9()
            case Level.TENTH:
                return BardLevel10()
            case Level.ELEVENTH:
                return BardLevel11()
            case Level.TWELFTH:
                return BardLevel12()
            case Level.THIRTEENTH:
                return BardLevel13()
            case Level.FOURTEENTH:
                return BardLevel14()
            case Level.FIFTEENTH:
                return BardLevel15()
            case Level.SIXTEENTH:
                return BardLevel16()
            case Level.SEVENTEENTH:
                return BardLevel17()
            case Level.EIGHTEENTH:
                return BardLevel18()
            case Level.NINETEENTH:
                return BardLevel19()
            case Level.TWENTIETH:
                return BardLevel20()
            case _ as never:
                assert_never(never)
