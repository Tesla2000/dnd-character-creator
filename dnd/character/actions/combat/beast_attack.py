from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal, Self

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import Action
from dnd.character.actions._damage_type import DamageType
from dnd.character.actions._melee_attack import _MeleeAttackExecutor
from dnd.character.actions.combat._wild_shape_forms import (
    primary_attack_for_druid_level,
)
from dnd.choices.equipment_creation.weapons import HitDieSize
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class BeastAttack(Action[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.BEAST_ATTACK] = AbilityName.BEAST_ATTACK
    range_tails: Literal[1] = 1
    actor_slot: SlotT
    executor: _MeleeAttackExecutor[SlotT]

    @classmethod
    def create(
        cls, actor_slot: SlotT, fighter: FightCharacter, battlemap: Battlemap[SlotT]
    ) -> tuple[Self, ...]:
        if (
            fighter.attacks_remaining <= 0
            or AbilityName.WILD_SHAPE not in fighter.active_features
        ):
            return ()
        atk = primary_attack_for_druid_level(fighter.character.classes.druid)
        damage_type = (
            DamageType.MAGICAL_SLASHING
            if AbilityName.PRIMAL_STRIKE in fighter.character.actions
            else DamageType.SLASHING
        )
        fx, fy = fighter.position.x, fighter.position.y
        results: list[Self] = []
        for target_slot in battlemap.all_slots():
            match battlemap.get_combatant(target_slot):
                case FightCharacter() as target if target.position != fighter.position:
                    tx, ty = target.position.x, target.position.y
                    if max(abs(tx - fx), abs(ty - fy)) <= 1:
                        results.append(
                            cls(
                                actor_slot=actor_slot,
                                executor=_MeleeAttackExecutor(
                                    actor_slot=actor_slot,
                                    target_slot=target_slot,
                                    die=HitDieSize(atk.dice_size),
                                    n_dice=atk.n_dice,
                                    damage_type=damage_type,
                                    ability_modifier=atk.damage_bonus,
                                ),
                            )
                        )
                case _:
                    pass
        return tuple(results)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        return self.executor.attack(battlemap)
