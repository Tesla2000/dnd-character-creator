from __future__ import annotations
from typing import Never

from collections.abc import Generator


from typing import Protocol

from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.health import HealthModifier
from dnd.character.sight import DarkvisionModifier
from typing import ClassVar
from dnd.character.race import Race
from dnd.character.subrace._base import SubraceModifier


class DwarvenCharacter(Protocol):
    @property
    def level(self) -> int: ...


class DwarvenToughnessModifier(HealthModifier[DwarvenCharacter]):
    def apply(self, character: DwarvenCharacter) -> int:
        return character.level


class HillDwarfPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.DWARF

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
        yield DwarvenToughnessModifier()


class MountainDwarfPlayersHandbookRace(SubraceModifier):
    race: ClassVar[Race] = Race.DWARF

    def get_modifiers(self) -> Generator[_Modifier[Never] | _ModifierSource]:
        yield DarkvisionModifier(range_feet=60)
