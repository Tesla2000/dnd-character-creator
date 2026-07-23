from typing import Generic, Literal

from dnd.fight._combatant_slot import SlotT
from dnd.fight.aspect._base import _Aspect
from dnd.fight.aspect._type import AspectType
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import FightCharacter


class _EnemyClusterAspect(_Aspect[SlotT], Generic[SlotT]):
    type: Literal[AspectType.ENEMY_CLUSTER] = AspectType.ENEMY_CLUSTER

    def value(
        self,
        before: Battlemap[SlotT],
        after: Battlemap[SlotT],
        actor_slot: SlotT,
    ) -> float:
        match before.get_combatant(actor_slot):
            case FightCharacter() as actor:
                pass
            case _:
                return 0.0
        hit_count = sum(
            1
            for slot in before.all_slots()
            if isinstance(before.get_combatant(slot), FightCharacter)
            and before.get_combatant(slot).team_id != actor.team_id
            and after.get_combatant(slot).current_health
            < before.get_combatant(slot).current_health
        )
        return float(hit_count)
