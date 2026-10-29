from __future__ import annotations

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class TabaxiMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.TABAXI

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class TabaxiVolosGuidetoMonstersRace(SubraceModifier):
    race: ClassVar[Race] = Race.TABAXI

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
