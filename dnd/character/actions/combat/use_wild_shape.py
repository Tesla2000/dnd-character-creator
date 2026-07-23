from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Literal

from dnd.character._ability_name import AbilityName
from dnd.character._fight_resource import ResourceName
from dnd.character.actions._base_action import BonusAction
from dnd.character.actions.combat._wild_shape_forms import beast_form_for_druid_level
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class UseWildShape(BonusAction[SlotT], Generic[SlotT]):
    name: Literal[AbilityName.WILD_SHAPE] = AbilityName.WILD_SHAPE
    range_tails: Literal[0] = 0
    radius_tails: Literal[0] = 0
    actor_slot: SlotT

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter[SlotT],
        battlemap: Battlemap[SlotT],
    ) -> tuple[UseWildShape[SlotT], ...]:
        if not (
            fighter.has_bonus_action
            and AbilityName.WILD_SHAPE not in fighter.active_features
            and any(
                r.name == ResourceName.WILD_SHAPE and r.remaining_uses > 0
                for r in fighter.resources
            )
        ):
            return ()
        return (cls(actor_slot=actor_slot),)

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match battlemap.get_combatant(self.actor_slot):
            case FightCharacter() as fighter:
                pass
            case _:
                return battlemap
        beast_form = beast_form_for_druid_level(fighter.character.classes.druid)
        beast_attack_ability = (
            AbilityName.ATTACK_WITH_POLAR_BEAR_CLAW
            if fighter.character.classes.druid >= 6
            else AbilityName.ATTACK_WITH_BROWN_BEAR_CLAW
        )
        updated = (
            fighter.model_copy(
                update={
                    "has_bonus_action": False,
                    "active_features": fighter.active_features
                    | {AbilityName.WILD_SHAPE, beast_attack_ability},
                }
            )
            .use_resource(ResourceName.WILD_SHAPE)
            .add_temporary_health(beast_form.hp)
        )
        return battlemap.replace_combatant(self.actor_slot, updated)
