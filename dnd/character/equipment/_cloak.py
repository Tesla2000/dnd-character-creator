from __future__ import annotations

from abc import ABC
from typing import ClassVar

from dnd.character.base import ModifierSource
from dnd.character.base import Priority


class CloakModifier(ModifierSource, ABC):
    """Base for cloaks. Every cloak is a source, so plate armor cannot be a cape."""

    priority: ClassVar[Priority] = Priority.UNORDERED
