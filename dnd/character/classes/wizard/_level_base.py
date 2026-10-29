from __future__ import annotations

from abc import ABC

from dnd.character.classes._base import ClassLevelBase
from dnd.character.classes._base import Die


class _WizardLevelBase(ClassLevelBase, ABC):
    hit_die = Die.D6
