from __future__ import annotations

from abc import ABC
from dnd.character.classes.base import ClassLevelBase
from dnd.character.classes.base import Die
from dnd.character.classes.enums import Class
from dnd.character.classes.enums import WizardSubclass
from dnd.character.level import Level
from enum import StrEnum
from enum import auto
from pydantic import BaseModel
from pydantic import ConfigDict
from typing import ClassVar
from typing import TYPE_CHECKING
from typing import assert_never

if TYPE_CHECKING:
    from dnd.character.classes.modifier import ClassModifier


class WizardLevelBase(ClassLevelBase, ABC):
    class_ = Class.WIZARD
    hit_die = Die.D6


class WizardLevel1(WizardLevelBase):
    number = Level.FIRST


class WizardLevel3(WizardLevelBase):
    number = Level.THIRD


class WizardLevel4(WizardLevelBase):
    number = Level.FOURTH


class WizardLevel5(WizardLevelBase):
    number = Level.FIFTH


class WizardLevel7(WizardLevelBase):
    number = Level.SEVENTH


class WizardLevel8(WizardLevelBase):
    number = Level.EIGHTH


class WizardLevel9(WizardLevelBase):
    number = Level.NINTH


class WizardLevel11(WizardLevelBase):
    number = Level.ELEVENTH


class WizardLevel12(WizardLevelBase):
    number = Level.TWELFTH


class WizardLevel13(WizardLevelBase):
    number = Level.THIRTEENTH


class WizardLevel15(WizardLevelBase):
    number = Level.FIFTEENTH


class WizardLevel16(WizardLevelBase):
    number = Level.SIXTEENTH


class WizardLevel17(WizardLevelBase):
    number = Level.SEVENTEENTH


class WizardLevel18(WizardLevelBase):
    number = Level.EIGHTEENTH


class WizardLevel19(WizardLevelBase):
    number = Level.NINETEENTH


class WizardLevel20(WizardLevelBase):
    number = Level.TWENTIETH


class SchoolSlot(StrEnum):
    SECOND = auto()
    SIXTH = auto()
    TENTH = auto()
    FOURTEENTH = auto()


class WizardSchoolLevelBase(WizardLevelBase, ABC):
    """A wizard level that belongs to a school, so it changes when the school changes."""

    school: ClassVar[WizardSubclass]
    slot: ClassVar[SchoolSlot]


class WizardLevel2Abjuration(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.ABJURATION


class WizardLevel6Abjuration(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.ABJURATION


class WizardLevel10Abjuration(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.ABJURATION


class WizardLevel14Abjuration(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.ABJURATION


class WizardLevel2Bladesinging(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.BLADESINGING


class WizardLevel6Bladesinging(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.BLADESINGING


class WizardLevel10Bladesinging(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.BLADESINGING


class WizardLevel14Bladesinging(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.BLADESINGING


class WizardLevel2Chronurgy(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.CHRONURGY


class WizardLevel6Chronurgy(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.CHRONURGY


class WizardLevel10Chronurgy(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.CHRONURGY


class WizardLevel14Chronurgy(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.CHRONURGY


class WizardLevel2Conjuration(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.CONJURATION


class WizardLevel6Conjuration(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.CONJURATION


class WizardLevel10Conjuration(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.CONJURATION


class WizardLevel14Conjuration(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.CONJURATION


class WizardLevel2Divination(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.DIVINATION


class WizardLevel6Divination(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.DIVINATION


class WizardLevel10Divination(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.DIVINATION


class WizardLevel14Divination(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.DIVINATION


class WizardLevel2Enchantment(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.ENCHANTMENT


class WizardLevel6Enchantment(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.ENCHANTMENT


class WizardLevel10Enchantment(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.ENCHANTMENT


class WizardLevel14Enchantment(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.ENCHANTMENT


class WizardLevel2Evocation(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.EVOCATION


class WizardLevel6Evocation(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.EVOCATION


class WizardLevel10Evocation(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.EVOCATION


class WizardLevel14Evocation(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.EVOCATION


class WizardLevel2Graviturgy(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.GRAVITURGY


class WizardLevel6Graviturgy(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.GRAVITURGY


class WizardLevel10Graviturgy(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.GRAVITURGY


class WizardLevel14Graviturgy(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.GRAVITURGY


class WizardLevel2Illusion(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.ILLUSION


class WizardLevel6Illusion(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.ILLUSION


class WizardLevel10Illusion(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.ILLUSION


class WizardLevel14Illusion(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.ILLUSION


class WizardLevel2Necromancy(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.NECROMANCY


class WizardLevel6Necromancy(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.NECROMANCY


class WizardLevel10Necromancy(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.NECROMANCY


class WizardLevel14Necromancy(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.NECROMANCY


class WizardLevel2Scribes(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.SCRIBES


class WizardLevel6Scribes(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.SCRIBES


class WizardLevel10Scribes(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.SCRIBES


class WizardLevel14Scribes(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.SCRIBES


class WizardLevel2Transmutation(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.TRANSMUTATION


class WizardLevel6Transmutation(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.TRANSMUTATION


class WizardLevel10Transmutation(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.TRANSMUTATION


class WizardLevel14Transmutation(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.TRANSMUTATION


class WizardLevel2WarMagic(WizardSchoolLevelBase):
    number = Level.SECOND
    slot = SchoolSlot.SECOND
    school = WizardSubclass.WAR_MAGIC


class WizardLevel6WarMagic(WizardSchoolLevelBase):
    number = Level.SIXTH
    slot = SchoolSlot.SIXTH
    school = WizardSubclass.WAR_MAGIC


class WizardLevel10WarMagic(WizardSchoolLevelBase):
    number = Level.TENTH
    slot = SchoolSlot.TENTH
    school = WizardSubclass.WAR_MAGIC


class WizardLevel14WarMagic(WizardSchoolLevelBase):
    number = Level.FOURTEENTH
    slot = SchoolSlot.FOURTEENTH
    school = WizardSubclass.WAR_MAGIC


class WizardSchoolLevels(BaseModel):
    """The four level classes a wizard school provides, at levels 2, 6, 10 and 14."""

    model_config = ConfigDict(frozen=True)

    second: type[WizardSchoolLevelBase]
    sixth: type[WizardSchoolLevelBase]
    tenth: type[WizardSchoolLevelBase]
    fourteenth: type[WizardSchoolLevelBase]


class WizardSubclassField:
    def __get__(
        self, owner: ClassModifier | None, objtype: type | None = None
    ) -> WizardSubclass:
        if owner is None:
            return WizardSubclass.ABJURATION
        return owner._wizard_subclass

    def __set__(self, owner: ClassModifier, value: WizardSubclass) -> None:
        owner._wizard_subclass = value
        owner._levels = tuple(
            self._school_level(level.slot, value)
            if isinstance(level, WizardSchoolLevelBase)
            else level
            for level in owner._levels
        )

    @classmethod
    def _school_level(
        cls, slot: SchoolSlot, subclass: WizardSubclass
    ) -> WizardSchoolLevelBase:
        levels = cls._school_levels(subclass)
        match slot:
            case SchoolSlot.SECOND:
                return levels.second()
            case SchoolSlot.SIXTH:
                return levels.sixth()
            case SchoolSlot.TENTH:
                return levels.tenth()
            case SchoolSlot.FOURTEENTH:
                return levels.fourteenth()
            case _ as never:
                assert_never(never)

    @staticmethod
    def _school_levels(subclass: WizardSubclass) -> WizardSchoolLevels:
        match subclass:
            case WizardSubclass.ABJURATION:
                return WizardSchoolLevels(
                    second=WizardLevel2Abjuration,
                    sixth=WizardLevel6Abjuration,
                    tenth=WizardLevel10Abjuration,
                    fourteenth=WizardLevel14Abjuration,
                )
            case WizardSubclass.BLADESINGING:
                return WizardSchoolLevels(
                    second=WizardLevel2Bladesinging,
                    sixth=WizardLevel6Bladesinging,
                    tenth=WizardLevel10Bladesinging,
                    fourteenth=WizardLevel14Bladesinging,
                )
            case WizardSubclass.CHRONURGY:
                return WizardSchoolLevels(
                    second=WizardLevel2Chronurgy,
                    sixth=WizardLevel6Chronurgy,
                    tenth=WizardLevel10Chronurgy,
                    fourteenth=WizardLevel14Chronurgy,
                )
            case WizardSubclass.CONJURATION:
                return WizardSchoolLevels(
                    second=WizardLevel2Conjuration,
                    sixth=WizardLevel6Conjuration,
                    tenth=WizardLevel10Conjuration,
                    fourteenth=WizardLevel14Conjuration,
                )
            case WizardSubclass.DIVINATION:
                return WizardSchoolLevels(
                    second=WizardLevel2Divination,
                    sixth=WizardLevel6Divination,
                    tenth=WizardLevel10Divination,
                    fourteenth=WizardLevel14Divination,
                )
            case WizardSubclass.ENCHANTMENT:
                return WizardSchoolLevels(
                    second=WizardLevel2Enchantment,
                    sixth=WizardLevel6Enchantment,
                    tenth=WizardLevel10Enchantment,
                    fourteenth=WizardLevel14Enchantment,
                )
            case WizardSubclass.EVOCATION:
                return WizardSchoolLevels(
                    second=WizardLevel2Evocation,
                    sixth=WizardLevel6Evocation,
                    tenth=WizardLevel10Evocation,
                    fourteenth=WizardLevel14Evocation,
                )
            case WizardSubclass.GRAVITURGY:
                return WizardSchoolLevels(
                    second=WizardLevel2Graviturgy,
                    sixth=WizardLevel6Graviturgy,
                    tenth=WizardLevel10Graviturgy,
                    fourteenth=WizardLevel14Graviturgy,
                )
            case WizardSubclass.ILLUSION:
                return WizardSchoolLevels(
                    second=WizardLevel2Illusion,
                    sixth=WizardLevel6Illusion,
                    tenth=WizardLevel10Illusion,
                    fourteenth=WizardLevel14Illusion,
                )
            case WizardSubclass.NECROMANCY:
                return WizardSchoolLevels(
                    second=WizardLevel2Necromancy,
                    sixth=WizardLevel6Necromancy,
                    tenth=WizardLevel10Necromancy,
                    fourteenth=WizardLevel14Necromancy,
                )
            case WizardSubclass.SCRIBES:
                return WizardSchoolLevels(
                    second=WizardLevel2Scribes,
                    sixth=WizardLevel6Scribes,
                    tenth=WizardLevel10Scribes,
                    fourteenth=WizardLevel14Scribes,
                )
            case WizardSubclass.TRANSMUTATION:
                return WizardSchoolLevels(
                    second=WizardLevel2Transmutation,
                    sixth=WizardLevel6Transmutation,
                    tenth=WizardLevel10Transmutation,
                    fourteenth=WizardLevel14Transmutation,
                )
            case WizardSubclass.WAR_MAGIC:
                return WizardSchoolLevels(
                    second=WizardLevel2WarMagic,
                    sixth=WizardLevel6WarMagic,
                    tenth=WizardLevel10WarMagic,
                    fourteenth=WizardLevel14WarMagic,
                )
            case _ as never:
                assert_never(never)

    @classmethod
    def level(cls, number: Level, subclass: WizardSubclass) -> ClassLevelBase:
        match number:
            case Level.FIRST:
                return WizardLevel1()
            case Level.SECOND:
                return cls._school_levels(subclass).second()
            case Level.THIRD:
                return WizardLevel3()
            case Level.FOURTH:
                return WizardLevel4()
            case Level.FIFTH:
                return WizardLevel5()
            case Level.SIXTH:
                return cls._school_levels(subclass).sixth()
            case Level.SEVENTH:
                return WizardLevel7()
            case Level.EIGHTH:
                return WizardLevel8()
            case Level.NINTH:
                return WizardLevel9()
            case Level.TENTH:
                return cls._school_levels(subclass).tenth()
            case Level.ELEVENTH:
                return WizardLevel11()
            case Level.TWELFTH:
                return WizardLevel12()
            case Level.THIRTEENTH:
                return WizardLevel13()
            case Level.FOURTEENTH:
                return cls._school_levels(subclass).fourteenth()
            case Level.FIFTEENTH:
                return WizardLevel15()
            case Level.SIXTEENTH:
                return WizardLevel16()
            case Level.SEVENTEENTH:
                return WizardLevel17()
            case Level.EIGHTEENTH:
                return WizardLevel18()
            case Level.NINETEENTH:
                return WizardLevel19()
            case Level.TWENTIETH:
                return WizardLevel20()
            case _ as never:
                assert_never(never)
