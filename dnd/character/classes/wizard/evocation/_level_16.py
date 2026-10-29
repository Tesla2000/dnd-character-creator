from __future__ import annotations

from dnd.character.classes.wizard._level_16 import WizardLevelComposer16
from dnd.character.classes.wizard.evocation._level_15 import EvocationLevelComposer15


class EvocationLevelComposer16(WizardLevelComposer16):
    previous: EvocationLevelComposer15
