from __future__ import annotations

from typing import Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._beast_melee_attack import _BeastMeleeAttack
from dnd.character.actions._damage_type import DamageType
from dnd.choices.equipment_creation.weapons import HitDieSize
from dnd.fight._combatant_slot import SlotT


class AttackWithWolfBite(_BeastMeleeAttack[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.ATTACK_WITH_WOLF_BITE] = AbilityName.ATTACK_WITH_WOLF_BITE

    @classmethod
    def _ability(cls) -> AbilityName:
        return AbilityName.ATTACK_WITH_WOLF_BITE

    @classmethod
    def _die(cls) -> HitDieSize:
        return HitDieSize.FOUR

    @classmethod
    def _n_dice(cls) -> int:
        return 2

    @classmethod
    def _damage_bonus(cls) -> int:
        return 2

    @classmethod
    def _damage_type(cls) -> DamageType:
        return DamageType.PIERCING
