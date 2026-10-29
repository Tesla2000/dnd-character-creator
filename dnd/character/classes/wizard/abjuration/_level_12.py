from __future__ import annotations

from dnd.character.classes.wizard._level_12 import WizardLevelComposer12
from dnd.character.classes.wizard.abjuration._level_11 import AbjurationLevelComposer11


class AbjurationLevelComposer12(WizardLevelComposer12):
    previous: AbjurationLevelComposer11
