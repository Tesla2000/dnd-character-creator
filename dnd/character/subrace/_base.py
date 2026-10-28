from __future__ import annotations

from abc import ABC
from typing import ClassVar

from dnd.character.base import ModifierSource
from dnd.character.base import Priority
from dnd.character.race import Race


class SubraceModifier(ModifierSource, ABC):
    """Base for subraces. Each subrace names the race it belongs to."""

    priority: ClassVar[Priority] = Priority.SUBRACE
    race: ClassVar[Race]
