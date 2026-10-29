from __future__ import annotations

from dnd.character.classes.wizard._level_20 import WizardLevelComposer20
from dnd.character.classes.wizard.abjuration._level_19 import AbjurationLevelComposer19


class AbjurationLevelComposer20(WizardLevelComposer20):
    previous: AbjurationLevelComposer19
