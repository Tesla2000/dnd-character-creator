from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, Self

from pydantic import PositiveInt

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import Action
from dnd.character.actions._damage_type import DamageType
from dnd.character.actions._melee_attack import _MeleeAttackExecutor
from dnd.choices.equipment_creation.weapons import HitDieSize, WeaponName
from dnd.choices.stats_creation.statistic import Statistic
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class _RangedAttackExecutor(_MeleeAttackExecutor[SlotT], Generic[SlotT]):
    long_range: bool = False

    def _compute_use_disadvantage(
        self, fighter: FightCharacter[SlotT], target: FightCharacter[SlotT]
    ) -> bool:
        return super()._compute_use_disadvantage(fighter, target) or self.long_range


class _RangedAttack(Action[SlotT], Generic[SlotT]):
    range_tails: PositiveInt
    actor_slot: SlotT
    executor: _RangedAttackExecutor[SlotT]

    @classmethod
    @abstractmethod
    def _damage_die(cls) -> HitDieSize: ...

    @classmethod
    @abstractmethod
    def _ability(cls) -> AbilityName: ...

    @classmethod
    @abstractmethod
    def _weapon(cls) -> WeaponName: ...

    @classmethod
    @abstractmethod
    def _two_handed(cls) -> bool: ...

    @classmethod
    @abstractmethod
    def _damage_type(cls) -> DamageType: ...

    @classmethod
    @abstractmethod
    def _normal_range_tails(cls) -> int: ...

    @classmethod
    @abstractmethod
    def _long_range_tails(cls) -> int: ...

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter[SlotT],
        battlemap: Battlemap[SlotT],
    ) -> tuple[Self, ...]:
        if (
            fighter.attacks_remaining <= 0
            or cls._ability() not in fighter.character.actions
        ):
            return ()
        weapon = cls._weapon()
        if cls._two_handed():
            if fighter.main_hand != weapon or fighter.off_hand != weapon:
                return ()
        else:
            if fighter.main_hand != weapon and fighter.off_hand != weapon:
                return ()
        fx, fy = fighter.position.x, fighter.position.y
        die = cls._damage_die()
        damage_type = cls._damage_type()
        ability_modifier = fighter.character.stats.get_modifier(Statistic.DEXTERITY)
        can_sneak_attack = AbilityName.SNEAK_ATTACK in fighter.character.actions
        results: list[Self] = []
        for target_slot in battlemap.all_slots():
            target = battlemap.get_combatant(target_slot)
            if (
                not isinstance(target, FightCharacter)
                or target.position == fighter.position
            ):
                continue
            tx, ty = target.position.x, target.position.y
            dist = max(abs(tx - fx), abs(ty - fy))
            if dist > cls._long_range_tails():
                continue
            long_range = dist > cls._normal_range_tails()
            results.append(
                cls(
                    name=cls._ability(),
                    range_tails=dist,
                    actor_slot=actor_slot,
                    executor=_RangedAttackExecutor(
                        actor_slot=actor_slot,
                        target_slot=target_slot,
                        die=die,
                        damage_type=damage_type,
                        ability_modifier=ability_modifier,
                        long_range=long_range,
                        can_sneak_attack=can_sneak_attack,
                    ),
                )
            )
        return tuple(results)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        return self.executor.attack(battlemap)
