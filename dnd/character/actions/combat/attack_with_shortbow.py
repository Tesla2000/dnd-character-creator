from __future__ import annotations

from typing import Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._damage_type import DamageType
from dnd.character.actions._ranged_attack import _RangedAttack
from dnd.choices.equipment_creation.weapons import HitDieSize, WeaponName
from dnd.fight._combatant_slot import SlotT


class AttackWithShortbow(_RangedAttack[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.ATTACK_WITH_SHORTBOW] = AbilityName.ATTACK_WITH_SHORTBOW

    @classmethod
    def _damage_die(cls) -> HitDieSize:
        return HitDieSize.SIX

    @classmethod
    def _ability(cls) -> AbilityName:
        return AbilityName.ATTACK_WITH_SHORTBOW

    @classmethod
    def _weapon(cls) -> WeaponName:
        return WeaponName.SHORTBOW

    @classmethod
    def _two_handed(cls) -> bool:
        return True

    @classmethod
    def _damage_type(cls) -> DamageType:
        return DamageType.PIERCING

    @classmethod
    def _normal_range_tails(cls) -> int:
        return 16

    @classmethod
    def _long_range_tails(cls) -> int:
        return 64
