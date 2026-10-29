from __future__ import annotations

from dnd.character.classes.wizard._level_5 import WizardLevelComposer5
from dnd.character.classes.wizard.evocation._level_4 import EvocationLevelComposer4


class EvocationLevelComposer5(WizardLevelComposer5):
    previous: EvocationLevelComposer4
