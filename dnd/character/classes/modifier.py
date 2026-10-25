from __future__ import annotations

from collections.abc import Generator
from dnd.character.classes.artificer import ArtificerSubclassField
from dnd.character.classes.barbarian import BarbarianSubclassField
from dnd.character.classes.bard import BardSubclassField
from dnd.character.classes.base import ClassLevelBase
from dnd.character.classes.cleric import ClericSubclassField
from dnd.character.classes.druid import DruidSubclassField
from dnd.character.classes.enums import ArtificerSubclass
from dnd.character.classes.enums import BarbarianSubclass
from dnd.character.classes.enums import BardSubclass
from dnd.character.classes.enums import Class
from dnd.character.classes.enums import ClericSubclass
from dnd.character.classes.enums import DruidSubclass
from dnd.character.classes.enums import FighterSubclass
from dnd.character.classes.enums import MonkSubclass
from dnd.character.classes.enums import PaladinSubclass
from dnd.character.classes.enums import RangerSubclass
from dnd.character.classes.enums import RogueSubclass
from dnd.character.classes.enums import SorcererSubclass
from dnd.character.classes.enums import WarlockSubclass
from dnd.character.classes.enums import WizardSubclass
from dnd.character.classes.fighter import FighterSubclassField
from dnd.character.classes.monk import MonkSubclassField
from dnd.character.classes.paladin import PaladinSubclassField
from dnd.character.classes.ranger import RangerSubclassField
from dnd.character.classes.rogue import RogueSubclassField
from dnd.character.classes.sorcerer import SorcererSubclassField
from dnd.character.classes.warlock import WarlockSubclassField
from dnd.character.classes.wizard import WizardSubclassField
from dnd.character.level import Level
from dnd.character.modifiers.base import _Modifier
from dnd.character.modifiers.health import MaxHealthModifier
from dnd.character.modifiers.source import _ModifierSource
from typing import assert_never


class ClassModifier(_ModifierSource):
    _levels: tuple[ClassLevelBase, ...] = ()
    _wizard_subclass: WizardSubclass = WizardSubclass.ABJURATION
    wizard_subclass = WizardSubclassField()
    _barbarian_subclass: BarbarianSubclass = BarbarianSubclass.ANCESTRAL_GUARDIAN
    barbarian_subclass = BarbarianSubclassField()
    _sorcerer_subclass: SorcererSubclass = SorcererSubclass.ABERRANT_MIND
    sorcerer_subclass = SorcererSubclassField()
    _artificer_subclass: ArtificerSubclass = ArtificerSubclass.ALCHEMIST
    artificer_subclass = ArtificerSubclassField()
    _bard_subclass: BardSubclass = BardSubclass.CREATION
    bard_subclass = BardSubclassField()
    _cleric_subclass: ClericSubclass = ClericSubclass.ARCANA
    cleric_subclass = ClericSubclassField()
    _druid_subclass: DruidSubclass = DruidSubclass.DREAMS
    druid_subclass = DruidSubclassField()
    _fighter_subclass: FighterSubclass = FighterSubclass.ARCANE_ARCHER
    fighter_subclass = FighterSubclassField()
    _monk_subclass: MonkSubclass = MonkSubclass.MERCY
    monk_subclass = MonkSubclassField()
    _paladin_subclass: PaladinSubclass = PaladinSubclass.ANCIENTS
    paladin_subclass = PaladinSubclassField()
    _ranger_subclass: RangerSubclass = RangerSubclass.BEAST_MASTER
    ranger_subclass = RangerSubclassField()
    _rogue_subclass: RogueSubclass = RogueSubclass.ARCANE_TRICKSTER
    rogue_subclass = RogueSubclassField()
    _warlock_subclass: WarlockSubclass = WarlockSubclass.ARCHFEY
    warlock_subclass = WarlockSubclassField()

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        for index, level in enumerate(self._levels):
            if index == 0:
                yield MaxHealthModifier(bonus=level.hit_die)
            else:
                yield level

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
            case Class.BARBARIAN:
                number = Level(self.class_level(Class.BARBARIAN) + 1)
                self._levels = (
                    *self._levels,
                    BarbarianSubclassField.level(number, self._barbarian_subclass),
                )
            case Class.SORCERER:
                number = Level(self.class_level(Class.SORCERER) + 1)
                self._levels = (
                    *self._levels,
                    SorcererSubclassField.level(number, self._sorcerer_subclass),
                )
            case Class.ARTIFICER:
                number = Level(self.class_level(Class.ARTIFICER) + 1)
                self._levels = (
                    *self._levels,
                    ArtificerSubclassField.level(number, self._artificer_subclass),
                )
            case Class.BARD:
                number = Level(self.class_level(Class.BARD) + 1)
                self._levels = (
                    *self._levels,
                    BardSubclassField.level(number, self._bard_subclass),
                )
            case Class.CLERIC:
                number = Level(self.class_level(Class.CLERIC) + 1)
                self._levels = (
                    *self._levels,
                    ClericSubclassField.level(number, self._cleric_subclass),
                )
            case Class.DRUID:
                number = Level(self.class_level(Class.DRUID) + 1)
                self._levels = (
                    *self._levels,
                    DruidSubclassField.level(number, self._druid_subclass),
                )
            case Class.FIGHTER:
                number = Level(self.class_level(Class.FIGHTER) + 1)
                self._levels = (
                    *self._levels,
                    FighterSubclassField.level(number, self._fighter_subclass),
                )
            case Class.MONK:
                number = Level(self.class_level(Class.MONK) + 1)
                self._levels = (
                    *self._levels,
                    MonkSubclassField.level(number, self._monk_subclass),
                )
            case Class.PALADIN:
                number = Level(self.class_level(Class.PALADIN) + 1)
                self._levels = (
                    *self._levels,
                    PaladinSubclassField.level(number, self._paladin_subclass),
                )
            case Class.RANGER:
                number = Level(self.class_level(Class.RANGER) + 1)
                self._levels = (
                    *self._levels,
                    RangerSubclassField.level(number, self._ranger_subclass),
                )
            case Class.ROGUE:
                number = Level(self.class_level(Class.ROGUE) + 1)
                self._levels = (
                    *self._levels,
                    RogueSubclassField.level(number, self._rogue_subclass),
                )
            case Class.WARLOCK:
                number = Level(self.class_level(Class.WARLOCK) + 1)
                self._levels = (
                    *self._levels,
                    WarlockSubclassField.level(number, self._warlock_subclass),
                )
            case _ as never:
                assert_never(never)
