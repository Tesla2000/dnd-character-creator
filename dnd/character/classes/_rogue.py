from __future__ import annotations

from abc import ABC
from dnd.character.classes._base import ClassLevelBase
from dnd.character.classes._base import Die
from dnd.character.classes._enums import Class
from dnd.character.classes._enums import RogueSubclass
from dnd.character.level import Level
from typing import Protocol
from typing import assert_never


class RogueLevelBase(ClassLevelBase, ABC):
    class_ = Class.ROGUE
    hit_die = Die.D8


class RogueLevel1(RogueLevelBase):
    number = Level.FIRST


class RogueLevel2(RogueLevelBase):
    number = Level.SECOND


class RogueLevel3(RogueLevelBase):
    number = Level.THIRD


class RogueLevel4(RogueLevelBase):
    number = Level.FOURTH


class RogueLevel5(RogueLevelBase):
    number = Level.FIFTH


class RogueLevel6(RogueLevelBase):
    number = Level.SIXTH


class RogueLevel7(RogueLevelBase):
    number = Level.SEVENTH


class RogueLevel8(RogueLevelBase):
    number = Level.EIGHTH


class RogueLevel9(RogueLevelBase):
    number = Level.NINTH


class RogueLevel10(RogueLevelBase):
    number = Level.TENTH


class RogueLevel11(RogueLevelBase):
    number = Level.ELEVENTH


class RogueLevel12(RogueLevelBase):
    number = Level.TWELFTH


class RogueLevel13(RogueLevelBase):
    number = Level.THIRTEENTH


class RogueLevel14(RogueLevelBase):
    number = Level.FOURTEENTH


class RogueLevel15(RogueLevelBase):
    number = Level.FIFTEENTH


class RogueLevel16(RogueLevelBase):
    number = Level.SIXTEENTH


class RogueLevel17(RogueLevelBase):
    number = Level.SEVENTEENTH


class RogueLevel18(RogueLevelBase):
    number = Level.EIGHTEENTH


class RogueLevel19(RogueLevelBase):
    number = Level.NINETEENTH


class RogueLevel20(RogueLevelBase):
    number = Level.TWENTIETH


class RogueOwner(Protocol):
    _levels: tuple[ClassLevelBase, ...]
    _rogue_subclass: RogueSubclass


class RogueSubclassField:
    def __get__(
        self, owner: RogueOwner | None, _objtype: type | None = None
    ) -> RogueSubclass:
        if owner is None:
            return RogueSubclass.ARCANE_TRICKSTER
        return owner._rogue_subclass

    def __set__(self, owner: RogueOwner, value: RogueSubclass) -> None:
        owner._rogue_subclass = value

    @classmethod
    def level(cls, number: Level, subclass: RogueSubclass) -> ClassLevelBase:
        # TODO: subclass-specific levels are not filled in yet
        match number:
            case Level.FIRST:
                return RogueLevel1()
            case Level.SECOND:
                return RogueLevel2()
            case Level.THIRD:
                return RogueLevel3()
            case Level.FOURTH:
                return RogueLevel4()
            case Level.FIFTH:
                return RogueLevel5()
            case Level.SIXTH:
                return RogueLevel6()
            case Level.SEVENTH:
                return RogueLevel7()
            case Level.EIGHTH:
                return RogueLevel8()
            case Level.NINTH:
                return RogueLevel9()
            case Level.TENTH:
                return RogueLevel10()
            case Level.ELEVENTH:
                return RogueLevel11()
            case Level.TWELFTH:
                return RogueLevel12()
            case Level.THIRTEENTH:
                return RogueLevel13()
            case Level.FOURTEENTH:
                return RogueLevel14()
            case Level.FIFTEENTH:
                return RogueLevel15()
            case Level.SIXTEENTH:
                return RogueLevel16()
            case Level.SEVENTEENTH:
                return RogueLevel17()
            case Level.EIGHTEENTH:
                return RogueLevel18()
            case Level.NINETEENTH:
                return RogueLevel19()
            case Level.TWENTIETH:
                return RogueLevel20()
            case _ as never:
                assert_never(never)
