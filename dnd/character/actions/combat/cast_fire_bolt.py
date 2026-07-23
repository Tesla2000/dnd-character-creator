from __future__ import annotations

from random import randint
from typing import TYPE_CHECKING, Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import Action
from dnd.character.actions._damage_type import DamageType
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter, SpellcasterFightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class CastFireBolt(Action[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.FIRE_BOLT] = AbilityName.FIRE_BOLT
    range_tails: Literal[24] = 24
    damage_type: Literal[DamageType.FIRE] = DamageType.FIRE
    actor_slot: SlotT
    target_slot: SlotT
    spell_attack_bonus: int

    @staticmethod
    def _damage_dice(level: int) -> int:
        if level >= 17:
            return 4
        if level >= 11:
            return 3
        if level >= 5:
            return 2
        return 1

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter[SlotT],
        battlemap: Battlemap[SlotT],
    ) -> tuple[CastFireBolt[SlotT], ...]:
        if not isinstance(fighter, SpellcasterFightCharacter):
            return ()
        if not fighter.has_action:
            return ()
        if AbilityName.FIRE_BOLT not in fighter.character.actions:
            return ()
        spell_attack_bonus = sum(
            m.apply(fighter.character)
            for m in fighter.character.spell_attack_bonus_modifiers
        )
        results: list[CastFireBolt[SlotT]] = []
        for target_slot in battlemap.all_slots():
            if target_slot == actor_slot:
                continue
            results.append(
                cls(
                    actor_slot=actor_slot,
                    target_slot=target_slot,
                    spell_attack_bonus=spell_attack_bonus,
                )
            )
        return tuple(results)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        fighter = battlemap.get_combatant(self.actor_slot)
        if not isinstance(fighter, SpellcasterFightCharacter):
            return battlemap
        battlemap = battlemap.replace_combatant(
            self.actor_slot, fighter.spend_action()
        )
        target = battlemap.get_combatant(self.target_slot)
        if not isinstance(target, FightCharacter):
            return battlemap
        roll = randint(1, 20) + self.spell_attack_bonus
        if roll < target.ac:
            return battlemap
        n_dice = self._damage_dice(fighter.character.level)
        damage = sum(randint(1, 10) for _ in range(n_dice))
        if self.damage_type in target.all_resistances():
            damage //= 2
        return battlemap.deal_damage(self.target_slot, damage)
