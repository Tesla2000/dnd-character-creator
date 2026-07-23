from __future__ import annotations

from enum import IntEnum

from dnd.character._ability_name import AbilityName
from dnd.character.actions.combat import (
    AnyCombatAction,
    AttackWithAxe,
    AttackWithBattleaxe,
    AttackWithBrownBearClaw,
    AttackWithDagger,
    AttackWithGreataxe,
    AttackWithHandCrossbow,
    AttackWithHandaxe,
    AttackWithPolarBearClaw,
    AttackWithRapier,
    AttackWithShortbow,
    AttackWithShortsword,
    CastChromaticOrb,
    CastConjureAnimals,
    CastFireBolt,
    CastFireball,
    CastIceStorm,
    CastLightningBolt,
    CastMagicMissile,
    CastScorchingRay,
    CommandSummonedBeast,
    Dash,
    Disengage,
    DrawItem,
    DropItem,
    Pass,
    RevertWildShape,
    UseRage,
    UseRecklessAttack,
    UseWildShape,
)
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import FightCharacter


class ActionResolver:
    @staticmethod
    def get_actions[T: IntEnum](
        actor_slot: T,
        fighter: FightCharacter[T],
        battlemap: Battlemap[T],
    ) -> tuple[tuple[AnyCombatAction[T], ...], ...]:
        candidates: list[tuple[AnyCombatAction[T], ...]] = []
        for action_name in fighter.character.actions:
            match action_name:
                case AbilityName.ATTACK_WITH_AXE:
                    axe_options = AttackWithAxe.create(actor_slot, fighter, battlemap)
                    if axe_options:
                        candidates.append(axe_options)
                case AbilityName.ATTACK_WITH_BATTLEAXE:
                    battleaxe_options = AttackWithBattleaxe.create(
                        actor_slot, fighter, battlemap
                    )
                    if battleaxe_options:
                        candidates.append(battleaxe_options)
                case AbilityName.ATTACK_WITH_GREATAXE:
                    greataxe_options = AttackWithGreataxe.create(
                        actor_slot, fighter, battlemap
                    )
                    if greataxe_options:
                        candidates.append(greataxe_options)
                case AbilityName.ATTACK_WITH_HANDAXE:
                    handaxe_options = AttackWithHandaxe.create(
                        actor_slot, fighter, battlemap
                    )
                    if handaxe_options:
                        candidates.append(handaxe_options)
                case AbilityName.ATTACK_WITH_DAGGER:
                    dagger_options = AttackWithDagger.create(
                        actor_slot, fighter, battlemap
                    )
                    if dagger_options:
                        candidates.append(dagger_options)
                case AbilityName.ATTACK_WITH_SHORTSWORD:
                    shortsword_options = AttackWithShortsword.create(
                        actor_slot, fighter, battlemap
                    )
                    if shortsword_options:
                        candidates.append(shortsword_options)
                case AbilityName.ATTACK_WITH_RAPIER:
                    rapier_options = AttackWithRapier.create(
                        actor_slot, fighter, battlemap
                    )
                    if rapier_options:
                        candidates.append(rapier_options)
                case AbilityName.ATTACK_WITH_SHORTBOW:
                    shortbow_options = AttackWithShortbow.create(
                        actor_slot, fighter, battlemap
                    )
                    if shortbow_options:
                        candidates.append(shortbow_options)
                case AbilityName.ATTACK_WITH_HAND_CROSSBOW:
                    hand_crossbow_options = AttackWithHandCrossbow.create(
                        actor_slot, fighter, battlemap
                    )
                    if hand_crossbow_options:
                        candidates.append(hand_crossbow_options)
                case AbilityName.CHROMATIC_ORB:
                    orb_options = CastChromaticOrb.create(
                        actor_slot, fighter, battlemap
                    )
                    if orb_options:
                        candidates.append(orb_options)
                case AbilityName.FIREBALL:
                    fireball_options = CastFireball.create(
                        actor_slot, fighter, battlemap
                    )
                    if fireball_options:
                        candidates.append(fireball_options)
                case AbilityName.FIRE_BOLT:
                    fire_bolt_options = CastFireBolt.create(
                        actor_slot, fighter, battlemap
                    )
                    if fire_bolt_options:
                        candidates.append(fire_bolt_options)
                case AbilityName.MAGIC_MISSILE:
                    magic_missile_options = CastMagicMissile.create(
                        actor_slot, fighter, battlemap
                    )
                    if magic_missile_options:
                        candidates.append(magic_missile_options)
                case AbilityName.SCORCHING_RAY:
                    scorching_ray_options = CastScorchingRay.create(
                        actor_slot, fighter, battlemap
                    )
                    if scorching_ray_options:
                        candidates.append(scorching_ray_options)
                case AbilityName.LIGHTNING_BOLT:
                    lightning_bolt_options = CastLightningBolt.create(
                        actor_slot, fighter, battlemap
                    )
                    if lightning_bolt_options:
                        candidates.append(lightning_bolt_options)
                case AbilityName.ICE_STORM:
                    ice_storm_options = CastIceStorm.create(
                        actor_slot, fighter, battlemap
                    )
                    if ice_storm_options:
                        candidates.append(ice_storm_options)
                case AbilityName.RAGE:
                    rage_options = UseRage.create(actor_slot, fighter, battlemap)
                    if rage_options:
                        candidates.append(rage_options)
                case AbilityName.RECKLESS_ATTACK:
                    reckless_options = UseRecklessAttack.create(
                        actor_slot, fighter, battlemap
                    )
                    if reckless_options:
                        candidates.append(reckless_options)
                case AbilityName.WILD_SHAPE:
                    wild_shape_options = UseWildShape.create(
                        actor_slot, fighter, battlemap
                    )
                    if wild_shape_options:
                        candidates.append(wild_shape_options)
                case AbilityName.BEAST_ATTACK:
                    brown_bear_claw_options = AttackWithBrownBearClaw.create(
                        actor_slot, fighter, battlemap
                    )
                    if brown_bear_claw_options:
                        candidates.append(brown_bear_claw_options)
                    polar_bear_claw_options = AttackWithPolarBearClaw.create(
                        actor_slot, fighter, battlemap
                    )
                    if polar_bear_claw_options:
                        candidates.append(polar_bear_claw_options)
                case AbilityName.CONJURE_ANIMALS:
                    conjure_animals_options = CastConjureAnimals.create(
                        actor_slot, fighter, battlemap
                    )
                    if conjure_animals_options:
                        candidates.append(conjure_animals_options)
                    command_summoned_beast_options = CommandSummonedBeast.create(
                        actor_slot, fighter, battlemap
                    )
                    if command_summoned_beast_options:
                        candidates.append(command_summoned_beast_options)
                case AbilityName.CUNNING_ACTION:
                    dash_options = Dash.create(actor_slot, fighter, battlemap)
                    if dash_options:
                        candidates.append(dash_options)
                    disengage_options = Disengage.create(actor_slot, fighter, battlemap)
                    if disengage_options:
                        candidates.append(disengage_options)
                case _:
                    pass
        pass_options = Pass.create(actor_slot, fighter, battlemap)
        if pass_options:
            candidates.append(pass_options)
        drop_options = DropItem.create(actor_slot, fighter, battlemap)
        if drop_options:
            candidates.append(drop_options)
        draw_options = DrawItem.create(actor_slot, fighter, battlemap)
        if draw_options:
            candidates.append(draw_options)
        revert_wild_shape_options = RevertWildShape.create(
            actor_slot, fighter, battlemap
        )
        if revert_wild_shape_options:
            candidates.append(revert_wild_shape_options)
        return tuple(candidates)
