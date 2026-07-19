from typing import Generic, NamedTuple, assert_never

from dnd._combat_event import OpportunityAttackEvent, TurnStartEvent
from dnd.character._ability_name import AbilityName
from dnd.character.actions.combat import AnyCombatAction
from dnd.character.actions.combat.attack_with_axe import AttackWithAxe
from dnd.character.actions.combat.attack_with_battleaxe import AttackWithBattleaxe
from dnd.character.actions.combat.attack_with_greataxe import AttackWithGreataxe
from dnd.character.actions.combat.attack_with_handaxe import AttackWithHandaxe
from dnd.character.actions.combat.move import Move
from dnd.character.actions.get_actions import get_actions
from dnd.fight._combatant_slot import SlotT
from dnd.fight._team_id import TeamId
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import DeadFightCharacter, FightCharacter
from dnd.fight.strategy import Strategy


class SimResult(NamedTuple):
    winner: TeamId | None
    log: list[str]
    rounds: int


class Simulator(Generic[SlotT]):
    def __init__(
        self,
        battlemap: Battlemap[SlotT],
        strategy_a: Strategy[SlotT],
        strategy_b: Strategy[SlotT],
    ) -> None:
        self._battlemap = battlemap
        self._strategy_a = strategy_a
        self._strategy_b = strategy_b
        pairs: list[tuple[SlotT, int]] = []
        for slot in battlemap.all_slots():
            c = battlemap.get_combatant(slot)
            if isinstance(c, FightCharacter):
                pairs.append((slot, c.initiative))
        pairs.sort(key=lambda x: -x[1])
        self._turn_order: tuple[SlotT, ...] = tuple(s for s, _ in pairs)

    def _is_eliminated(self, team_id: TeamId, battlemap: Battlemap[SlotT]) -> bool:
        for slot in battlemap.all_slots():
            c = battlemap.get_combatant(slot)
            if isinstance(c, FightCharacter) and c.team_id == team_id:
                return False
        return True

    def _strategy_for(self, team_id: TeamId) -> Strategy[SlotT]:
        match team_id:
            case TeamId.A:
                return self._strategy_a
            case TeamId.B:
                return self._strategy_b
            case _ as never:
                assert_never(never)

    def _slot_from_int(self, value: int, battlemap: Battlemap[SlotT]) -> SlotT:
        return next(s for s in battlemap.all_slots() if int(s) == value)

    def _get_oa_options(
        self,
        actor_slot: SlotT,
        attacker: FightCharacter,
        target_slot: SlotT,
        battlemap: Battlemap[SlotT],
    ) -> tuple[tuple[AnyCombatAction[SlotT], ...], ...]:
        candidates: list[tuple[AnyCombatAction[SlotT], ...]] = []
        for action_name in attacker.character.actions:
            match action_name:
                case AbilityName.ATTACK_WITH_AXE:
                    opts = AttackWithAxe.create_oa(
                        actor_slot, attacker, target_slot, battlemap
                    )
                    if opts:
                        candidates.append(opts)
                case AbilityName.ATTACK_WITH_BATTLEAXE:
                    opts = AttackWithBattleaxe.create_oa(
                        actor_slot, attacker, target_slot, battlemap
                    )
                    if opts:
                        candidates.append(opts)
                case AbilityName.ATTACK_WITH_GREATAXE:
                    opts = AttackWithGreataxe.create_oa(
                        actor_slot, attacker, target_slot, battlemap
                    )
                    if opts:
                        candidates.append(opts)
                case AbilityName.ATTACK_WITH_HANDAXE:
                    opts = AttackWithHandaxe.create_oa(
                        actor_slot, attacker, target_slot, battlemap
                    )
                    if opts:
                        candidates.append(opts)
                case _:
                    pass
        return tuple(candidates)

    def _process_oa_events(
        self,
        battlemap: Battlemap[SlotT],
        log_before: int,
        log: list[str],
    ) -> tuple[Battlemap[SlotT], bool]:
        any_oa = False
        new_events = battlemap.event_log[log_before:]
        for event in new_events:
            match event:
                case OpportunityAttackEvent() as oa_event:
                    attacker_slot = self._slot_from_int(
                        oa_event.attacker_slot, battlemap
                    )
                    target_slot = self._slot_from_int(
                        oa_event.target_slot, battlemap
                    )
                    match battlemap.get_combatant(attacker_slot):
                        case FightCharacter() as attacker if attacker.has_reaction:
                            oa_groups = self._get_oa_options(
                                attacker_slot, attacker, target_slot, battlemap
                            )
                            if oa_groups:
                                any_oa = True
                                oa_action = self._strategy_for(
                                    attacker.team_id
                                ).choose(oa_groups)
                                battlemap = oa_action.perform(battlemap)
                                log.append(
                                    f"  {attacker.name}"
                                    f" (team {attacker.team_id.name})"
                                    f" takes opportunity attack on {target_slot}!"
                                )
                        case _:
                            pass
                case _:
                    pass
        return battlemap, any_oa

    def run(self) -> SimResult:
        battlemap = self._battlemap
        log: list[str] = []
        round_number = 0

        while True:
            round_number += 1
            log.append(f"--- Round {round_number} ---")
            any_action_this_round = False

            for slot in self._turn_order:
                match battlemap.get_combatant(slot):
                    case FightCharacter() as fighter:
                        pass
                    case _:
                        continue

                battlemap = battlemap.emit(TurnStartEvent(target_id=fighter.id))

                match battlemap.get_combatant(slot):
                    case FightCharacter() as fighter:
                        pass
                    case _:
                        continue

                log_before = len(battlemap.event_log)
                move_options = Move.create(slot, fighter, battlemap)
                if move_options:
                    any_action_this_round = True
                    move_action = self._strategy_for(fighter.team_id).choose(
                        (move_options,)
                    )
                    battlemap = move_action.perform(battlemap)

                battlemap, had_oa = self._process_oa_events(
                    battlemap, log_before, log
                )
                if had_oa:
                    any_action_this_round = True

                match battlemap.get_combatant(slot):
                    case FightCharacter() as fighter:
                        pass
                    case _:
                        continue

                action_groups = get_actions(slot, fighter, battlemap)
                if not action_groups:
                    log.append(
                        f"  {fighter.name} (team {fighter.team_id.name}): no actions"
                    )
                    continue

                any_action_this_round = True
                action = self._strategy_for(fighter.team_id).choose(action_groups)
                battlemap = action.perform(battlemap)

                hp_parts: list[str] = []
                for s in battlemap.all_slots():
                    c = battlemap.get_combatant(s)
                    if isinstance(c, DeadFightCharacter):
                        hp_parts.append(f"{c.name}=DEAD")
                    else:
                        hp_parts.append(f"{c.name}={c.current_health}/{c.max_health}")

                log.append(
                    f"  {fighter.name} (team {fighter.team_id.name})"
                    f" uses {action.name} | {', '.join(hp_parts)}"
                )

                for team in TeamId:
                    if self._is_eliminated(team, battlemap):
                        match team:
                            case TeamId.A:
                                winner = TeamId.B
                            case TeamId.B:
                                winner = TeamId.A
                            case _ as never:
                                assert_never(never)
                        log.append(f"Team {winner.name} wins!")
                        return SimResult(winner=winner, log=log, rounds=round_number)

            if not any_action_this_round:
                log.append("Stagnation detected -- no actions possible this round.")
                return SimResult(winner=None, log=log, rounds=round_number)
