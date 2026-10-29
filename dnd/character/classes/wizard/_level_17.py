from __future__ import annotations

from collections.abc import Generator
from typing import ClassVar

from pydantic import BaseModel
from pydantic import ConfigDict

from dnd.character.base import ModifierSource
from dnd.character.base import Priority
from dnd.character.base import _Modifier
from dnd.character.base import _ModifierSource
from dnd.character.classes._enums import Class
from dnd.character.classes.wizard._level_base import _WizardLevelBase


class WizardLevel17Argument(BaseModel):
    model_config = ConfigDict(frozen=True)


class _WizardLevel17(_WizardLevelBase):
    class_ = Class.WIZARD

    def _get_level_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class _WizardLevel17Converter:
    def convert(self, _: WizardLevel17Argument) -> _WizardLevel17:
        return _WizardLevel17()


class WizardLevelComposer17(ModifierSource):
    priority: ClassVar[Priority] = Priority.UNORDERED

    new_level: WizardLevel17Argument
    previous: ModifierSource

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield self.previous
        yield _WizardLevel17Converter().convert(self.new_level)
