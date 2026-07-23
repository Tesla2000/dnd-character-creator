from __future__ import annotations

from abc import ABC, abstractmethod
from random import randint
from typing import ClassVar, Generic, Self, cast

from pydantic import BaseModel, ConfigDict, Field

from dnd._position import Position
from dnd.fight._combat_event import (
    AnyCombatEvent,
    ConcentrationBrokenEvent,
    RoundEndEvent,
    RoundStartEvent,
    TurnEndEvent,
    TurnStartEvent,
)
from dnd.fight._combatant_slot import SlotT
from dnd.fight._condition import Condition
from dnd.fight._terrain_type import TerrainType
from dnd.fight.fight_character import (
    AnyActiveCombatant,
    FightCharacter,
    UnsummonedFightCharacter,
)
from dnd.fight.terrain_modifier import AnyTerrainModifier


class Battlemap(BaseModel, Generic[SlotT], ABC):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    event_log: tuple[AnyCombatEvent[SlotT], ...] = ()
    terrain_height: dict[tuple[int, int], int] = Field(default_factory=dict)
    terrain: dict[Position, tuple[AnyTerrainModifier[SlotT], ...]] = Field(
        default_factory=dict
    )

    def terrain_height_at(self, x: int, y: int) -> int:
        return self.terrain_height.get((x, y), 0)

    def relative_height_at(self, position: Position) -> int:
        return position.height - self.terrain_height_at(position.x, position.y)

    def terrain_at(self, position: Position) -> TerrainType:
        if self.relative_height_at(position) != 0:
            return TerrainType.NORMAL
        ground = Position(x=position.x, y=position.y)
        for modifier in self.terrain.get(ground, ()):
            if modifier.terrain_type() is TerrainType.DIFFICULT:
                return TerrainType.DIFFICULT
        return TerrainType.NORMAL

    def all_slots(self) -> tuple[SlotT, ...]:
        for base in type(self).__mro__:
            if (
                issubclass(base, Battlemap)
                and base.__pydantic_generic_metadata__["args"]
            ):
                slot_type = cast(
                    type[SlotT], base.__pydantic_generic_metadata__["args"][0]
                )
                return tuple(slot_type)
        return ()

    @abstractmethod
    def get_combatant(self, slot: SlotT) -> AnyActiveCombatant[SlotT]: ...

    @abstractmethod
    def replace_combatant(
        self, slot: SlotT, updated: AnyActiveCombatant[SlotT]
    ) -> Self: ...

    def emit(self, event: AnyCombatEvent[SlotT]) -> Self:
        result: Self = self.model_copy(
            update={"event_log": self.event_log + (event,)}
        )

        for slot in result.all_slots():
            combatant = result.get_combatant(slot)
            updated, emitted = combatant.on_event(event)
            result = result.replace_combatant(slot, updated)
            for follow_up in emitted:
                result = result.emit(follow_up)

        distinct: dict[int, AnyTerrainModifier[SlotT]] = {
            id(modifier): modifier
            for modifiers in result.terrain.values()
            for modifier in modifiers
        }
        survivors: dict[int, AnyTerrainModifier[SlotT] | None] = {}
        for modifier_id, modifier in distinct.items():
            updated_modifier, emitted = modifier.on_event(event)
            survivors[modifier_id] = updated_modifier
            for follow_up in emitted:
                result = result.emit(follow_up)

        new_terrain: dict[Position, tuple[AnyTerrainModifier[SlotT], ...]] = {}
        for position, modifiers in result.terrain.items():
            surviving = tuple(
                survivors[id(modifier)] if id(modifier) in survivors else modifier
                for modifier in modifiers
            )
            surviving = tuple(modifier for modifier in surviving if modifier is not None)
            if surviving:
                new_terrain[position] = surviving

        return result.model_copy(update={"terrain": new_terrain})

    def has_progress_since(self, index: int) -> bool:
        bookkeeping = (TurnStartEvent, TurnEndEvent, RoundStartEvent, RoundEndEvent)
        return any(
            not isinstance(event, bookkeeping) for event in self.event_log[index:]
        )

    def deal_damage(self, slot: SlotT, amount: int) -> Self:
        match self.get_combatant(slot):
            case FightCharacter() as combatant:
                pass
            case _:
                return self
        was_concentrating = Condition.CONCENTRATION in combatant.conditions
        result: Self = self.replace_combatant(slot, combatant.take_damage(amount))
        if not was_concentrating:
            return result

        match result.get_combatant(slot):
            case FightCharacter() as survivor:
                dc = max(10, amount // 2)
                roll = randint(1, 20) + survivor.con_save_bonus
                save_failed = roll < dc
                if save_failed:
                    result = result.replace_combatant(
                        slot, survivor.remove_condition(Condition.CONCENTRATION)
                    )
            case _:
                save_failed = True

        if not save_failed:
            return result

        result = result.emit(ConcentrationBrokenEvent(caster_slot=slot))
        for other_slot in result.all_slots():
            match result.get_combatant(other_slot):
                case FightCharacter() as summon if summon.summoned_by == slot:
                    result = result.replace_combatant(
                        other_slot, UnsummonedFightCharacter.from_vanished(summon)
                    )
                case _:
                    pass
        return result

    def reset_summoned_creatures(self, caster_slot: SlotT) -> Self:
        result: Self = self
        for slot in result.all_slots():
            match result.get_combatant(slot):
                case FightCharacter() as summon if summon.summoned_by == caster_slot:
                    updated = summon.model_copy(
                        update={
                            "has_action": True,
                            "has_bonus_action": True,
                            "has_reaction": True,
                            "attacks_remaining": summon.number_of_attacks,
                        }
                    )
                    result = result.replace_combatant(slot, updated)
                case _:
                    pass
        return result
