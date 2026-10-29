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


class WizardLevel11Argument(BaseModel):
    model_config = ConfigDict(frozen=True)


class _WizardLevel11(_WizardLevelBase):
    class_ = Class.WIZARD

    def _get_level_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield from ()


class _WizardLevel11Converter:
    def convert(self, _: WizardLevel11Argument) -> _WizardLevel11:
        return _WizardLevel11()


class WizardLevelComposer11(ModifierSource):
    priority: ClassVar[Priority] = Priority.UNORDERED

    new_level: WizardLevel11Argument
    previous: ModifierSource

    def get_modifiers(self) -> Generator[_Modifier | _ModifierSource]:
        yield self.previous
        yield _WizardLevel11Converter().convert(self.new_level)
