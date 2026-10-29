from __future__ import annotations

from dnd.character.classes.wizard._level_7 import WizardLevelComposer7
from dnd.character.classes.wizard.abjuration._level_6 import AbjurationLevelComposer6


class AbjurationLevelComposer7(WizardLevelComposer7):
    previous: AbjurationLevelComposer6
