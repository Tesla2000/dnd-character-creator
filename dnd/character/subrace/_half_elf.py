from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class AquaticElfHeritagePlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALF_ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class DarkElfHeritagePlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALF_ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class HighElfHeritagePlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALF_ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class WoodElfHeritagePlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALF_ELF

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
