from __future__ import annotations

from abc import abstractmethod
from random import randint
from typing import TYPE_CHECKING, ClassVar, Generic, Literal, Self
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, PositiveInt
from uuid_string import UUIDString

from dnd._combat_event import (
    CreatureAttackedEvent,
    CreatureTargetedEvent,
    MeleeDamageEvent,
)
from dnd.character._ability_name import AbilityName
from dnd.character.actions._base_action import Action
from dnd.character.actions.advantage_modifier import (
    AdvantageModifier,
    DisadvantageModifier,
    GrantsAdvantageModifier,
)
from dnd.character.actions._damage_type import DamageType
from dnd.character.actions.attack_bonus_modifier import AttackBonusModifier
from dnd.character.actions.magical_damage_modifier import MagicalDamageModifier
from dnd.choices.abilities.fighting_style import FightingStyle
from dnd.choices.equipment_creation.weapons import HitDieSize, WeaponName
from dnd.choices.stats_creation.statistic import Statistic
from dnd.fight._combatant_slot import SlotT
from dnd.fight.fight_character import FightCharacter

if TYPE_CHECKING:
    from dnd.fight.battlemap import Battlemap


class _MeleeAttackExecutor(BaseModel, Generic[SlotT]):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    actor_slot: SlotT
    target_slot: SlotT
    die: HitDieSize
    damage_type: DamageType
    n_dice: PositiveInt = 1
    ability_modifier: int = 0
    is_oa: bool = False
    can_sneak_attack: bool = False

    def _compute_use_advantage(
        self, fighter: FightCharacter[SlotT], target: FightCharacter[SlotT]
    ) -> bool:
        return any(
            isinstance(m, AdvantageModifier) and m.apply(fighter, target)
            for m in fighter.modifiers
        ) or any(
            isinstance(m, GrantsAdvantageModifier) and m.apply(fighter, target)
            for m in target.modifiers
        )

    def _compute_use_disadvantage(
        self, fighter: FightCharacter[SlotT], target: FightCharacter[SlotT]
    ) -> bool:
        return any(
            isinstance(m, DisadvantageModifier) and m.apply(fighter, target)
            for m in fighter.modifiers
        )

    def _has_ally_adjacent_to_target(
        self,
        bm: Battlemap[SlotT],
        fighter: FightCharacter[SlotT],
        target: FightCharacter[SlotT],
    ) -> bool:
        tx, ty = target.position.x, target.position.y
        for slot in bm.all_slots():
            if slot in (self.actor_slot, self.target_slot):
                continue
            ally = bm.get_combatant(slot)
            if not isinstance(ally, FightCharacter) or ally.team_id != fighter.team_id:
                continue
            ax, ay = ally.position.x, ally.position.y
            if max(abs(ax - tx), abs(ay - ty)) <= 1:
                return True
        return False

    def attack(self, bm: Battlemap[SlotT]) -> Battlemap[SlotT]:
        match bm.get_combatant(self.actor_slot):
            case FightCharacter() as fighter:
                pass
            case _:
                return bm

        if self.is_oa:
            bm = bm.replace_combatant(self.actor_slot, fighter.spend_reaction())
        else:
            bm = bm.replace_combatant(self.actor_slot, fighter.spend_attack())

        match bm.get_combatant(self.target_slot):
            case FightCharacter() as target:
                pass
            case _:
                return bm

        attack_id = UUIDString(str(uuid4()))

        bm = bm.emit(
            CreatureTargetedEvent(
                attacker_id=fighter.id,
                defender_id=target.id,
                attack_id=attack_id,
            )
        )

        match bm.get_combatant(self.actor_slot):
            case FightCharacter() as fighter:
                pass
            case _:
                return bm

        match bm.get_combatant(self.target_slot):
            case FightCharacter() as target:
                pass
            case _:
                return bm

        use_advantage = self._compute_use_advantage(fighter, target)
        use_disadvantage = self._compute_use_disadvantage(fighter, target)
        roll1 = randint(1, 20)
        roll2 = randint(1, 20) if (use_advantage or use_disadvantage) else roll1
        if use_advantage and not use_disadvantage:
            roll = max(roll1, roll2)
        elif use_disadvantage and not use_advantage:
            roll = min(roll1, roll2)
        else:
            roll = roll1
        is_crit = roll == 20
        total_bonus = sum(
            m.apply(fighter, target)
            for m in fighter.modifiers
            if isinstance(m, AttackBonusModifier)
        )

        bm = bm.emit(
            CreatureAttackedEvent(
                attacker_id=fighter.id,
                defender_id=target.id,
                roll=roll,
                total_bonus=total_bonus,
                is_crit=is_crit,
                attack_id=attack_id,
            )
        )

        match bm.get_combatant(self.target_slot):
            case FightCharacter() as target:
                pass
            case _:
                return bm

        if roll + total_bonus >= target.ac:
            sneak_attack_rolls = 0
            if self.can_sneak_attack and not fighter.sneak_attack_used_this_turn:
                ally_adjacent = self._has_ally_adjacent_to_target(bm, fighter, target)
                if use_advantage or (ally_adjacent and not use_disadvantage):
                    sneak_attack_rolls = fighter.sneak_attack_dice * (
                        2 if is_crit else 1
                    )
                    bm = bm.replace_combatant(
                        self.actor_slot,
                        fighter.model_copy(
                            update={"sneak_attack_used_this_turn": True}
                        ),
                    )
            damage = (
                sum(randint(1, int(self.die)) for _ in range(self.n_dice))
                + self.ability_modifier
                + sum(
                    randint(1, int(HitDieSize.SIX)) for _ in range(sneak_attack_rolls)
                )
            )
            match bm.get_combatant(self.actor_slot):
                case FightCharacter() as fighter:
                    pass
                case _:
                    return bm
            if is_crit:
                damage += sum(
                    randint(1, int(self.die)) + self.ability_modifier
                    for _ in range(fighter.brutal_critical_dice)
                )

            damage_type = self.damage_type
            for m in fighter.modifiers:
                if isinstance(m, MagicalDamageModifier):
                    damage_type = m.upgrade(damage_type)

            if damage_type in target.all_resistances():
                damage //= 2

            bm = bm.emit(
                MeleeDamageEvent(
                    attacker_id=fighter.id,
                    defender_id=target.id,
                    damage=damage,
                    is_crit=is_crit,
                    attack_id=attack_id,
                )
            )

            match bm.get_combatant(self.target_slot):
                case FightCharacter():
                    bm = bm.deal_damage(self.target_slot, damage)
                case _:
                    pass

        return bm


class _MeleeAttack(Action[SlotT], Generic[SlotT]):
    range_tails: Literal[1] = 1
    actor_slot: SlotT
    executor: _MeleeAttackExecutor[SlotT]

    @classmethod
    @abstractmethod
    def _damage_die(cls) -> HitDieSize: ...

    @classmethod
    @abstractmethod
    def _ability(cls) -> AbilityName: ...

    @classmethod
    @abstractmethod
    def _weapon(cls) -> WeaponName: ...

    @classmethod
    @abstractmethod
    def _two_handed(cls) -> bool: ...

    @classmethod
    @abstractmethod
    def _stat(cls) -> Statistic: ...

    @classmethod
    @abstractmethod
    def _damage_type(cls) -> DamageType: ...

    @classmethod
    def _finesse(cls) -> bool:
        return False

    @classmethod
    def create(
        cls,
        actor_slot: SlotT,
        fighter: FightCharacter[SlotT],
        battlemap: Battlemap[SlotT],
    ) -> tuple[Self, ...]:
        if (
            fighter.attacks_remaining <= 0
            or cls._ability() not in fighter.character.actions
        ):
            return ()
        weapon = cls._weapon()
        if cls._two_handed():
            if fighter.main_hand != weapon or fighter.off_hand != weapon:
                return ()
        else:
            if fighter.main_hand != weapon and fighter.off_hand != weapon:
                return ()
        fx, fy = fighter.position.x, fighter.position.y
        die = cls._damage_die()
        damage_type = cls._damage_type()
        if cls._finesse():
            ability_modifier = max(
                fighter.character.stats.get_modifier(Statistic.STRENGTH),
                fighter.character.stats.get_modifier(Statistic.DEXTERITY),
            )
        else:
            ability_modifier = fighter.character.stats.get_modifier(cls._stat())
        can_sneak_attack = (
            cls._finesse() and AbilityName.SNEAK_ATTACK in fighter.character.actions
        )
        other_hand = (
            fighter.off_hand if fighter.main_hand == weapon else fighter.main_hand
        )
        if (
            fighter.character.fighting_style is FightingStyle.DUELING
            and not cls._two_handed()
            and other_hand in (None, WeaponName.SHIELD)
        ):
            ability_modifier += 2
        results: list[Self] = []
        for target_slot in battlemap.all_slots():
            match battlemap.get_combatant(target_slot):
                case FightCharacter() as target if target.position != fighter.position:
                    tx, ty = target.position.x, target.position.y
                    if max(abs(tx - fx), abs(ty - fy)) <= 1:
                        results.append(
                            cls(
                                name=cls._ability(),
                                actor_slot=actor_slot,
                                executor=_MeleeAttackExecutor(
                                    actor_slot=actor_slot,
                                    target_slot=target_slot,
                                    die=die,
                                    damage_type=damage_type,
                                    ability_modifier=ability_modifier,
                                    can_sneak_attack=can_sneak_attack,
                                ),
                            )
                        )
                case _:
                    pass
        return tuple(results)

    @classmethod
    def create_oa(
        cls,
        actor_slot: SlotT,
        attacker: FightCharacter[SlotT],
        target_slot: SlotT,
        battlemap: Battlemap[SlotT],
    ) -> tuple[Self, ...]:
        if cls._ability() not in attacker.character.actions:
            return ()
        if not attacker.has_reaction:
            return ()
        die = cls._damage_die()
        return (
            cls(
                name=cls._ability(),
                actor_slot=actor_slot,
                executor=_MeleeAttackExecutor(
                    actor_slot=actor_slot,
                    target_slot=target_slot,
                    die=die,
                    damage_type=cls._damage_type(),
                    is_oa=True,
                ),
            ),
        )

    def perform(self, battlemap: Battlemap[SlotT]) -> Battlemap[SlotT]:
        return self.executor.attack(battlemap)
