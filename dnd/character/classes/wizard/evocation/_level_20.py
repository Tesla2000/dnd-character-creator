from __future__ import annotations

from dnd.character.classes.wizard._level_20 import WizardLevelComposer20
from dnd.character.classes.wizard.evocation._level_19 import EvocationLevelComposer19


class EvocationLevelComposer20(WizardLevelComposer20):
    previous: EvocationLevelComposer19
