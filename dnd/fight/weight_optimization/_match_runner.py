from __future__ import annotations

from typing import Generic, Protocol

from dnd.fight._combatant_slot import SlotT
from dnd.fight._team_id import TeamId
from dnd.fight.battlemap import Battlemap
from dnd.fight.simulator import Simulator
from dnd.fight.strategy import Strategy
from dnd.fight.weight_optimization._outcome import AggregatedOutcome, FightOutcome


class BattlemapFactory(Protocol[SlotT]):
    def create(self) -> Battlemap[SlotT]: ...


class MatchRunner(Protocol[SlotT]):
    def run(
        self,
        strategy_a: Strategy[SlotT],
        strategy_b: Strategy[SlotT],
        perspective: TeamId,
    ) -> AggregatedOutcome: ...


class SimulatorMatchRunner(Generic[SlotT]):
    def __init__(
        self,
        battlemap_factory: BattlemapFactory[SlotT],
        trials: int,
        max_rounds: int,
    ) -> None:
        self._battlemap_factory = battlemap_factory
        self._trials = trials
        self._max_rounds = max_rounds

    def run(
        self,
        strategy_a: Strategy[SlotT],
        strategy_b: Strategy[SlotT],
        perspective: TeamId,
    ) -> AggregatedOutcome:
        outcomes = tuple(
            self._run_single(strategy_a, strategy_b, perspective)
            for _ in range(self._trials)
        )
        return AggregatedOutcome.from_outcomes(outcomes)

    def _run_single(
        self,
        strategy_a: Strategy[SlotT],
        strategy_b: Strategy[SlotT],
        perspective: TeamId,
    ) -> FightOutcome:
        battlemap = self._battlemap_factory.create()
        result = Simulator(
            battlemap, strategy_a, strategy_b, max_rounds=self._max_rounds
        ).run()
        return self._score(
            result.final_battlemap,
            result.ever_downed_slots,
            result.ever_dead_slots,
            perspective,
        )

    @staticmethod
    def _score(
        battlemap: Battlemap[SlotT],
        ever_downed: frozenset[SlotT],
        ever_dead: frozenset[SlotT],
        perspective: TeamId,
    ) -> FightOutcome:
        own_dead = 0
        enemy_dead = 0
        own_downed = 0
        enemy_downed = 0
        own_hp = 0
        enemy_hp = 0
        for slot in battlemap.all_slots():
            combatant = battlemap.get_combatant(slot)
            is_own = combatant.team_id == perspective
            if slot in ever_dead:
                if is_own:
                    own_dead += 1
                else:
                    enemy_dead += 1
            if slot in ever_downed:
                if is_own:
                    own_downed += 1
                else:
                    enemy_downed += 1
            if is_own:
                own_hp += combatant.current_health
            else:
                enemy_hp += combatant.current_health
        return FightOutcome(
            dead_diff=enemy_dead - own_dead,
            downed_diff=enemy_downed - own_downed,
            hp_diff=own_hp - enemy_hp,
        )
