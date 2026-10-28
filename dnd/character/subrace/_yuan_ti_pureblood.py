from __future__ import annotations
from typing import Never

from collections.abc import Generator

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class YuantiMordenkainenPresentsMonstersoftheMultiverseRace(SubraceModifier):
    race: ClassVar[Race] = Race.YUAN_TI_PUREBLOOD

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)


class YuantiPurebloodVolosGuidetoMonstersRace(SubraceModifier):
    race: ClassVar[Race] = Race.YUAN_TI_PUREBLOOD

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
