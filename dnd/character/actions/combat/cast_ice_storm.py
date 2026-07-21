from __future__ import annotations

from random import randint
from typing import TYPE_CHECKING, Generic, Literal, Self

from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.actions.combat._negative_aoe import NegativeAoeAction
from dnd.choices.stats_creation.statistic import Statistic
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter, SpellcasterFightCharacter
from dnd.fight.terrain_modifier import AnyTerrainModifier, IceStormTerrainModifier

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class CastIceStorm(NegativeAoeAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.ICE_STORM] = AbilityName.ICE_STORM
    range_tails: Literal[300] = 300
    radius_tails: Literal[4] = 4
    center_position: Position

    @classmethod
    def _for_position(
        cls, actor_slot: SlotT, position: Position, spell_save_dc: int
    ) -> Self:
        return cls(
            actor_slot=actor_slot,
            center_position=position,
            spell_save_dc=spell_save_dc,
        )

    def hit_slots(self, battlemap: Battlemap[SlotT]) -> frozenset[SlotT]:
        cx, cy = self.center_position.x, self.center_position.y
        hit: set[SlotT] = set()
        for slot in battlemap.all_slots():
            if slot == self.actor_slot:
                continue
            match battlemap.get_combatant(slot):
                case FightCharacter() as combatant:
                    tx, ty = combatant.position.x, combatant.position.y
                    if max(abs(tx - cx), abs(ty - cy)) <= self.radius_tails:
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
    ) -> tuple[CastIceStorm[SlotT], ...]:
        if not isinstance(fighter, SpellcasterFightCharacter):
            return ()
        if not fighter.has_action:
            return ()
        if fighter.remaining_spell_slots.level_4 == 0:
            return ()
        if AbilityName.ICE_STORM not in fighter.character.actions:
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
            self.actor_slot, fighter.spend_action().spend_level_4_slot()
        )
        damage = sum(randint(1, 8) for _ in range(2)) + sum(
            randint(1, 6) for _ in range(4)
        )
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
        new_cells = IceStormTerrainModifier.sphere(
            center=Position(x=self.center_position.x, y=self.center_position.y),
            radius_tails=self.radius_tails,
            caster_slot=self.actor_slot,
        )
        merged: dict[Position, tuple[AnyTerrainModifier[SlotT], ...]] = dict(
            battlemap.terrain
        )
        for position, modifier in new_cells.items():
            merged[position] = merged.get(position, ()) + (modifier,)
        battlemap = battlemap.model_copy(update={"terrain": merged})
        return battlemap
