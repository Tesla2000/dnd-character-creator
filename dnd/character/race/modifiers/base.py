from __future__ import annotations

from abc import ABC
from dnd.character.modifiers.source import ModifierSource


class RaceModifier(ModifierSource, ABC):
    """Base for race-subrace pairs."""
