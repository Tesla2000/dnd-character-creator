from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Generator
from enum import IntEnum
from enum import StrEnum
from enum import auto
from typing import ClassVar
from typing import Self
from typing import assert_never

from dnd.character.blueprint.sentinels import Level
from dnd.choices.class_creation.character_class import Class
from dnd.choices.class_creation.character_class import WizardSubclass
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import InstanceOf
from pydantic import NonNegativeInt


class Die(IntEnum):
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20


class MaxHealth(int):
    def __new__(cls, value: int) -> Self:
        if value <= 0:
            raise ValueError(f"MaxHealth must be a positive integer, got {value}")
        return super().__new__(cls, value)


class _ModifierSource(ABC):
    """Anything that produces modifiers, either leaf modifiers or further sources."""

    @abstractmethod
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]: ...


class ModifierSource(_ModifierSource, BaseModel, ABC):
    model_config = ConfigDict(frozen=True)


class _Modifier(ABC):
    """A leaf effect that computes its contribution from the character."""

    @abstractmethod
    def apply(self, character: Character) -> object: ...


class Modifier(_Modifier, BaseModel):
    model_config = ConfigDict(frozen=True)


class MaxHealthModifier(Modifier):
    bonus: int

    def apply(self, character: Character) -> int:
        return self.bonus


class DwarvenToughnessModifier(Modifier):
    def apply(self, character: Character) -> int:
        return character.level


class AcModifier(Modifier):
    bonus: int

    def apply(self, character: Character) -> int:
        return self.bonus


class DarkvisionModifier(Modifier):
    range_feet: NonNegativeInt

    def apply(self, character: Character) -> int:
        return self.range_feet


class ClassLevelBase(ModifierSource, ABC):
    """Base for one class: its class and hit die. Each level is a subclass of this."""

    class_: ClassVar[Class]
    hit_die: ClassVar[Die]
    number: ClassVar[Level]

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield MaxHealthModifier(bonus=self.hit_die // 2 + 1)


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


class ClassModifier(_ModifierSource):
    _levels: tuple[ClassLevelBase, ...] = ()
    _wizard_subclass: WizardSubclass = WizardSubclass.ABJURATION
    wizard_subclass = WizardSubclassField()

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from self._levels

    def class_level(self, class_: Class) -> int:
        return sum(1 for level in self._levels if level.class_ == class_)

    def total_level(self) -> int:
        return len(self._levels)

    def level_up(self, class_: Class) -> None:
        match class_:
            case Class.WIZARD:
                number = Level(self.class_level(Class.WIZARD) + 1)
                self._levels = (
                    *self._levels,
                    WizardSubclassField.level(number, self._wizard_subclass),
                )
            case (
                Class.ARTIFICER
                | Class.BARBARIAN
                | Class.BARD
                | Class.CLERIC
                | Class.DRUID
                | Class.FIGHTER
                | Class.MONK
                | Class.PALADIN
                | Class.RANGER
                | Class.ROGUE
                | Class.SORCERER
                | Class.WARLOCK
            ):
                # TODO: level up for the other classes
                raise NotImplementedError(f"Level up for {class_!r} is not written yet")
            case _ as never:
                assert_never(never)

class RaceModifier(ModifierSource, ABC):
    """Base for race-subrace pairs."""


class HumanRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class HillDwarfRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
        yield DwarvenToughnessModifier()


class HighElfRace(RaceModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class HelmetModifier(ModifierSource, ABC):
    """Base for helmets. Every helmet is a source, so plate armor cannot go on the head."""


class NoHelmet(HelmetModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class CloakModifier(ModifierSource, ABC):
    """Base for cloaks. Every cloak is a source, so plate armor cannot be a cape."""


class NoCloak(CloakModifier):
    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class Character(BaseModel):
    model_config = ConfigDict(frozen=True)

    class_modifier: InstanceOf[ClassModifier]
    race_modifier: RaceModifier
    helmet_modifier: HelmetModifier = NoHelmet()
    cloak_modifier: CloakModifier = NoCloak()

    @property
    def level(self) -> int:
        return self.class_modifier.total_level()

    @property
    def modifiers(self) -> tuple[_Modifier, ...]:
        roots = (
            self.class_modifier,
            self.race_modifier,
            self.helmet_modifier,
            self.cloak_modifier,
        )
        return tuple(found for root in roots for found in self._walk(root))

    @classmethod
    def _walk(cls, source: _ModifierSource) -> Generator[_Modifier]:
        for child in source.get_modifiers():
            if isinstance(child, _ModifierSource):
                yield from cls._walk(child)
            else:
                yield child


class Getter(BaseModel, ABC):
    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def get(self, character: Character) -> object: ...


class MaxHealthGetter(Getter):
    def get(self, character: Character) -> MaxHealth:
        return MaxHealth(
            sum(
                modifier.apply(character)
                for modifier in character.modifiers
                if isinstance(modifier, (MaxHealthModifier, DwarvenToughnessModifier))
            )
        )


class AcGetter(Getter):
    base: int = 10

    def get(self, character: Character) -> int:
        return self.base + sum(
            modifier.apply(character)
            for modifier in character.modifiers
            if isinstance(modifier, AcModifier)
        )


class DarkvisionGetter(Getter):
    def get(self, character: Character) -> int:
        return max(
            (
                modifier.apply(character)
                for modifier in character.modifiers
                if isinstance(modifier, DarkvisionModifier)
            ),
            default=0,
        )
