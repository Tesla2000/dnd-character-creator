from enum import IntEnum
from typing import Union

from dnd.character.actions._base_action import (
    Action,
    BaseAction,
    BonusAction,
    CombatAction,
    FreeAction,
    MovementAction,
)
from dnd.character.actions.combat._negative_aoe import NegativeAoeAction
from dnd.character.actions.combat.attack_with_axe import AttackWithAxe
from dnd.character.actions.combat.attack_with_battleaxe import AttackWithBattleaxe
from dnd.character.actions.combat.attack_with_greataxe import AttackWithGreataxe
from dnd.character.actions.combat.attack_with_handaxe import AttackWithHandaxe
from dnd.character.actions.combat.beast_attack import BeastAttack
from dnd.character.actions.combat.cast_chromatic_orb import CastChromaticOrb
from dnd.character.actions.combat.cast_fireball import CastFireball
from dnd.character.actions.combat.cast_ice_storm import CastIceStorm
from dnd.character.actions.combat.cast_lightning_bolt import CastLightningBolt
from dnd.character.actions.combat.cast_magic_missile import CastMagicMissile
from dnd.character.actions.combat.cast_scorching_ray import CastScorchingRay
from dnd.character.actions.combat.draw_item import DrawItem
from dnd.character.actions.combat.drop_item import DropItem
from dnd.character.actions.combat.move import Move
from dnd.character.actions.combat.pass_turn import Pass
from dnd.character.actions.combat.revert_wild_shape import RevertWildShape
from dnd.character.actions.combat.use_rage import UseRage
from dnd.character.actions.combat.use_reckless_attack import UseRecklessAttack
from dnd.character.actions.combat.use_wild_shape import UseWildShape

type AnyCombatAction[T: IntEnum] = Union[
    AttackWithAxe[T],
    AttackWithBattleaxe[T],
    AttackWithGreataxe[T],
    AttackWithHandaxe[T],
    BeastAttack[T],
    CastChromaticOrb[T],
    CastFireball[T],
    CastIceStorm[T],
    CastLightningBolt[T],
    CastMagicMissile[T],
    CastScorchingRay[T],
    DrawItem[T],
    DropItem[T],
    Move[T],
    Pass[T],
    RevertWildShape[T],
    UseRage[T],
    UseRecklessAttack[T],
    UseWildShape[T],
]

__all__ = [
    "Action",
    "AnyCombatAction",
    "AttackWithAxe",
    "AttackWithBattleaxe",
    "AttackWithGreataxe",
    "AttackWithHandaxe",
    "BaseAction",
    "BeastAttack",
    "BonusAction",
    "CastChromaticOrb",
    "CastFireball",
    "CastIceStorm",
    "CastLightningBolt",
    "CastMagicMissile",
    "CastScorchingRay",
    "CombatAction",
    "DrawItem",
    "DropItem",
    "FreeAction",
    "Move",
    "MovementAction",
    "NegativeAoeAction",
    "Pass",
    "RevertWildShape",
    "UseRage",
    "UseRecklessAttack",
    "UseWildShape",
]
