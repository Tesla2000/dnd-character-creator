from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class MarkofHealingEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class MarkofHospitalityEberronRisingfromtheLastWarRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class LotusdenHalflingExplorersGuidetoWildemountRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class LightfootPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class StoutPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class GhostwiseSwordCoastAdventurersGuideRace(SubraceModifier):
    race: ClassVar[Race] = Race.HALFLING

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()
