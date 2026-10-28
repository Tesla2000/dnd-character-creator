from __future__ import annotations

from abc import ABC
from dnd.character.classes._base import ClassLevelBase
from dnd.character.classes._base import Die
from dnd.character.classes._enums import Class
from dnd.character.classes._enums import PaladinSubclass
from dnd.character.level import Level
from typing import Protocol
from typing import assert_never


class PaladinLevelBase(ClassLevelBase, ABC):
    class_ = Class.PALADIN
    hit_die = Die.D10


class PaladinLevel1(PaladinLevelBase):
    number = Level.FIRST


class PaladinLevel2(PaladinLevelBase):
    number = Level.SECOND


class PaladinLevel3(PaladinLevelBase):
    number = Level.THIRD


class PaladinLevel4(PaladinLevelBase):
    number = Level.FOURTH


class PaladinLevel5(PaladinLevelBase):
    number = Level.FIFTH


class PaladinLevel6(PaladinLevelBase):
    number = Level.SIXTH


class PaladinLevel7(PaladinLevelBase):
    number = Level.SEVENTH


class PaladinLevel8(PaladinLevelBase):
    number = Level.EIGHTH


class PaladinLevel9(PaladinLevelBase):
    number = Level.NINTH


class PaladinLevel10(PaladinLevelBase):
    number = Level.TENTH


class PaladinLevel11(PaladinLevelBase):
    number = Level.ELEVENTH


class PaladinLevel12(PaladinLevelBase):
    number = Level.TWELFTH


class PaladinLevel13(PaladinLevelBase):
    number = Level.THIRTEENTH


class PaladinLevel14(PaladinLevelBase):
    number = Level.FOURTEENTH


class PaladinLevel15(PaladinLevelBase):
    number = Level.FIFTEENTH


class PaladinLevel16(PaladinLevelBase):
    number = Level.SIXTEENTH


class PaladinLevel17(PaladinLevelBase):
    number = Level.SEVENTEENTH


class PaladinLevel18(PaladinLevelBase):
    number = Level.EIGHTEENTH


class PaladinLevel19(PaladinLevelBase):
    number = Level.NINETEENTH


class PaladinLevel20(PaladinLevelBase):
    number = Level.TWENTIETH


class PaladinOwner(Protocol):
    _levels: tuple[ClassLevelBase, ...]
    _paladin_subclass: PaladinSubclass


class PaladinSubclassField:
    def __get__(
        self, owner: PaladinOwner | None, _objtype: type | None = None
    ) -> PaladinSubclass:
        if owner is None:
            return PaladinSubclass.ANCIENTS
        return owner._paladin_subclass

    def __set__(self, owner: PaladinOwner, value: PaladinSubclass) -> None:
        owner._paladin_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: PaladinSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return PaladinLevel1()
            case Level.SECOND:
                return PaladinLevel2()
            case Level.THIRD:
                return PaladinLevel3()
            case Level.FOURTH:
                return PaladinLevel4()
            case Level.FIFTH:
                return PaladinLevel5()
            case Level.SIXTH:
                return PaladinLevel6()
            case Level.SEVENTH:
                return PaladinLevel7()
            case Level.EIGHTH:
                return PaladinLevel8()
            case Level.NINTH:
                return PaladinLevel9()
            case Level.TENTH:
                return PaladinLevel10()
            case Level.ELEVENTH:
                return PaladinLevel11()
            case Level.TWELFTH:
                return PaladinLevel12()
            case Level.THIRTEENTH:
                return PaladinLevel13()
            case Level.FOURTEENTH:
                return PaladinLevel14()
            case Level.FIFTEENTH:
                return PaladinLevel15()
            case Level.SIXTEENTH:
                return PaladinLevel16()
            case Level.SEVENTEENTH:
                return PaladinLevel17()
            case Level.EIGHTEENTH:
                return PaladinLevel18()
            case Level.NINETEENTH:
                return PaladinLevel19()
            case Level.TWENTIETH:
                return PaladinLevel20()
            case _ as never:
                assert_never(never)
