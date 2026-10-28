from __future__ import annotations

from abc import ABC
from typing import ClassVar

from dnd.character.base import ModifierSource
from dnd.character.base import Priority


class HelmetModifier(ModifierSource, ABC):
    """Base for helmets. Every helmet is a source, so plate armor cannot go on the head."""

    priority: ClassVar[Priority] = Priority.UNORDERED
