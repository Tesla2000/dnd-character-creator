from __future__ import annotations

from abc import ABC
from dnd.character.classes.base import ClassLevelBase
from dnd.character.classes.base import Die
from dnd.character.classes.enums import ArtificerSubclass
from dnd.character.classes.enums import Class
from dnd.character.level import Level
from typing import TYPE_CHECKING
from typing import assert_never

if TYPE_CHECKING:
    from dnd.character.classes.modifier import ClassModifier


class ArtificerLevelBase(ClassLevelBase, ABC):
    class_ = Class.ARTIFICER
    hit_die = Die.D8


class ArtificerLevel1(ArtificerLevelBase):
    number = Level.FIRST


class ArtificerLevel2(ArtificerLevelBase):
    number = Level.SECOND


class ArtificerLevel3(ArtificerLevelBase):
    number = Level.THIRD


class ArtificerLevel4(ArtificerLevelBase):
    number = Level.FOURTH


class ArtificerLevel5(ArtificerLevelBase):
    number = Level.FIFTH


class ArtificerLevel6(ArtificerLevelBase):
    number = Level.SIXTH


class ArtificerLevel7(ArtificerLevelBase):
    number = Level.SEVENTH


class ArtificerLevel8(ArtificerLevelBase):
    number = Level.EIGHTH


class ArtificerLevel9(ArtificerLevelBase):
    number = Level.NINTH


class ArtificerLevel10(ArtificerLevelBase):
    number = Level.TENTH


class ArtificerLevel11(ArtificerLevelBase):
    number = Level.ELEVENTH


class ArtificerLevel12(ArtificerLevelBase):
    number = Level.TWELFTH


class ArtificerLevel13(ArtificerLevelBase):
    number = Level.THIRTEENTH


class ArtificerLevel14(ArtificerLevelBase):
    number = Level.FOURTEENTH


class ArtificerLevel15(ArtificerLevelBase):
    number = Level.FIFTEENTH


class ArtificerLevel16(ArtificerLevelBase):
    number = Level.SIXTEENTH


class ArtificerLevel17(ArtificerLevelBase):
    number = Level.SEVENTEENTH


class ArtificerLevel18(ArtificerLevelBase):
    number = Level.EIGHTEENTH


class ArtificerLevel19(ArtificerLevelBase):
    number = Level.NINETEENTH


class ArtificerLevel20(ArtificerLevelBase):
    number = Level.TWENTIETH


class ArtificerSubclassField:
    def __get__(
        self, owner: ClassModifier | None, objtype: type | None = None
    ) -> ArtificerSubclass:
        if owner is None:
            return ArtificerSubclass.ALCHEMIST
        return owner._artificer_subclass

    def __set__(self, owner: ClassModifier, value: ArtificerSubclass) -> None:
        owner._artificer_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: ArtificerSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return ArtificerLevel1()
            case Level.SECOND:
                return ArtificerLevel2()
            case Level.THIRD:
                return ArtificerLevel3()
            case Level.FOURTH:
                return ArtificerLevel4()
            case Level.FIFTH:
                return ArtificerLevel5()
            case Level.SIXTH:
                return ArtificerLevel6()
            case Level.SEVENTH:
                return ArtificerLevel7()
            case Level.EIGHTH:
                return ArtificerLevel8()
            case Level.NINTH:
                return ArtificerLevel9()
            case Level.TENTH:
                return ArtificerLevel10()
            case Level.ELEVENTH:
                return ArtificerLevel11()
            case Level.TWELFTH:
                return ArtificerLevel12()
            case Level.THIRTEENTH:
                return ArtificerLevel13()
            case Level.FOURTEENTH:
                return ArtificerLevel14()
            case Level.FIFTEENTH:
                return ArtificerLevel15()
            case Level.SIXTEENTH:
                return ArtificerLevel16()
            case Level.SEVENTEENTH:
                return ArtificerLevel17()
            case Level.EIGHTEENTH:
                return ArtificerLevel18()
            case Level.NINETEENTH:
                return ArtificerLevel19()
            case Level.TWENTIETH:
                return ArtificerLevel20()
            case _ as never:
                assert_never(never)
