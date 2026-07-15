from typing import Literal
from typing import TypeAlias

from dnd.character.blueprint.sentinels import (
    ClassPreSubclassLevel,
    FirstSubclassPreLevel,
    SecondSubclassPreLevel,
    SorcererPreSubclassLevel,
    ThirdSubclassPreLevel,
    WizardPreSubclassLevel,
)
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.race.race import Race
from dnd.character.stats import Stats

_Z = Literal[SecondSubclassPreLevel.ZEROTH]
_SZ = Literal[FirstSubclassPreLevel.ZEROTH]
_TZ = Literal[ThirdSubclassPreLevel.ZEROTH]

InitializedBlueprint: TypeAlias = Blueprint[
    Race,
    Stats,
    None,
    Literal[0],
    Literal[0],
    WizardPreSubclassLevel[_Z, None],
    SorcererPreSubclassLevel[_SZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    None,
]
