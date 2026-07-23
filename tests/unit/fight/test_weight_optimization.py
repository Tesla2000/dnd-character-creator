from enum import IntEnum
from typing import Self

import pytest

from dnd._position import Position
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.stats import Stats
from dnd.fight._team_id import TeamId
from dnd.fight.aspect import AnyAspect, AoeVulnerabilityAspect, EnemyClusterAspect
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import (
    AnyActiveCombatant,
    DeadFightCharacter,
    FightCharacter,
)
from dnd.fight.strategy import CompositeStrategy, RandomStrategy
from dnd.fight.weight_optimization import (
    AggregatedOutcome,
    BattlemapFactory,
    CoordinateAscentOptimizer,
    FightOutcome,
    SimulatorMatchRunner,
)

_STATS = Stats(
    strength=17,
    dexterity=13,
    constitution=16,
    intelligence=9,
    wisdom=11,
    charisma=8,
)

_PC_DATA: dict[str, object] = {
    "race": "Human",
    "stats": _STATS.model_dump(),
    "health_base": 20,
    "character_data": {"name": ""},
    "classes": {
        "wizard": 0,
        "sorcerer": 0,
        "fighter": 0,
        "barbarian": 1,
        "rogue": 0,
        "cleric": 0,
        "druid": 0,
        "paladin": 0,
        "ranger": 0,
        "monk": 0,
        "bard": 0,
        "warlock": 0,
        "artificer": 0,
    },
    "speed": 30,
    "dark_vision_range": 0,
    "saving_throw_proficiencies": [],
    "other_active_abilities": [],
    "weapons": [],
    "actions": [],
}


class _TwoSlot(IntEnum):
    A = 0
    B = 1


class _TwoBattlemap(Battlemap[_TwoSlot]):
    combatants: tuple[AnyActiveCombatant, AnyActiveCombatant]

    def get_combatant(self, slot: _TwoSlot) -> AnyActiveCombatant:
        match slot:
            case _TwoSlot.A:
                return self.combatants[0]
            case _TwoSlot.B:
                return self.combatants[1]

    def replace_combatant(self, slot: _TwoSlot, updated: AnyActiveCombatant) -> Self:
        match slot:
            case _TwoSlot.A:
                return self.model_copy(
                    update={"combatants": (updated, self.combatants[1])}
                )
            case _TwoSlot.B:
                return self.model_copy(
                    update={"combatants": (self.combatants[0], updated)}
                )


def _make_fc(name: str, team_id: TeamId, current_health: int) -> FightCharacter:
    data = {**_PC_DATA, "character_data": {"name": name}}
    pc = PresentableCharacter.model_validate(data)
    return FightCharacter.from_presentable(
        pc, initiative=10, team_id=team_id
    ).model_copy(
        update={
            "position": Position(x=0, y=0),
            "current_health": current_health,
        }
    )


def _make_dead(name: str, team_id: TeamId) -> DeadFightCharacter:
    fc = _make_fc(name, team_id, current_health=1)
    return DeadFightCharacter(
        character=fc.character,
        initiative=fc.initiative,
        max_health=fc.max_health,
        current_health=0,
        team_id=team_id,
        speed=fc.speed,
        position=fc.position,
    )


@pytest.mark.unit
class TestFightOutcome:
    def test_is_named_tuple_of_three_ints(self) -> None:
        outcome = FightOutcome(dead_diff=1, downed_diff=2, hp_diff=3)
        assert outcome.dead_diff == 1
        assert outcome.downed_diff == 2
        assert outcome.hp_diff == 3


@pytest.mark.unit
class TestAggregatedOutcome:
    def test_from_outcomes_averages_each_field(self) -> None:
        outcomes = (
            FightOutcome(dead_diff=1, downed_diff=2, hp_diff=10),
            FightOutcome(dead_diff=0, downed_diff=0, hp_diff=-10),
        )
        aggregated = AggregatedOutcome.from_outcomes(outcomes)
        assert aggregated.mean_dead_diff == 0.5
        assert aggregated.mean_downed_diff == 1.0
        assert aggregated.mean_hp_diff == 0.0

    def test_beats_prioritizes_dead_diff_first(self) -> None:
        better = AggregatedOutcome(
            mean_dead_diff=1.0, mean_downed_diff=-5.0, mean_hp_diff=-100.0
        )
        worse = AggregatedOutcome(
            mean_dead_diff=0.0, mean_downed_diff=5.0, mean_hp_diff=100.0
        )
        assert better.beats(worse)
        assert not worse.beats(better)

    def test_beats_falls_back_to_downed_diff_when_dead_diff_ties(self) -> None:
        better = AggregatedOutcome(
            mean_dead_diff=0.0, mean_downed_diff=1.0, mean_hp_diff=-100.0
        )
        worse = AggregatedOutcome(
            mean_dead_diff=0.0, mean_downed_diff=0.0, mean_hp_diff=100.0
        )
        assert better.beats(worse)
        assert not worse.beats(better)

    def test_beats_falls_back_to_hp_diff_when_dead_and_downed_diff_tie(self) -> None:
        better = AggregatedOutcome(
            mean_dead_diff=0.0, mean_downed_diff=0.0, mean_hp_diff=1.0
        )
        worse = AggregatedOutcome(
            mean_dead_diff=0.0, mean_downed_diff=0.0, mean_hp_diff=0.0
        )
        assert better.beats(worse)
        assert not worse.beats(better)


@pytest.mark.unit
class TestSimulatorMatchRunnerScore:
    def test_score_from_winning_teams_perspective(self) -> None:
        alive_a = _make_fc("A", TeamId.A, current_health=15)
        dead_b = _make_dead("B", TeamId.B)
        battlemap = _TwoBattlemap(combatants=(alive_a, dead_b))

        outcome = SimulatorMatchRunner._score(
            battlemap,
            ever_downed=frozenset({_TwoSlot.B}),
            ever_dead=frozenset({_TwoSlot.B}),
            perspective=TeamId.A,
        )
        assert outcome == FightOutcome(dead_diff=1, downed_diff=1, hp_diff=15)

    def test_score_from_losing_teams_perspective_is_the_mirror_image(self) -> None:
        alive_a = _make_fc("A", TeamId.A, current_health=15)
        dead_b = _make_dead("B", TeamId.B)
        battlemap = _TwoBattlemap(combatants=(alive_a, dead_b))

        outcome = SimulatorMatchRunner._score(
            battlemap,
            ever_downed=frozenset({_TwoSlot.B}),
            ever_dead=frozenset({_TwoSlot.B}),
            perspective=TeamId.B,
        )
        assert outcome == FightOutcome(dead_diff=-1, downed_diff=-1, hp_diff=-15)

    def test_score_ignores_slots_never_downed_or_dead(self) -> None:
        alive_a = _make_fc("A", TeamId.A, current_health=10)
        alive_b = _make_fc("B", TeamId.B, current_health=4)
        battlemap = _TwoBattlemap(combatants=(alive_a, alive_b))

        outcome = SimulatorMatchRunner._score(
            battlemap,
            ever_downed=frozenset(),
            ever_dead=frozenset(),
            perspective=TeamId.A,
        )
        assert outcome == FightOutcome(dead_diff=0, downed_diff=0, hp_diff=6)


class _FixedBattlemapFactory:
    def __init__(self, battlemap: Battlemap[_TwoSlot]) -> None:
        self._battlemap = battlemap

    def create(self) -> Battlemap[_TwoSlot]:
        return self._battlemap


@pytest.mark.unit
class TestSimulatorMatchRunnerRun:
    def test_run_averages_outcomes_over_configured_trial_count(self) -> None:
        alive_a = _make_fc("A", TeamId.A, current_health=15)
        dead_b = _make_dead("B", TeamId.B)
        battlemap = _TwoBattlemap(combatants=(alive_a, dead_b))
        factory: BattlemapFactory[_TwoSlot] = _FixedBattlemapFactory(battlemap)
        runner: SimulatorMatchRunner[_TwoSlot] = SimulatorMatchRunner(
            battlemap_factory=factory, trials=3, max_rounds=5
        )
        strategy: RandomStrategy[_TwoSlot] = RandomStrategy()

        outcome = runner.run(strategy, strategy, TeamId.A)

        assert outcome == AggregatedOutcome(
            mean_dead_diff=1.0, mean_downed_diff=1.0, mean_hp_diff=15.0
        )


class _WeightSeekingRunner:
    def __init__(self, target_weight: float, optimizing_team: TeamId) -> None:
        self._target_weight = target_weight
        self._optimizing_team = optimizing_team
        self.seen_weights: list[float] = []

    def run(
        self,
        strategy_a: object,
        strategy_b: object,
        perspective: TeamId,
    ) -> AggregatedOutcome:
        strategy = strategy_a if self._optimizing_team == TeamId.A else strategy_b
        assert isinstance(strategy, CompositeStrategy)
        weight = strategy.aspects[1].weight
        self.seen_weights.append(weight)
        score = -abs(weight - self._target_weight)
        return AggregatedOutcome(
            mean_dead_diff=0.0, mean_downed_diff=0.0, mean_hp_diff=score
        )


class _FixedOutcomeRunner:
    def run(
        self,
        strategy_a: object,
        strategy_b: object,
        perspective: TeamId,
    ) -> AggregatedOutcome:
        return AggregatedOutcome(
            mean_dead_diff=0.0, mean_downed_diff=0.0, mean_hp_diff=0.0
        )


@pytest.mark.unit
class TestCoordinateAscentOptimizer:
    def test_converges_to_the_best_candidate_weight_for_team_b(self) -> None:
        aspects: tuple[AnyAspect[_TwoSlot], ...] = (
            EnemyClusterAspect(),
            AoeVulnerabilityAspect(),
        )
        evaluator = _WeightSeekingRunner(target_weight=2.0, optimizing_team=TeamId.B)
        frozen_strategy: RandomStrategy[_TwoSlot] = RandomStrategy()

        tuned = CoordinateAscentOptimizer().optimize(
            aspects, evaluator, frozen_strategy, TeamId.B
        )

        assert tuned[0].weight == 1.0
        assert tuned[1].weight == 2.0

    def test_converges_for_team_a_too(self) -> None:
        aspects: tuple[AnyAspect[_TwoSlot], ...] = (
            EnemyClusterAspect(),
            AoeVulnerabilityAspect(),
        )
        evaluator = _WeightSeekingRunner(target_weight=0.5, optimizing_team=TeamId.A)
        frozen_strategy: RandomStrategy[_TwoSlot] = RandomStrategy()

        tuned = CoordinateAscentOptimizer().optimize(
            aspects, evaluator, frozen_strategy, TeamId.A
        )

        assert tuned[1].weight == 0.5

    def test_single_aspect_side_has_no_free_weight_to_tune(self) -> None:
        aspects: tuple[AnyAspect[_TwoSlot], ...] = (EnemyClusterAspect(),)
        evaluator = _FixedOutcomeRunner()
        frozen_strategy: RandomStrategy[_TwoSlot] = RandomStrategy()

        tuned = CoordinateAscentOptimizer().optimize(
            aspects, evaluator, frozen_strategy, TeamId.B
        )

        assert len(tuned) == 1
        assert tuned[0].weight == 1.0
