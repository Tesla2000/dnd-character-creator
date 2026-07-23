from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, Literal, Self

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import Action
from dnd.character.actions._damage_type import DamageType
from dnd.character.actions._melee_attack import _MeleeAttackExecutor
from dnd.choices.equipment_creation.weapons import HitDieSize
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class _BeastMeleeAttack(Action[SlotT], Generic[SlotT], ABC):
    range_tails: Literal[1] = 1
    actor_slot: SlotT
    executor: _MeleeAttackExecutor[SlotT]

    @classmethod
    @abstractmethod
    def _ability(cls) -> AbilityName: ...

    @classmethod
    @abstractmethod
    def _die(cls) -> HitDieSize: ...

    @classmethod
    @abstractmethod
    def _n_dice(cls) -> int: ...

    @classmethod
    @abstractmethod
    def _damage_bonus(cls) -> int: ...

    @classmethod
    @abstractmethod
    def _damage_type(cls) -> DamageType: ...

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter[SlotT],
        battlemap: Battlemap[SlotT],
    ) -> tuple[Self, ...]:
        if (
            fighter.attacks_remaining <= 0
            or cls._ability() not in fighter.active_features
        ):
            return ()
        fx, fy = fighter.position.x, fighter.position.y
        results: list[Self] = []
        for target_slot in battlemap.all_slots():
            match battlemap.get_combatant(target_slot):
                case FightCharacter() as target if target.position != fighter.position:
                    tx, ty = target.position.x, target.position.y
                    if max(abs(tx - fx), abs(ty - fy)) <= 1:
                        results.append(
                            cls(
                                name=cls._ability(),
                                actor_slot=actor_slot,
                                executor=_MeleeAttackExecutor(
                                    actor_slot=actor_slot,
                                    target_slot=target_slot,
                                    die=cls._die(),
                                    n_dice=cls._n_dice(),
                                    damage_type=cls._damage_type(),
                                    ability_modifier=cls._damage_bonus(),
                                ),
                            )
                        )
                case _:
                    pass
        return tuple(results)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        return self.executor.attack(battlemap)
