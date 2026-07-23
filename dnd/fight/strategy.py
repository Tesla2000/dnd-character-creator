import random
from collections import defaultdict
from typing import Annotated, ClassVar, Generic, Protocol

from pydantic import BaseModel, ConfigDict, Field

from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.actions.combat import AnyCombatAction
from dnd.character.actions.combat.draw_item import DrawItem
from dnd.character.actions.combat.drop_item import DropItem
from dnd.character.actions.combat.move import Move
from dnd.character.actions.combat.pass_turn import Pass
from dnd.fight._combatant_slot import SlotT
from dnd.fight.aspect import AnyAspect
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import FightCharacter

_FILLER_ACTIONS: tuple[type, ...] = (Pass, DropItem, DrawItem)


class Strategy(Protocol[SlotT]):
    def choose(
        self,
        candidates: tuple[AnyCombatAction[SlotT], ...],
        battlemap: Battlemap[SlotT],
        actor_slot: SlotT,
    ) -> AnyCombatAction[SlotT]: ...


class RandomStrategy(Generic[SlotT]):
    def choose(
        self,
        candidates: tuple[AnyCombatAction[SlotT], ...],
        battlemap: Battlemap[SlotT],
        actor_slot: SlotT,
    ) -> AnyCombatAction[SlotT]:
        return self._pick_uniform_by_ability(candidates)

    @staticmethod
    def _pick_uniform_by_ability(
        candidates: tuple[AnyCombatAction[SlotT], ...],
    ) -> AnyCombatAction[SlotT]:
        by_name: defaultdict[AbilityName, list[AnyCombatAction[SlotT]]] = defaultdict(
            list
        )
        for action in candidates:
            by_name[action.name].append(action)
        chosen_name = random.choice(list(by_name))
        return random.choice(by_name[chosen_name])


class AggressiveStrategy(RandomStrategy[SlotT], Generic[SlotT]):
    def choose(
        self,
        candidates: tuple[AnyCombatAction[SlotT], ...],
        battlemap: Battlemap[SlotT],
        actor_slot: SlotT,
    ) -> AnyCombatAction[SlotT]:
        move_actions: list[Move[SlotT]] = [
            a for a in candidates if isinstance(a, Move)
        ]
        if move_actions:
            match battlemap.get_combatant(actor_slot):
                case FightCharacter() as actor:
                    my_team = actor.team_id
                case _:
                    return super().choose(candidates, battlemap, actor_slot)
            enemy_positions: list[Position] = [
                battlemap.get_combatant(s).position
                for s in battlemap.all_slots()
                if isinstance(battlemap.get_combatant(s), FightCharacter)
                and battlemap.get_combatant(s).team_id != my_team
            ]
            if enemy_positions:
                return min(
                    move_actions,
                    key=lambda m: self._closest_enemy_distance(m, enemy_positions),
                )

        non_move = tuple(a for a in candidates if not isinstance(a, Move))
        if not non_move:
            return random.choice(candidates)

        useful = tuple(a for a in non_move if not isinstance(a, _FILLER_ACTIONS))
        if useful:
            return self._pick_uniform_by_ability(useful)

        pass_actions = tuple(a for a in non_move if isinstance(a, Pass))
        if pass_actions:
            return random.choice(pass_actions)

        return self._pick_uniform_by_ability(non_move)

    @staticmethod
    def _closest_enemy_distance(
        move: Move[SlotT], enemy_positions: list[Position]
    ) -> int:
        return min(
            max(abs(move.to.x - p.x), abs(move.to.y - p.y)) for p in enemy_positions
        )


class CompositeStrategy(BaseModel, Generic[SlotT]):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    aspects: Annotated[tuple[AnyAspect[SlotT], ...], Field(min_length=1)]

    def choose(
        self,
        candidates: tuple[AnyCombatAction[SlotT], ...],
        battlemap: Battlemap[SlotT],
        actor_slot: SlotT,
    ) -> AnyCombatAction[SlotT]:
        scored: list[tuple[float, AnyCombatAction[SlotT]]] = [
            (self._score(action, battlemap, actor_slot), action)
            for action in candidates
        ]
        best_score = max(score for score, _ in scored)
        best_actions = [action for score, action in scored if score == best_score]
        best_moves = [action for action in best_actions if isinstance(action, Move)]
        if best_moves:
            return min(best_moves, key=lambda move: move.movement_cost)
        return random.choice(best_actions)

    def _score(
        self,
        action: AnyCombatAction[SlotT],
        battlemap: Battlemap[SlotT],
        actor_slot: SlotT,
    ) -> float:
        after = action.perform(battlemap)
        return sum(
            aspect.weight * aspect.value(battlemap, after, actor_slot)
            for aspect in self.aspects
        )
