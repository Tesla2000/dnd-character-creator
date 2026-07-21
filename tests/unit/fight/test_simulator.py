import random
from enum import IntEnum
from typing import Self

import pytest

import dnd.fight.simulator as simulator_module
from dnd._combat_event import AnyCombatEvent, TurnEndEvent, TurnStartEvent
from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.actions.combat import (
    AnyCombatAction,
    AttackWithBattleaxe,
    DrawItem,
    DropItem,
    Pass,
)
from dnd.character.actions.combat.move import Move
from dnd.character.actions.get_actions import ActionResolver
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.stats import Stats
from dnd.choices.equipment_creation.weapons import WeaponName
from dnd.fight._team_id import TeamId
from dnd.fight.aspect import AoeVulnerabilityAspect
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import AnyActiveCombatant, FightCharacter
from dnd.fight.simulator import (
    ActionCapExceededError,
    RoundCapExceededError,
    SimResult,
    Simulator,
)
from dnd.fight.strategy import AggressiveStrategy, CompositeStrategy, RandomStrategy

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
    "weapons": [WeaponName.BATTLEAXE],
    "actions": [AbilityName.ATTACK_WITH_BATTLEAXE],
}


class _TwoFightSlot(IntEnum):
    A = 0
    B = 1


class _TwoFightBattlemap(Battlemap[_TwoFightSlot]):
    combatants: tuple[AnyActiveCombatant, AnyActiveCombatant]

    def get_combatant(self, slot: _TwoFightSlot) -> AnyActiveCombatant:
        match slot:
            case _TwoFightSlot.A:
                return self.combatants[0]
            case _TwoFightSlot.B:
                return self.combatants[1]

    def replace_combatant(
        self, slot: _TwoFightSlot, updated: AnyActiveCombatant
    ) -> Self:
        match slot:
            case _TwoFightSlot.A:
                return self.model_copy(
                    update={"combatants": (updated, self.combatants[1])}
                )
            case _TwoFightSlot.B:
                return self.model_copy(
                    update={"combatants": (self.combatants[0], updated)}
                )


class _ThreeFightSlot(IntEnum):
    A0 = 0
    A1 = 1
    B0 = 2


class _ThreeFightBattlemap(Battlemap[_ThreeFightSlot]):
    combatants: tuple[AnyActiveCombatant, AnyActiveCombatant, AnyActiveCombatant]

    def get_combatant(self, slot: _ThreeFightSlot) -> AnyActiveCombatant:
        match slot:
            case _ThreeFightSlot.A0:
                return self.combatants[0]
            case _ThreeFightSlot.A1:
                return self.combatants[1]
            case _ThreeFightSlot.B0:
                return self.combatants[2]

    def replace_combatant(
        self, slot: _ThreeFightSlot, updated: AnyActiveCombatant
    ) -> Self:
        match slot:
            case _ThreeFightSlot.A0:
                return self.model_copy(
                    update={
                        "combatants": (
                            updated,
                            self.combatants[1],
                            self.combatants[2],
                        )
                    }
                )
            case _ThreeFightSlot.A1:
                return self.model_copy(
                    update={
                        "combatants": (
                            self.combatants[0],
                            updated,
                            self.combatants[2],
                        )
                    }
                )
            case _ThreeFightSlot.B0:
                return self.model_copy(
                    update={
                        "combatants": (
                            self.combatants[0],
                            self.combatants[1],
                            updated,
                        )
                    }
                )


def _make_fc(
    name: str, initiative: int, team_id: TeamId, speed: int = 0
) -> FightCharacter:
    data = {**_PC_DATA, "character_data": {"name": name}}
    pc = PresentableCharacter.model_validate(data)
    return FightCharacter.from_presentable(
        pc, initiative=initiative, team_id=team_id
    ).model_copy(
        update={
            "position": Position(x=0, y=0)
            if team_id == TeamId.A
            else Position(x=1, y=0),
            "speed": speed,
        }
    )


def _pick_fallback_action(
    candidates: tuple[AnyCombatAction[_TwoFightSlot], ...],
) -> AnyCombatAction[_TwoFightSlot]:
    """Fallback pick for test strategies that don't otherwise care which
    action they take. Always picking candidates[0] is unsafe here: right
    after an attack, DropItem can be the *only* candidate offered (a free
    action, independent of the spent action economy), so a naive fallback
    would drop the fighter's weapon; and once dropped, if Pass is ever
    preferred over DrawItem, the fighter never re-arms and the fight stalls
    forever. So the priority is: a real action first, then DrawItem (recover
    a dropped weapon), then Pass, and only then DropItem as an absolute last
    resort.
    """
    for action in candidates:
        if not isinstance(action, (Pass, DropItem, DrawItem)):
            return action
    for action in candidates:
        if isinstance(action, DrawItem):
            return action
    for action in candidates:
        if isinstance(action, Pass):
            return action
    return candidates[0]


@pytest.mark.unit
class TestTeamId:
    def test_team_id_is_int_enum(self) -> None:
        assert TeamId.A == 0
        assert TeamId.B == 1

    def test_team_id_on_fight_character_defaults_to_a(self) -> None:
        pc = PresentableCharacter.model_validate(_PC_DATA)
        fc = FightCharacter.from_presentable(pc, initiative=10)
        assert fc.team_id == TeamId.A

    def test_team_id_propagates_through_from_presentable(self) -> None:
        pc = PresentableCharacter.model_validate(_PC_DATA)
        fc = FightCharacter.from_presentable(pc, initiative=10, team_id=TeamId.B)
        assert fc.team_id == TeamId.B


@pytest.mark.unit
class TestRandomStrategy:
    def test_choose_returns_action_from_candidates(self) -> None:
        fc = _make_fc("a", 10, TeamId.A)
        target = _make_fc("b", 5, TeamId.B)
        bm = _TwoFightBattlemap(combatants=(fc, target))
        attacks = AttackWithBattleaxe.create(_TwoFightSlot.A, fc, bm)
        strategy: RandomStrategy[_TwoFightSlot] = RandomStrategy()
        action = strategy.choose(attacks, bm, _TwoFightSlot.A)
        assert isinstance(action, AttackWithBattleaxe)

    def test_samples_uniformly_by_ability_before_by_option(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        fc = _make_fc("a", 10, TeamId.A)
        target = _make_fc("b", 5, TeamId.B)
        bm = _TwoFightBattlemap(combatants=(fc, target))
        move_options = tuple(
            Move(to=Position(x=x, y=0), mover_slot=_TwoFightSlot.A, movement_cost=5)
            for x in range(5)
        )
        pass_option = (Pass(actor_slot=_TwoFightSlot.A),)
        candidates: tuple[AnyCombatAction[_TwoFightSlot], ...] = (
            move_options + pass_option
        )
        seen_lengths: list[int] = []
        real_choice = random.choice

        def _spy_choice(seq: list[object]) -> object:
            seen_lengths.append(len(seq))
            return real_choice(seq)

        monkeypatch.setattr(random, "choice", _spy_choice)
        strategy: RandomStrategy[_TwoFightSlot] = RandomStrategy()
        strategy.choose(candidates, bm, _TwoFightSlot.A)
        assert 2 in seen_lengths


@pytest.mark.unit
class TestAggressiveStrategy:
    def test_moves_toward_nearest_enemy(self) -> None:
        fc_a = _make_fc("A", 10, TeamId.A, speed=30).model_copy(
            update={"position": Position(x=0, y=0), "movement_remaining": 30}
        )
        fc_b = _make_fc("B", 5, TeamId.B, speed=0).model_copy(
            update={"position": Position(x=10, y=0)}
        )
        bm = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        move_options = Move.create(_TwoFightSlot.A, fc_a, bm)
        strategy: AggressiveStrategy[_TwoFightSlot] = AggressiveStrategy()
        chosen = strategy.choose(move_options, bm, _TwoFightSlot.A)
        assert isinstance(chosen, Move)
        assert chosen.to.x > fc_a.position.x

    def test_excludes_move_from_fallback_when_no_enemies_present(self) -> None:
        fc_a = _make_fc("A", 10, TeamId.A, speed=30).model_copy(
            update={"position": Position(x=0, y=0), "movement_remaining": 30}
        )
        ally = _make_fc("Ally", 5, TeamId.A, speed=0).model_copy(
            update={"position": Position(x=1, y=0)}
        )
        bm = _TwoFightBattlemap(combatants=(fc_a, ally))
        move_options = Move.create(_TwoFightSlot.A, fc_a, bm)
        pass_options = Pass.create(_TwoFightSlot.A, fc_a, bm)
        assert move_options
        candidates: tuple[AnyCombatAction[_TwoFightSlot], ...] = (
            move_options + pass_options
        )
        strategy: AggressiveStrategy[_TwoFightSlot] = AggressiveStrategy()
        chosen = strategy.choose(candidates, bm, _TwoFightSlot.A)
        assert not isinstance(chosen, Move)


@pytest.mark.unit
class TestCompositeStrategy:
    def test_choose_prefers_the_action_that_scores_highest(self) -> None:
        a0 = _make_fc("A0", 10, TeamId.A, speed=30).model_copy(
            update={"position": Position(x=0, y=0), "movement_remaining": 30}
        )
        a1 = _make_fc("A1", 9, TeamId.A, speed=0).model_copy(
            update={"position": Position(x=20, y=20)}
        )
        b0 = _make_fc("B0", 5, TeamId.B, speed=0).model_copy(
            update={"position": Position(x=-20, y=-20)}
        )
        bm = _ThreeFightBattlemap(combatants=(a0, a1, b0))

        move_toward_ally = Move(
            to=Position(x=19, y=20), mover_slot=_ThreeFightSlot.A0, movement_cost=5
        )
        move_away_from_ally = Move(
            to=Position(x=-5, y=0), mover_slot=_ThreeFightSlot.A0, movement_cost=5
        )
        candidates: tuple[AnyCombatAction[_ThreeFightSlot], ...] = (
            move_toward_ally,
            move_away_from_ally,
        )

        strategy: CompositeStrategy[_ThreeFightSlot] = CompositeStrategy(
            aspects=(AoeVulnerabilityAspect(),)
        )
        chosen = strategy.choose(candidates, bm, _ThreeFightSlot.A0)
        assert chosen is move_away_from_ally

    def test_two_composite_strategies_produce_a_winner(self) -> None:
        fc_a = _make_fc("A", initiative=15, team_id=TeamId.A)
        fc_b = _make_fc("B", initiative=12, team_id=TeamId.B)
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        strategy: CompositeStrategy[_TwoFightSlot] = CompositeStrategy(
            aspects=(AoeVulnerabilityAspect(),)
        )
        result = Simulator(battlemap, strategy_a=strategy, strategy_b=strategy).run()
        assert isinstance(result, SimResult)
        assert result.winner in (TeamId.A, TeamId.B)


@pytest.mark.unit
class TestSimulator:
    def test_two_fighters_produce_a_winner(self) -> None:
        fc_a = _make_fc("A", initiative=15, team_id=TeamId.A)
        fc_b = _make_fc("B", initiative=12, team_id=TeamId.B)
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        strategy: RandomStrategy[_TwoFightSlot] = RandomStrategy()
        result = Simulator(battlemap, strategy_a=strategy, strategy_b=strategy).run()
        assert isinstance(result, SimResult)
        assert result.winner in (TeamId.A, TeamId.B)
        assert result.rounds >= 1
        assert len(result.log) > 0

    def test_sim_result_is_named_tuple(self) -> None:
        result = SimResult(winner=TeamId.A, log=["line"], rounds=3)
        assert result.winner == TeamId.A
        assert result.rounds == 3

    def test_log_contains_round_headers(self) -> None:
        fc_a = _make_fc("A", initiative=15, team_id=TeamId.A)
        fc_b = _make_fc("B", initiative=12, team_id=TeamId.B)
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        strategy: RandomStrategy[_TwoFightSlot] = RandomStrategy()
        result = Simulator(battlemap, strategy_a=strategy, strategy_b=strategy).run()
        assert isinstance(result, SimResult)
        assert any("Round" in line for line in result.log)

    def test_strategy_dispatch_uses_correct_team(self) -> None:
        class _FixedStrategy:
            def __init__(self, action_index: int) -> None:
                self._idx = action_index

            def choose(
                self,
                candidates: tuple[AnyCombatAction[_TwoFightSlot], ...],
                battlemap: Battlemap[_TwoFightSlot],
                actor_slot: _TwoFightSlot,
            ) -> AnyCombatAction[_TwoFightSlot]:
                fallback = _pick_fallback_action(candidates)
                same_ability = tuple(
                    a for a in candidates if a.name == fallback.name
                )
                return same_ability[self._idx % len(same_ability)]

        fc_a = _make_fc("A", initiative=20, team_id=TeamId.A)
        fc_b = _make_fc("B", initiative=5, team_id=TeamId.B)
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        result = Simulator(
            battlemap,
            strategy_a=_FixedStrategy(0),
            strategy_b=_FixedStrategy(0),
        ).run()
        assert isinstance(result, SimResult)
        assert result.winner in (TeamId.A, TeamId.B)

    def test_movement_closes_distance(self) -> None:
        fc_a = _make_fc("A", 20, TeamId.A, speed=5).model_copy(
            update={"position": Position(x=0, y=0)}
        )
        fc_b = _make_fc("B", 5, TeamId.B, speed=0).model_copy(
            update={"position": Position(x=2, y=0)}
        )
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        target = (2, 0)

        class _ApproachStrategy:
            def choose(
                self,
                candidates: tuple[AnyCombatAction[_TwoFightSlot], ...],
                battlemap: Battlemap[_TwoFightSlot],
                actor_slot: _TwoFightSlot,
            ) -> AnyCombatAction[_TwoFightSlot]:
                moves = [a for a in candidates if isinstance(a, Move)]
                if moves:
                    return min(
                        moves,
                        key=lambda m: max(
                            abs(m.to[0] - target[0]), abs(m.to[1] - target[1])
                        ),
                    )
                return _pick_fallback_action(candidates)

        result = Simulator(
            battlemap,
            strategy_a=_ApproachStrategy(),
            strategy_b=_ApproachStrategy(),
        ).run()
        assert isinstance(result, SimResult)
        assert result.winner in (TeamId.A, TeamId.B)

    def test_opportunity_attack_fires_on_retreat(self) -> None:
        fc_a = _make_fc("A", 20, TeamId.A, speed=5)
        fc_b = _make_fc("B", 5, TeamId.B, speed=0)
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        b_pos = fc_b.position

        class _RetreatOnceThenApproachStrategy:
            def __init__(self) -> None:
                self._retreated = False

            def choose(
                self,
                candidates: tuple[AnyCombatAction[_TwoFightSlot], ...],
                battlemap: Battlemap[_TwoFightSlot],
                actor_slot: _TwoFightSlot,
            ) -> AnyCombatAction[_TwoFightSlot]:
                moves = [a for a in candidates if isinstance(a, Move)]
                if moves:
                    if not self._retreated:
                        for m in moves:
                            if m.triggered_oa_from:
                                self._retreated = True
                                return m
                        self._retreated = True
                        return moves[0]
                    return min(
                        moves,
                        key=lambda m: max(
                            abs(m.to[0] - b_pos[0]), abs(m.to[1] - b_pos[1])
                        ),
                    )
                return _pick_fallback_action(candidates)

        class _AttackStrategy:
            def choose(
                self,
                candidates: tuple[AnyCombatAction[_TwoFightSlot], ...],
                battlemap: Battlemap[_TwoFightSlot],
                actor_slot: _TwoFightSlot,
            ) -> AnyCombatAction[_TwoFightSlot]:
                return _pick_fallback_action(candidates)

        result = Simulator(
            battlemap,
            strategy_a=_RetreatOnceThenApproachStrategy(),
            strategy_b=_AttackStrategy(),
        ).run()
        assert isinstance(result, SimResult)
        assert any("opportunity attack" in line for line in result.log)

    def test_round_cap_exceeded_returns_error(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(simulator_module, "_MAX_ROUNDS", 2)
        data = {**_PC_DATA, "weapons": [], "actions": []}
        fc_a = FightCharacter.from_presentable(
            PresentableCharacter.model_validate(
                {**data, "character_data": {"name": "A"}}
            ),
            initiative=15,
            team_id=TeamId.A,
        )
        fc_b = FightCharacter.from_presentable(
            PresentableCharacter.model_validate(
                {**data, "character_data": {"name": "B"}}
            ),
            initiative=12,
            team_id=TeamId.B,
        ).model_copy(update={"position": Position(x=1, y=0)})
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        strategy: RandomStrategy[_TwoFightSlot] = RandomStrategy()
        result = Simulator(battlemap, strategy_a=strategy, strategy_b=strategy).run()
        assert isinstance(result, RoundCapExceededError)

    def test_action_cap_exceeded_returns_error(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(simulator_module, "_MAX_ACTIONS_PER_TURN", 3)

        def _fake_get_actions(
            actor_slot: _TwoFightSlot,
            fighter: FightCharacter,
            battlemap: Battlemap[_TwoFightSlot],
        ) -> tuple[tuple[AnyCombatAction[_TwoFightSlot], ...], ...]:
            return ((DropItem(actor_slot=actor_slot, which_hand="main"),),)

        monkeypatch.setattr(
            ActionResolver, "get_actions", staticmethod(_fake_get_actions)
        )
        fc_a = _make_fc("A", initiative=15, team_id=TeamId.A)
        fc_b = _make_fc("B", initiative=12, team_id=TeamId.B)
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        strategy: RandomStrategy[_TwoFightSlot] = RandomStrategy()
        result = Simulator(battlemap, strategy_a=strategy, strategy_b=strategy).run()
        assert isinstance(result, ActionCapExceededError)

    def test_turn_end_event_paired_with_turn_start_when_no_elimination(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(simulator_module, "_MAX_ROUNDS", 2)
        recorded: list[AnyCombatEvent[_TwoFightSlot]] = []
        original_emit = Battlemap.emit

        def _spy_emit(
            self: Battlemap[_TwoFightSlot], event: AnyCombatEvent[_TwoFightSlot]
        ) -> Battlemap[_TwoFightSlot]:
            recorded.append(event)
            return original_emit(self, event)

        monkeypatch.setattr(Battlemap, "emit", _spy_emit)
        data = {**_PC_DATA, "weapons": [], "actions": []}
        fc_a = FightCharacter.from_presentable(
            PresentableCharacter.model_validate(
                {**data, "character_data": {"name": "A"}}
            ),
            initiative=15,
            team_id=TeamId.A,
        )
        fc_b = FightCharacter.from_presentable(
            PresentableCharacter.model_validate(
                {**data, "character_data": {"name": "B"}}
            ),
            initiative=12,
            team_id=TeamId.B,
        ).model_copy(update={"position": Position(x=1, y=0)})
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        strategy: RandomStrategy[_TwoFightSlot] = RandomStrategy()
        result = Simulator(battlemap, strategy_a=strategy, strategy_b=strategy).run()
        assert isinstance(result, RoundCapExceededError)
        turn_starts = [e for e in recorded if isinstance(e, TurnStartEvent)]
        turn_ends = [e for e in recorded if isinstance(e, TurnEndEvent)]
        assert len(turn_starts) == 4
        assert len(turn_ends) == 4

    def test_turn_end_event_not_emitted_when_fight_ends_mid_turn(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        recorded: list[AnyCombatEvent[_TwoFightSlot]] = []
        original_emit = Battlemap.emit

        def _spy_emit(
            self: Battlemap[_TwoFightSlot], event: AnyCombatEvent[_TwoFightSlot]
        ) -> Battlemap[_TwoFightSlot]:
            recorded.append(event)
            return original_emit(self, event)

        monkeypatch.setattr(Battlemap, "emit", _spy_emit)
        fc_a = _make_fc("A", initiative=15, team_id=TeamId.A)
        fc_b = _make_fc("B", initiative=12, team_id=TeamId.B)
        battlemap = _TwoFightBattlemap(combatants=(fc_a, fc_b))
        strategy: RandomStrategy[_TwoFightSlot] = RandomStrategy()
        result = Simulator(battlemap, strategy_a=strategy, strategy_b=strategy).run()
        assert isinstance(result, SimResult)
        turn_starts = sum(1 for e in recorded if isinstance(e, TurnStartEvent))
        turn_ends = sum(1 for e in recorded if isinstance(e, TurnEndEvent))
        assert turn_starts == turn_ends + 1
