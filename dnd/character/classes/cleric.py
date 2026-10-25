from __future__ import annotations

from abc import ABC
from dnd.character.classes.base import ClassLevelBase
from dnd.character.classes.base import Die
from dnd.character.classes.enums import Class
from dnd.character.classes.enums import ClericSubclass
from dnd.character.level import Level
from typing import TYPE_CHECKING
from typing import assert_never

if TYPE_CHECKING:
    from dnd.character.classes.modifier import ClassModifier


class ClericLevelBase(ClassLevelBase, ABC):
    class_ = Class.CLERIC
    hit_die = Die.D8


class ClericLevel1(ClericLevelBase):
    number = Level.FIRST


class ClericLevel2(ClericLevelBase):
    number = Level.SECOND


class ClericLevel3(ClericLevelBase):
    number = Level.THIRD


class ClericLevel4(ClericLevelBase):
    number = Level.FOURTH


class ClericLevel5(ClericLevelBase):
    number = Level.FIFTH


class ClericLevel6(ClericLevelBase):
    number = Level.SIXTH


class ClericLevel7(ClericLevelBase):
    number = Level.SEVENTH


class ClericLevel8(ClericLevelBase):
    number = Level.EIGHTH


class ClericLevel9(ClericLevelBase):
    number = Level.NINTH


class ClericLevel10(ClericLevelBase):
    number = Level.TENTH


class ClericLevel11(ClericLevelBase):
    number = Level.ELEVENTH


class ClericLevel12(ClericLevelBase):
    number = Level.TWELFTH


class ClericLevel13(ClericLevelBase):
    number = Level.THIRTEENTH


class ClericLevel14(ClericLevelBase):
    number = Level.FOURTEENTH


class ClericLevel15(ClericLevelBase):
    number = Level.FIFTEENTH


class ClericLevel16(ClericLevelBase):
    number = Level.SIXTEENTH


class ClericLevel17(ClericLevelBase):
    number = Level.SEVENTEENTH


class ClericLevel18(ClericLevelBase):
    number = Level.EIGHTEENTH


class ClericLevel19(ClericLevelBase):
    number = Level.NINETEENTH


class ClericLevel20(ClericLevelBase):
    number = Level.TWENTIETH


class ClericSubclassField:
    def __get__(
        self, owner: ClassModifier | None, objtype: type | None = None
    ) -> ClericSubclass:
        if owner is None:
            return ClericSubclass.ARCANA
        return owner._cleric_subclass

    def __set__(self, owner: ClassModifier, value: ClericSubclass) -> None:
        owner._cleric_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: ClericSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return ClericLevel1()
            case Level.SECOND:
                return ClericLevel2()
            case Level.THIRD:
                return ClericLevel3()
            case Level.FOURTH:
                return ClericLevel4()
            case Level.FIFTH:
                return ClericLevel5()
            case Level.SIXTH:
                return ClericLevel6()
            case Level.SEVENTH:
                return ClericLevel7()
            case Level.EIGHTH:
                return ClericLevel8()
            case Level.NINTH:
                return ClericLevel9()
            case Level.TENTH:
                return ClericLevel10()
            case Level.ELEVENTH:
                return ClericLevel11()
            case Level.TWELFTH:
                return ClericLevel12()
            case Level.THIRTEENTH:
                return ClericLevel13()
            case Level.FOURTEENTH:
                return ClericLevel14()
            case Level.FIFTEENTH:
                return ClericLevel15()
            case Level.SIXTEENTH:
                return ClericLevel16()
            case Level.SEVENTEENTH:
                return ClericLevel17()
            case Level.EIGHTEENTH:
                return ClericLevel18()
            case Level.NINETEENTH:
                return ClericLevel19()
            case Level.TWENTIETH:
                return ClericLevel20()
            case _ as never:
                assert_never(never)
