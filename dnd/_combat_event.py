from enum import IntEnum, StrEnum, auto
from typing import Annotated, Literal, Union

from pydantic import BaseModel, ConfigDict, Field
from uuid_string import UUIDString

from dnd._position import Position
from dnd.character._ability_name import AbilityName


class CombatEventType(StrEnum):
    RAGE_ENDS = auto()
    TURN_START = auto()
    TURN_END = auto()
    ROUND_START = auto()
    ROUND_END = auto()
    CREATURE_TARGETED = auto()
    CREATURE_ATTACKED = auto()
    MELEE_DAMAGE = auto()
    OPPORTUNITY_ATTACK = auto()
    MOVEMENT = auto()
    ACTION_TAKEN = auto()
    CONCENTRATION_BROKEN = auto()


class RageEndsEvent(BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.RAGE_ENDS] = CombatEventType.RAGE_ENDS
    target_id: UUIDString


class TurnStartEvent(BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.TURN_START] = CombatEventType.TURN_START
    target_id: UUIDString


class TurnEndEvent[SlotT: IntEnum](BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.TURN_END] = CombatEventType.TURN_END
    actor_slot: SlotT


class RoundStartEvent(BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.ROUND_START] = CombatEventType.ROUND_START


class RoundEndEvent(BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.ROUND_END] = CombatEventType.ROUND_END


class CreatureTargetedEvent(BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.CREATURE_TARGETED] = CombatEventType.CREATURE_TARGETED
    attacker_id: UUIDString
    defender_id: UUIDString
    attack_id: UUIDString


class CreatureAttackedEvent(BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.CREATURE_ATTACKED] = CombatEventType.CREATURE_ATTACKED
    attacker_id: UUIDString
    defender_id: UUIDString
    roll: int
    total_bonus: int
    is_crit: bool
    attack_id: UUIDString


class MeleeDamageEvent(BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.MELEE_DAMAGE] = CombatEventType.MELEE_DAMAGE
    attacker_id: UUIDString
    defender_id: UUIDString
    damage: int
    is_crit: bool
    attack_id: UUIDString


class OpportunityAttackEvent[SlotT: IntEnum](BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.OPPORTUNITY_ATTACK] = (
        CombatEventType.OPPORTUNITY_ATTACK
    )
    attacker_slot: SlotT
    target_slot: SlotT


class MovementEvent[SlotT: IntEnum](BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.MOVEMENT] = CombatEventType.MOVEMENT
    mover_slot: SlotT
    to: Position


class ActionTakenEvent[SlotT: IntEnum](BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.ACTION_TAKEN] = CombatEventType.ACTION_TAKEN
    actor_slot: SlotT
    action_name: AbilityName


class ConcentrationBrokenEvent[SlotT: IntEnum](BaseModel):
    model_config = ConfigDict(frozen=True)
    type: Literal[CombatEventType.CONCENTRATION_BROKEN] = (
        CombatEventType.CONCENTRATION_BROKEN
    )
    caster_slot: SlotT


type AnyCombatEvent[SlotT: IntEnum] = Annotated[
    Union[
        RageEndsEvent,
        TurnStartEvent,
        TurnEndEvent[SlotT],
        RoundStartEvent,
        RoundEndEvent,
        CreatureTargetedEvent,
        CreatureAttackedEvent,
        MeleeDamageEvent,
        OpportunityAttackEvent[SlotT],
        MovementEvent[SlotT],
        ActionTakenEvent[SlotT],
        ConcentrationBrokenEvent[SlotT],
    ],
    Field(discriminator="type"),
]

__all__ = [
    "ActionTakenEvent",
    "AnyCombatEvent",
    "CombatEventType",
    "ConcentrationBrokenEvent",
    "CreatureAttackedEvent",
    "CreatureTargetedEvent",
    "MeleeDamageEvent",
    "MovementEvent",
    "OpportunityAttackEvent",
    "RageEndsEvent",
    "RoundEndEvent",
    "RoundStartEvent",
    "TurnEndEvent",
    "TurnStartEvent",
]
