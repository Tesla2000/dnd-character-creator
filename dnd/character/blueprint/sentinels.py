import types
from enum import IntEnum
from typing import Generic
from typing import Literal
from typing import TypeVar

from dnd.character.blueprint.character_data import CharacterData
from dnd.character.race.race import Race
from dnd.character.stats import Stats
from dnd.choices.class_creation.character_class import AnySubclass
from dnd.choices.class_creation.character_class import SorcererSubclass
from dnd.choices.class_creation.character_class import WizardSubclass
from pydantic import PositiveInt


class FirstSubclassPreLevel(IntEnum):
    """Level 0 for classes whose subclass arrives at level 1 (e.g. Sorcerer)."""

    ZEROTH = 0


class FirstSubclassPostLevel(IntEnum):
    """Levels 1–20: post-subclass range for subclass-at-1 classes."""

    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    NINTH = 9
    TENTH = 10
    ELEVENTH = 11
    TWELFTH = 12
    THIRTEENTH = 13
    FOURTEENTH = 14
    FIFTEENTH = 15
    SIXTEENTH = 16
    SEVENTEENTH = 17
    EIGHTEENTH = 18
    NINETEENTH = 19
    TWENTIETH = 20


Level = FirstSubclassPostLevel


class SecondSubclassPreLevel(IntEnum):
    """Levels 0–1 for classes whose subclass arrives at level 2 (e.g. Wizard)."""

    ZEROTH = 0
    FIRST = 1


class SecondSubclassPostLevel(IntEnum):
    """Levels 2–20: post-subclass range for subclass-at-2 classes."""

    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    NINTH = 9
    TENTH = 10
    ELEVENTH = 11
    TWELFTH = 12
    THIRTEENTH = 13
    FOURTEENTH = 14
    FIFTEENTH = 15
    SIXTEENTH = 16
    SEVENTEENTH = 17
    EIGHTEENTH = 18
    NINETEENTH = 19
    TWENTIETH = 20


class ThirdSubclassPreLevel(IntEnum):
    """Levels 0–2 for classes whose subclass arrives at level 3."""

    ZEROTH = 0
    FIRST = 1
    SECOND = 2


class ThirdSubclassPostLevel(IntEnum):
    """Levels 3–20: post-subclass range for subclass-at-3 classes."""

    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    NINTH = 9
    TENTH = 10
    ELEVENTH = 11
    TWELFTH = 12
    THIRTEENTH = 13
    FOURTEENTH = 14
    FIFTEENTH = 15
    SIXTEENTH = 16
    SEVENTEENTH = 17
    EIGHTEENTH = 18
    NINETEENTH = 19
    TWENTIETH = 20


# Internal TypeVars — only for phantom class Generic definitions.
# Covariant because phantom classes have no data fields; required for Literal subtyping.
_WPL = TypeVar("_WPL", bound=SecondSubclassPreLevel, covariant=True)
_WSL = TypeVar("_WSL", bound=SecondSubclassPostLevel, covariant=True)
_WSS = TypeVar("_WSS", bound=WizardSubclass, covariant=True)
_SPL = TypeVar("_SPL", bound=FirstSubclassPreLevel, covariant=True)
_SSL = TypeVar("_SSL", bound=FirstSubclassPostLevel, covariant=True)
_SSS = TypeVar("_SSS", bound=SorcererSubclass, covariant=True)
_CPL = TypeVar("_CPL", bound=ThirdSubclassPreLevel, covariant=True)
_CSL = TypeVar("_CSL", bound=ThirdSubclassPostLevel, covariant=True)
_CSS = TypeVar("_CSS", bound=AnySubclass, covariant=True)
_NT = TypeVar("_NT", bound=None, covariant=True)


class WizardPreSubclassLevel(Generic[_WPL, _NT]):
    """Phantom: wizard at a pre-subclass level (0–1). SubclassT is always None."""

    @classmethod
    def __class_getitem__(cls, params: object) -> types.GenericAlias:
        return types.GenericAlias(
            cls, params if isinstance(params, tuple) else (params,)
        )


class WizardSubclassLevel(Generic[_WSL, _WSS]):
    """Phantom: wizard at a post-subclass level (2–20) with assigned subclass."""

    @classmethod
    def __class_getitem__(cls, params: object) -> types.GenericAlias:
        return types.GenericAlias(
            cls, params if isinstance(params, tuple) else (params,)
        )


class SorcererPreSubclassLevel(Generic[_SPL, _NT]):
    """Phantom: sorcerer at pre-subclass level (0). SubclassT is always None."""

    @classmethod
    def __class_getitem__(cls, params: object) -> types.GenericAlias:
        return types.GenericAlias(
            cls, params if isinstance(params, tuple) else (params,)
        )


class SorcererSubclassLevel(Generic[_SSL, _SSS]):
    """Phantom: sorcerer at a post-subclass level (1–20) with assigned subclass."""

    @classmethod
    def __class_getitem__(cls, params: object) -> types.GenericAlias:
        return types.GenericAlias(
            cls, params if isinstance(params, tuple) else (params,)
        )


class ClassPreSubclassLevel(Generic[_CPL, _NT]):
    """Phantom: standard class (subclass at 3) at a pre-subclass level (0–2)."""

    @classmethod
    def __class_getitem__(cls, params: object) -> types.GenericAlias:
        return types.GenericAlias(
            cls, params if isinstance(params, tuple) else (params,)
        )


class ClassSubclassLevel(Generic[_CSL, _CSS]):
    """Phantom: standard class (subclass at 3) at a post-subclass level (3–20)."""

    @classmethod
    def __class_getitem__(cls, params: object) -> types.GenericAlias:
        return types.GenericAlias(
            cls, params if isinstance(params, tuple) else (params,)
        )


# Type aliases for Blueprint dimension bounds — use these in method-level TypeVar bounds.
type MaybeRace = Race | None
type MaybeStats = Stats | None
type MaybeHealth = PositiveInt | None
type AnyStatChoices = Literal[0] | PositiveInt
type AnyWizardLevel = (
    WizardPreSubclassLevel[SecondSubclassPreLevel, None]
    | WizardSubclassLevel[SecondSubclassPostLevel, WizardSubclass]
)
type AnySorcererLevel = (
    SorcererPreSubclassLevel[FirstSubclassPreLevel, None]
    | SorcererSubclassLevel[FirstSubclassPostLevel, SorcererSubclass]
)
type AnyClassLevel = (
    ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass]
)
type MaybeCharacterData = CharacterData | None


# Pass-through TypeVars for all Blueprint dimensions.
_RK = TypeVar("_RK", bound=Race | None)
_StK = TypeVar("_StK", bound=Stats | None)
_HeK = TypeVar("_HeK", bound=PositiveInt | None)
_StCK = TypeVar("_StCK", bound=Literal[0] | PositiveInt)
_SkCK = TypeVar("_SkCK", bound=Literal[0] | PositiveInt)
_WZK = TypeVar(
    "_WZK",
    bound=WizardPreSubclassLevel[SecondSubclassPreLevel, None]
    | WizardSubclassLevel[SecondSubclassPostLevel, WizardSubclass],
)
_SOK = TypeVar(
    "_SOK",
    bound=SorcererPreSubclassLevel[FirstSubclassPreLevel, None]
    | SorcererSubclassLevel[FirstSubclassPostLevel, SorcererSubclass],
)
_FGK = TypeVar(
    "_FGK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_BAK = TypeVar(
    "_BAK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_ROK = TypeVar(
    "_ROK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_CLK = TypeVar(
    "_CLK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_DRK = TypeVar(
    "_DRK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_PAK = TypeVar(
    "_PAK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_RAK = TypeVar(
    "_RAK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_MOK = TypeVar(
    "_MOK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_BDK = TypeVar(
    "_BDK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_WAK = TypeVar(
    "_WAK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_ARK = TypeVar(
    "_ARK",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
)
_CDK = TypeVar("_CDK", bound=CharacterData | None)

# Covariant TypeVars for Blueprint class definition (frozen model = read-only fields).
_RK_co = TypeVar("_RK_co", bound=Race | None, covariant=True)
_StK_co = TypeVar("_StK_co", bound=Stats | None, covariant=True)
_HeK_co = TypeVar("_HeK_co", bound=PositiveInt | None, covariant=True)
_StCK_co = TypeVar("_StCK_co", bound=Literal[0] | PositiveInt, covariant=True)
_SkCK_co = TypeVar("_SkCK_co", bound=Literal[0] | PositiveInt, covariant=True)
_WZK_co = TypeVar(
    "_WZK_co",
    bound=WizardPreSubclassLevel[SecondSubclassPreLevel, None]
    | WizardSubclassLevel[SecondSubclassPostLevel, WizardSubclass],
    covariant=True,
)
_SOK_co = TypeVar(
    "_SOK_co",
    bound=SorcererPreSubclassLevel[FirstSubclassPreLevel, None]
    | SorcererSubclassLevel[FirstSubclassPostLevel, SorcererSubclass],
    covariant=True,
)
_FGK_co = TypeVar(
    "_FGK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_BAK_co = TypeVar(
    "_BAK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_ROK_co = TypeVar(
    "_ROK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_CLK_co = TypeVar(
    "_CLK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_DRK_co = TypeVar(
    "_DRK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_PAK_co = TypeVar(
    "_PAK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_RAK_co = TypeVar(
    "_RAK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_MOK_co = TypeVar(
    "_MOK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_BDK_co = TypeVar(
    "_BDK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_WAK_co = TypeVar(
    "_WAK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_ARK_co = TypeVar(
    "_ARK_co",
    bound=ClassPreSubclassLevel[ThirdSubclassPreLevel, None]
    | ClassSubclassLevel[ThirdSubclassPostLevel, AnySubclass],
    covariant=True,
)
_CDK_co = TypeVar("_CDK_co", bound=CharacterData | None, covariant=True)

__all__ = [
    "Level",
    "FirstSubclassPreLevel",
    "FirstSubclassPostLevel",
    "SecondSubclassPreLevel",
    "SecondSubclassPostLevel",
    "ThirdSubclassPreLevel",
    "ThirdSubclassPostLevel",
    "WizardPreSubclassLevel",
    "WizardSubclassLevel",
    "SorcererPreSubclassLevel",
    "SorcererSubclassLevel",
    "ClassPreSubclassLevel",
    "ClassSubclassLevel",
    "_RK",
    "_StK",
    "_HeK",
    "_StCK",
    "_SkCK",
    "_WZK",
    "_SOK",
    "_FGK",
    "_BAK",
    "_ROK",
    "_CLK",
    "_DRK",
    "_PAK",
    "_RAK",
    "_MOK",
    "_BDK",
    "_WAK",
    "_ARK",
    "_CDK",
    "_RK_co",
    "_StK_co",
    "_HeK_co",
    "_StCK_co",
    "_SkCK_co",
    "_WZK_co",
    "_SOK_co",
    "_FGK_co",
    "_BAK_co",
    "_ROK_co",
    "_CLK_co",
    "_DRK_co",
    "_PAK_co",
    "_RAK_co",
    "_MOK_co",
    "_BDK_co",
    "_WAK_co",
    "_ARK_co",
    "_CDK_co",
    "WizardSubclass",
    "SorcererSubclass",
    "MaybeRace",
    "MaybeStats",
    "MaybeHealth",
    "AnyStatChoices",
    "AnyWizardLevel",
    "AnySorcererLevel",
    "AnyClassLevel",
    "MaybeCharacterData",
]
