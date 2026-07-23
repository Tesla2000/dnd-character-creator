import sys

from dnd._position import Position
from dnd.fight._team_id import TeamId
from dnd.fight.aspect import AoeVulnerabilityAspect, EnemyClusterAspect
from dnd.fight.battlemap import Battlemap
from dnd.fight.strategy import CompositeStrategy
from dnd.fight.weight_optimization import (
    CoordinateAscentOptimizer,
    SimulatorMatchRunner,
)
from scripts.simulate_2v2_sorcerers import (
    _FourFightBattlemap,
    _FourSlot,
    _make_sorcerer,
)

_N_ROUNDS = 3
_TRIALS_PER_EVALUATION = 20
_MAX_ROUNDS_PER_FIGHT = 150


class _SorcererBattlemapFactory:
    def create(self) -> Battlemap[_FourSlot]:
        fc_a0 = _make_sorcerer(
            "Aria", initiative=18, team_id=TeamId.A, position=Position(x=0, y=0)
        )
        fc_a1 = _make_sorcerer(
            "Aria2", initiative=16, team_id=TeamId.A, position=Position(x=1, y=0)
        )
        fc_b0 = _make_sorcerer(
            "Boris", initiative=14, team_id=TeamId.B, position=Position(x=10, y=0)
        )
        fc_b1 = _make_sorcerer(
            "Boris2", initiative=12, team_id=TeamId.B, position=Position(x=11, y=0)
        )
        return _FourFightBattlemap(combatants=(fc_a0, fc_a1, fc_b0, fc_b1))


def main() -> None:
    strategy_a: CompositeStrategy[_FourSlot] = CompositeStrategy(
        aspects=(EnemyClusterAspect(),)
    )
    strategy_b: CompositeStrategy[_FourSlot] = CompositeStrategy(
        aspects=(EnemyClusterAspect(), AoeVulnerabilityAspect())
    )
    optimizer = CoordinateAscentOptimizer()
    runner: SimulatorMatchRunner[_FourSlot] = SimulatorMatchRunner(
        battlemap_factory=_SorcererBattlemapFactory(),
        trials=_TRIALS_PER_EVALUATION,
        max_rounds=_MAX_ROUNDS_PER_FIGHT,
    )

    for round_num in range(1, _N_ROUNDS + 1):
        b_aspects = optimizer.optimize(strategy_b.aspects, runner, strategy_a, TeamId.B)
        strategy_b = CompositeStrategy(aspects=b_aspects)
        a_aspects = optimizer.optimize(strategy_a.aspects, runner, strategy_b, TeamId.A)
        strategy_a = CompositeStrategy(aspects=a_aspects)
        sys.stdout.write(f"--- round {round_num} ---\n")
        sys.stdout.write(f"Team A aspects: {strategy_a.aspects}\n")
        sys.stdout.write(f"Team B aspects: {strategy_b.aspects}\n")


if __name__ == "__main__":  # pragma: no cover
    main()
