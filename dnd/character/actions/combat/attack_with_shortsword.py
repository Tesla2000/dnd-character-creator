from __future__ import annotations

from typing import Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._damage_type import DamageType
from dnd.character.actions._melee_attack import _MeleeAttack
from dnd.choices.equipment_creation.weapons import HitDieSize, WeaponName
from dnd.choices.stats_creation.statistic import Statistic
from dnd.fight._combatant_slot import SlotT


class AttackWithShortsword(_MeleeAttack[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.ATTACK_WITH_SHORTSWORD] = (
        AbilityName.ATTACK_WITH_SHORTSWORD
    )

    @classmethod
    def _damage_die(cls) -> HitDieSize:
        return HitDieSize.SIX

    @classmethod
    def _ability(cls) -> AbilityName:
        return AbilityName.ATTACK_WITH_SHORTSWORD

    @classmethod
    def _weapon(cls) -> WeaponName:
        return WeaponName.SHORTSWORD

    @classmethod
    def _two_handed(cls) -> bool:
        return False

    @classmethod
    def _stat(cls) -> Statistic:
        return Statistic.DEXTERITY

    @classmethod
    def _damage_type(cls) -> DamageType:
        return DamageType.PIERCING

    @classmethod
    def _finesse(cls) -> bool:
        return True
