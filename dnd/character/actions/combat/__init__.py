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
from dnd.character.actions.combat.attack_with_brown_bear_claw import (
    AttackWithBrownBearClaw,
)
from dnd.character.actions.combat.attack_with_dagger import AttackWithDagger
from dnd.character.actions.combat.attack_with_greataxe import AttackWithGreataxe
from dnd.character.actions.combat.attack_with_hand_crossbow import (
    AttackWithHandCrossbow,
)
from dnd.character.actions.combat.attack_with_handaxe import AttackWithHandaxe
from dnd.character.actions.combat.attack_with_polar_bear_claw import (
    AttackWithPolarBearClaw,
)
from dnd.character.actions.combat.attack_with_rapier import AttackWithRapier
from dnd.character.actions.combat.attack_with_shortbow import AttackWithShortbow
from dnd.character.actions.combat.attack_with_shortsword import AttackWithShortsword
from dnd.character.actions.combat.attack_with_wolf_bite import AttackWithWolfBite
from dnd.character.actions.combat.cast_chromatic_orb import CastChromaticOrb
from dnd.character.actions.combat.cast_conjure_animals import CastConjureAnimals
from dnd.character.actions.combat.cast_fire_bolt import CastFireBolt
from dnd.character.actions.combat.cast_fireball import CastFireball
from dnd.character.actions.combat.cast_ice_storm import CastIceStorm
from dnd.character.actions.combat.cast_lightning_bolt import CastLightningBolt
from dnd.character.actions.combat.cast_magic_missile import CastMagicMissile
from dnd.character.actions.combat.cast_scorching_ray import CastScorchingRay
from dnd.character.actions.combat.command_summoned_beast import CommandSummonedBeast
from dnd.character.actions.combat.dash import Dash
from dnd.character.actions.combat.disengage import Disengage
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
    AttackWithBrownBearClaw[T],
    AttackWithDagger[T],
    AttackWithGreataxe[T],
    AttackWithHandCrossbow[T],
    AttackWithHandaxe[T],
    AttackWithPolarBearClaw[T],
    AttackWithRapier[T],
    AttackWithShortbow[T],
    AttackWithShortsword[T],
    AttackWithWolfBite[T],
    CastChromaticOrb[T],
    CastConjureAnimals[T],
    CastFireBolt[T],
    CastFireball[T],
    CastIceStorm[T],
    CastLightningBolt[T],
    CastMagicMissile[T],
    CastScorchingRay[T],
    CommandSummonedBeast[T],
    Dash[T],
    Disengage[T],
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
    "AttackWithBrownBearClaw",
    "AttackWithDagger",
    "AttackWithGreataxe",
    "AttackWithHandCrossbow",
    "AttackWithHandaxe",
    "AttackWithPolarBearClaw",
    "AttackWithRapier",
    "AttackWithShortbow",
    "AttackWithShortsword",
    "AttackWithWolfBite",
    "BaseAction",
    "BonusAction",
    "CastChromaticOrb",
    "CastConjureAnimals",
    "CastFireBolt",
    "CastFireball",
    "CastIceStorm",
    "CastLightningBolt",
    "CastMagicMissile",
    "CastScorchingRay",
    "CombatAction",
    "CommandSummonedBeast",
    "Dash",
    "Disengage",
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
