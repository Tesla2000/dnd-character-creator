from __future__ import annotations

import math
from random import randint
from typing import TYPE_CHECKING, Generic, Literal, Self

from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.actions.combat._negative_aoe import NegativeAoeAction
from dnd.choices.stats_creation.statistic import Statistic
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter, SpellcasterFightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap

_LINE_HALF_WIDTH = 0.5


class CastLightningBolt(NegativeAoeAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.LIGHTNING_BOLT] = AbilityName.LIGHTNING_BOLT
    range_tails: Literal[0] = 0
    radius_tails: Literal[20] = 20
    end_position: Position

    @staticmethod
    def _distance_to_segment(
        px: float, py: float, ax: float, ay: float, bx: float, by: float
    ) -> float:
        dx, dy = bx - ax, by - ay
        length_sq = dx * dx + dy * dy
        if length_sq == 0:
            return math.hypot(px - ax, py - ay)
        t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / length_sq))
        closest_x, closest_y = ax + t * dx, ay + t * dy
        return math.hypot(px - closest_x, py - closest_y)

    @staticmethod
    def _clamp_endpoint(
        ax: float, ay: float, bx: float, by: float, max_length: float
    ) -> tuple[float, float]:
        dx, dy = bx - ax, by - ay
        distance = math.hypot(dx, dy)
        if distance <= max_length or distance == 0:
            return bx, by
        scale = max_length / distance
        return ax + dx * scale, ay + dy * scale

    @classmethod
    def _for_position(
        cls, actor_slot: SlotT, position: Position, spell_save_dc: int
    ) -> Self:
        return cls(
            actor_slot=actor_slot,
            end_position=position,
            spell_save_dc=spell_save_dc,
        )

    def hit_slots(self, battlemap: Battlemap[SlotT]) -> frozenset[SlotT]:
        match battlemap.get_combatant(self.actor_slot):
            case FightCharacter() as actor:
                pass
            case _:
                return frozenset()
        ax, ay = actor.position.x, actor.position.y
        bx, by = self._clamp_endpoint(
            ax, ay, self.end_position.x, self.end_position.y, self.radius_tails
        )
        hit: set[SlotT] = set()
        for slot in battlemap.all_slots():
            if slot == self.actor_slot:
                continue
            match battlemap.get_combatant(slot):
                case FightCharacter() as combatant:
                    tx, ty = combatant.position.x, combatant.position.y
                    if (
                        self._distance_to_segment(tx, ty, ax, ay, bx, by)
                        <= _LINE_HALF_WIDTH
                    ):
                        hit.add(slot)
                case _:
                    pass
        return frozenset(hit)

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter,
        battlemap: Battlemap[SlotT],
    ) -> tuple[CastLightningBolt[SlotT], ...]:
        if not isinstance(fighter, SpellcasterFightCharacter):
            return ()
        if not fighter.has_action:
            return ()
        if fighter.remaining_spell_slots.level_3 == 0:
            return ()
        if AbilityName.LIGHTNING_BOLT not in fighter.character.actions:
            return ()
        spell_save_dc = 8 + sum(
            m.apply(fighter.character)
            for m in fighter.character.spell_save_dc_modifiers
        )
        return cls.create_candidates(actor_slot, battlemap, spell_save_dc)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match battlemap.get_combatant(self.actor_slot):
            case SpellcasterFightCharacter() as fighter:
                pass
            case _:
                return battlemap
        battlemap = battlemap.replace_combatant(
            self.actor_slot, fighter.spend_action().spend_level_3_slot()
        )
        damage = sum(randint(1, 6) for _ in range(8))
        for slot in self.hit_slots(battlemap):
            match battlemap.get_combatant(slot):
                case FightCharacter() as combatant:
                    roll = (
                        randint(1, 20)
                        + combatant.character.saving_throw_modifiers[
                            Statistic.DEXTERITY
                        ]
                    )
                    hit_damage = damage if roll < self.spell_save_dc else damage // 2
                    battlemap = battlemap.replace_combatant(
                        slot, combatant.take_damage(hit_damage)
                    )
                case _:
                    pass
        return battlemap
