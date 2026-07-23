from __future__ import annotations

from typing import Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._beast_melee_attack import _BeastMeleeAttack
from dnd.character.actions._damage_type import DamageType
from dnd.choices.equipment_creation.weapons import HitDieSize
from dnd.fight._combatant_slot import SlotT


class AttackWithPolarBearClaw(_BeastMeleeAttack[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.ATTACK_WITH_POLAR_BEAR_CLAW] = (
        AbilityName.ATTACK_WITH_POLAR_BEAR_CLAW
    )

    @classmethod
    def _ability(cls) -> AbilityName:
        return AbilityName.ATTACK_WITH_POLAR_BEAR_CLAW

    @classmethod
    def _die(cls) -> HitDieSize:
        return HitDieSize.SIX

    @classmethod
    def _n_dice(cls) -> int:
        return 2

    @classmethod
    def _damage_bonus(cls) -> int:
        return 5

    @classmethod
    def _damage_type(cls) -> DamageType:
        return DamageType.SLASHING
