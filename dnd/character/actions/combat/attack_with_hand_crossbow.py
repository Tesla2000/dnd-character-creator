from __future__ import annotations

from typing import Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._damage_type import DamageType
from dnd.character.actions._ranged_attack import _RangedAttack
from dnd.choices.equipment_creation.weapons import HitDieSize, WeaponName
from dnd.fight._combatant_slot import SlotT


class AttackWithHandCrossbow(_RangedAttack[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.ATTACK_WITH_HAND_CROSSBOW] = (
        AbilityName.ATTACK_WITH_HAND_CROSSBOW
    )

    @classmethod
    def _damage_die(cls) -> HitDieSize:
        return HitDieSize.SIX

    @classmethod
    def _ability(cls) -> AbilityName:
        return AbilityName.ATTACK_WITH_HAND_CROSSBOW

    @classmethod
    def _weapon(cls) -> WeaponName:
        return WeaponName.CROSSBOW_HAND

    @classmethod
    def _two_handed(cls) -> bool:
        return False

    @classmethod
    def _damage_type(cls) -> DamageType:
        return DamageType.PIERCING

    @classmethod
    def _normal_range_tails(cls) -> int:
        return 6

    @classmethod
    def _long_range_tails(cls) -> int:
        return 24
