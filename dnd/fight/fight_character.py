from __future__ import annotations

from enum import IntEnum
from random import randint
from typing import (
    TYPE_CHECKING,
    Annotated,
    ClassVar,
    Generic,
)
from uuid import uuid4

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    InstanceOf,
    NonNegativeInt,
    PositiveInt,
)
from typing import Self
from uuid_string import UUIDString

if TYPE_CHECKING:
    pass

from dnd._position import Position
from dnd.character._ability_name import AbilityName
from dnd.character.actions._any_modifier import AnyModifier
from dnd.character.actions._damage_type import DamageType
from dnd.character.actions.advantage_modifier import (
    AdvantageModifier,
    DisadvantageModifier,
    GrantsAdvantageModifier,
)
from dnd.character.actions.damage_resistance_modifier import DamageResistanceModifier
from dnd.fight._combat_event import (
    AnyCombatEvent,
    RageEndsEvent,
    TurnStartEvent,
)
from dnd.fight._team_id import TeamId
from dnd.character.actions.magical_damage_modifier import (
    PrimalStrikeMagicalDamageModifier,
)
from dnd.character.presentable_character import PresentableCharacter
from dnd.character.spells.max_spell_levels import SpellSlots
from dnd.choices.equipment_creation.weapons import TWO_HANDED_WEAPONS, WeaponName
from dnd.choices.stats_creation.statistic import Statistic
from dnd.fight._combatant_slot import SlotT
from dnd.fight._condition import Condition
from dnd.fight._fight_resource import _FightResource, ResourceName
from dnd.other_profficiencies import ArmorProficiency


class _CombatantBase[HealthType: NonNegativeInt](BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    character: InstanceOf[PresentableCharacter]
    initiative: int
    max_health: PositiveInt
    current_health: HealthType
    temporary_health: NonNegativeInt = 0
    conditions: frozenset[Condition] = frozenset()
    resources: tuple[_FightResource, ...] = ()
    team_id: TeamId = TeamId.A
    speed: int = 30
    movement_remaining: int = 0
    position: Position = Position(x=0, y=0)

    @property
    def name(self) -> str:
        return self.character.character_data.name or "Unknown"

    def add_condition(self, c: Condition) -> Self:
        return self.model_copy(update={"conditions": self.conditions | {c}})

    def remove_condition(self, c: Condition) -> Self:
        return self.model_copy(update={"conditions": self.conditions - {c}})

    def use_resource(self, name: ResourceName) -> Self:
        updated = tuple(
            r.model_copy(update={"remaining_uses": max(0, r.remaining_uses - 1)})
            if r.name == name
            else r
            for r in self.resources
        )
        return self.model_copy(update={"resources": updated})

    def add_temporary_health(self, amount: int) -> Self:
        new_temp = max(self.temporary_health, amount)
        return self.model_copy(update={"temporary_health": new_temp})

    def on_event[T: IntEnum](
        self, event: AnyCombatEvent[T]
    ) -> tuple[Self, tuple[AnyCombatEvent[T], ...]]:
        return self, ()


class FightCharacter(_CombatantBase[PositiveInt], Generic[SlotT]):
    has_action: bool = True
    has_bonus_action: bool = True
    has_reaction: bool = True
    has_free_action: bool = True
    base_ac: int = 10
    modifiers: tuple[AnyModifier, ...] = ()
    damage_resistance: frozenset[DamageType] = frozenset()
    condition_immunities: frozenset[Condition] = frozenset()
    active_features: frozenset[AbilityName] = frozenset()
    id: UUIDString = Field(default_factory=lambda: UUIDString(str(uuid4())))
    number_of_attacks: int = 1
    attacks_remaining: int = 1
    brutal_critical_dice: int = 0
    con_save_bonus: int = 0
    main_hand: WeaponName | None = None
    off_hand: WeaponName | None = None
    summoned_by: SlotT | None = None
    sneak_attack_dice: NonNegativeInt = 0
    sneak_attack_used_this_turn: bool = False
    disengaging: bool = False

    @property
    def ac(self) -> int:
        shield_held = (
            self.main_hand == WeaponName.SHIELD or self.off_hand == WeaponName.SHIELD
        )
        shield_prof = ArmorProficiency.SHIELDS in self.character.armor_proficiencies
        return self.base_ac + (2 if shield_held and shield_prof else 0)

    def all_resistances(self) -> frozenset[DamageType]:
        return self.damage_resistance | frozenset[DamageType]().union(
            *(
                m.get_resistances()
                for m in self.modifiers
                if isinstance(m, DamageResistanceModifier)
            )
        )

    @staticmethod
    def _resources_from_character(
        character: PresentableCharacter,
    ) -> tuple[_FightResource, ...]:
        return tuple(
            _FightResource(name=r.name, max_uses=r.max_uses, remaining_uses=r.max_uses)
            for r in character.resource_max_uses
        )

    @classmethod
    def from_presentable(
        cls,
        character: PresentableCharacter,
        initiative: int,
        resources: tuple[_FightResource, ...] | None = None,
        team_id: TeamId = TeamId.A,
    ) -> FightCharacter[SlotT]:
        if resources is None:
            resources = cls._resources_from_character(character)
        number_of_attacks = 2 if AbilityName.EXTRA_ATTACK in character.actions else 1
        brutal_critical_dice = (
            3
            if AbilityName.BRUTAL_CRITICAL_3_DICE in character.actions
            else 2
            if AbilityName.BRUTAL_CRITICAL_2_DICE in character.actions
            else 1
            if AbilityName.BRUTAL_CRITICAL_1_DIE in character.actions
            else 0
        )
        con_save_bonus = character.stats.get_modifier(Statistic.CONSTITUTION)
        weapons = character.weapons
        has_shield = WeaponName.SHIELD in character.other_equipment
        main_hand: WeaponName | None = None
        off_hand: WeaponName | None = None
        for w in weapons:
            if w in TWO_HANDED_WEAPONS:
                main_hand = w
                off_hand = w
                break
            if main_hand is None:
                main_hand = w
            elif off_hand is None:
                off_hand = w
                break
        if has_shield and off_hand is None:
            off_hand = WeaponName.SHIELD
        modifiers: tuple[AnyModifier, ...] = (
            (PrimalStrikeMagicalDamageModifier(),)
            if AbilityName.PRIMAL_STRIKE in character.actions
            else ()
        )
        sneak_attack_dice = (
            (character.classes.rogue + 1) // 2
            if AbilityName.SNEAK_ATTACK in character.actions
            else 0
        )
        return cls(
            character=character,
            initiative=initiative,
            max_health=character.health,
            current_health=character.health,
            base_ac=character.ac,
            resources=resources,
            team_id=team_id,
            speed=character.speed or 30,
            number_of_attacks=number_of_attacks,
            attacks_remaining=number_of_attacks,
            brutal_critical_dice=brutal_critical_dice,
            con_save_bonus=con_save_bonus,
            main_hand=main_hand,
            off_hand=off_hand,
            modifiers=modifiers,
            sneak_attack_dice=sneak_attack_dice,
        )

    def on_event[T: IntEnum](
        self, event: AnyCombatEvent[T]
    ) -> tuple[Self, tuple[AnyCombatEvent[T], ...]]:
        pending: list[AnyCombatEvent[T]] = []
        surviving: list[AnyModifier] = []
        for m in self.modifiers:
            r, emitted = m.on_event(event)
            pending.extend(emitted)
            if r is not None:
                surviving.append(r)

        update: dict[str, object] = {}

        match event:
            case TurnStartEvent() if event.target_id == self.id:
                update["has_action"] = True
                update["has_bonus_action"] = True
                update["has_reaction"] = True
                update["has_free_action"] = True
                update["attacks_remaining"] = self.number_of_attacks
                update["movement_remaining"] = self.speed
                update["sneak_attack_used_this_turn"] = False
                update["disengaging"] = False
                surviving = [
                    m
                    for m in surviving
                    if not isinstance(
                        m,
                        (
                            AdvantageModifier,
                            DisadvantageModifier,
                            GrantsAdvantageModifier,
                        ),
                    )
                ]
            case RageEndsEvent() if event.target_id == self.id:
                update["active_features"] = self.active_features - {AbilityName.RAGE}
            case _:
                pass

        update["modifiers"] = tuple(surviving)
        return self.model_copy(update=update), tuple(pending)

    def spend_attack(self) -> Self:
        return self.model_copy(
            update={
                "attacks_remaining": self.attacks_remaining - 1,
                "has_action": False,
            }
        )

    def spend_action(self) -> Self:
        return self.model_copy(update={"has_action": False})

    def spend_bonus_action(self) -> Self:
        return self.model_copy(update={"has_bonus_action": False})

    def spend_reaction(self) -> Self:
        return self.model_copy(update={"has_reaction": False})

    def spend_free_action(self) -> Self:
        return self.model_copy(update={"has_free_action": False})

    def take_damage(self, amount: int) -> FightCharacter[SlotT] | DownedFightCharacter:
        remaining = amount
        new_temp = self.temporary_health
        if new_temp > 0:
            absorbed = min(new_temp, remaining)
            new_temp -= absorbed
            remaining -= absorbed
        new_hp = self.current_health - remaining
        active_features = self.active_features
        if AbilityName.WILD_SHAPE in active_features and new_temp == 0:
            active_features = active_features - {AbilityName.WILD_SHAPE}
        if new_hp <= 0:
            if (
                self.has_reaction
                and AbilityName.RELENTLESS_RAGE in self.character.actions
                and randint(1, 20) + self.con_save_bonus >= 10
            ):
                return self.model_copy(
                    update={
                        "current_health": 1,
                        "temporary_health": new_temp,
                        "has_reaction": False,
                        "active_features": active_features,
                    }
                )
            return DownedFightCharacter.from_active(
                self.model_copy(
                    update={"current_health": 1, "temporary_health": new_temp}
                )
            )
        return self.model_copy(
            update={
                "current_health": new_hp,
                "temporary_health": new_temp,
                "active_features": active_features,
            }
        )

    def heal(self, amount: int) -> Self:
        new_hp = min(self.current_health + amount, self.max_health)
        return self.model_copy(update={"current_health": new_hp})


class SpellcasterFightCharacter(FightCharacter[SlotT], Generic[SlotT]):
    remaining_spell_slots: SpellSlots

    @classmethod
    def from_presentable(
        cls,
        character: PresentableCharacter,
        initiative: int,
        resources: tuple[_FightResource, ...] | None = None,
        team_id: TeamId = TeamId.A,
    ) -> SpellcasterFightCharacter[SlotT]:
        if resources is None:
            resources = cls._resources_from_character(character)
        number_of_attacks = 2 if AbilityName.EXTRA_ATTACK in character.actions else 1
        brutal_critical_dice = (
            3
            if AbilityName.BRUTAL_CRITICAL_3_DICE in character.actions
            else 2
            if AbilityName.BRUTAL_CRITICAL_2_DICE in character.actions
            else 1
            if AbilityName.BRUTAL_CRITICAL_1_DIE in character.actions
            else 0
        )
        con_save_bonus = character.stats.get_modifier(Statistic.CONSTITUTION)
        weapons = character.weapons
        has_shield = WeaponName.SHIELD in character.other_equipment
        main_hand: WeaponName | None = None
        off_hand: WeaponName | None = None
        for w in weapons:
            if w in TWO_HANDED_WEAPONS:
                main_hand = w
                off_hand = w
                break
            if main_hand is None:
                main_hand = w
            elif off_hand is None:
                off_hand = w
                break
        if has_shield and off_hand is None:
            off_hand = WeaponName.SHIELD
        caster_info = character.caster
        assert caster_info is not None
        modifiers: tuple[AnyModifier, ...] = (
            (PrimalStrikeMagicalDamageModifier(),)
            if AbilityName.PRIMAL_STRIKE in character.actions
            else ()
        )
        sneak_attack_dice = (
            (character.classes.rogue + 1) // 2
            if AbilityName.SNEAK_ATTACK in character.actions
            else 0
        )
        return cls(
            character=character,
            initiative=initiative,
            max_health=character.health,
            current_health=character.health,
            base_ac=character.ac,
            remaining_spell_slots=caster_info.spell_slots,
            resources=resources,
            team_id=team_id,
            speed=character.speed or 30,
            number_of_attacks=number_of_attacks,
            attacks_remaining=number_of_attacks,
            brutal_critical_dice=brutal_critical_dice,
            con_save_bonus=con_save_bonus,
            main_hand=main_hand,
            off_hand=off_hand,
            modifiers=modifiers,
            sneak_attack_dice=sneak_attack_dice,
        )

    def spend_level_1_slot(self) -> Self:
        return self.model_copy(
            update={
                "remaining_spell_slots": self.remaining_spell_slots.spend_level_1_slot()
            }
        )

    def spend_level_2_slot(self) -> Self:
        return self.model_copy(
            update={
                "remaining_spell_slots": self.remaining_spell_slots.spend_level_2_slot()
            }
        )

    def spend_level_3_slot(self) -> Self:
        return self.model_copy(
            update={
                "remaining_spell_slots": self.remaining_spell_slots.spend_level_3_slot()
            }
        )

    def spend_level_4_slot(self) -> Self:
        return self.model_copy(
            update={
                "remaining_spell_slots": self.remaining_spell_slots.spend_level_4_slot()
            }
        )


class DownedFightCharacter(_CombatantBase[NonNegativeInt]):
    current_health: NonNegativeInt = 0
    death_save_successes: Annotated[int, Field(ge=0, le=3)] = 0
    death_save_failures: Annotated[int, Field(ge=0, le=3)] = 0

    @classmethod
    def from_active[T: IntEnum](cls, fc: FightCharacter[T]) -> DownedFightCharacter:
        return cls(
            character=fc.character,
            initiative=fc.initiative,
            max_health=fc.max_health,
            current_health=0,
            temporary_health=0,
            conditions=fc.conditions | {Condition.UNCONSCIOUS},
            resources=fc.resources,
            team_id=fc.team_id,
            speed=fc.speed,
            position=fc.position,
        )

    def make_death_save(
        self, success: bool
    ) -> DownedFightCharacter | StabilizedFightCharacter | DeadFightCharacter:
        if success:
            new_successes = self.death_save_successes + 1
            if new_successes >= 3:
                return StabilizedFightCharacter.from_downed(self)
            return self.model_copy(update={"death_save_successes": new_successes})
        new_failures = self.death_save_failures + 1
        if new_failures >= 3:
            return DeadFightCharacter.from_downed(self)
        return self.model_copy(update={"death_save_failures": new_failures})

    def take_damage(self, amount: int) -> Self:
        new_failures = min(3, self.death_save_failures + 1)
        return self.model_copy(update={"death_save_failures": new_failures})

    def heal[T: IntEnum](self, amount: int) -> FightCharacter[T]:
        new_hp = min(amount, self.max_health)
        return FightCharacter(
            character=self.character,
            initiative=self.initiative,
            max_health=self.max_health,
            current_health=new_hp if new_hp > 0 else 1,
            temporary_health=self.temporary_health,
            conditions=self.conditions - {Condition.UNCONSCIOUS},
            resources=self.resources,
            team_id=self.team_id,
            speed=self.speed,
            position=self.position,
        )


class StabilizedFightCharacter(_CombatantBase[NonNegativeInt]):
    current_health: NonNegativeInt = 0

    @classmethod
    def from_downed(cls, fc: DownedFightCharacter) -> StabilizedFightCharacter:
        return cls(
            character=fc.character,
            initiative=fc.initiative,
            max_health=fc.max_health,
            current_health=0,
            temporary_health=fc.temporary_health,
            conditions=fc.conditions,
            resources=fc.resources,
            team_id=fc.team_id,
            speed=fc.speed,
            position=fc.position,
        )

    def heal[T: IntEnum](self, amount: int) -> FightCharacter[T]:
        new_hp = min(amount, self.max_health)
        return FightCharacter(
            character=self.character,
            initiative=self.initiative,
            max_health=self.max_health,
            current_health=new_hp if new_hp > 0 else 1,
            temporary_health=self.temporary_health,
            conditions=self.conditions - {Condition.UNCONSCIOUS},
            resources=self.resources,
            team_id=self.team_id,
            speed=self.speed,
            position=self.position,
        )


class DeadFightCharacter(_CombatantBase[NonNegativeInt]):
    current_health: NonNegativeInt = 0

    @classmethod
    def from_downed(cls, fc: DownedFightCharacter) -> DeadFightCharacter:
        return cls(
            character=fc.character,
            initiative=fc.initiative,
            max_health=fc.max_health,
            current_health=0,
            temporary_health=0,
            conditions=fc.conditions | {Condition.UNCONSCIOUS},
            resources=fc.resources,
            team_id=fc.team_id,
            speed=fc.speed,
            position=fc.position,
        )

    def revive[T: IntEnum](self, amount: int) -> FightCharacter[T]:
        new_hp = min(max(1, amount), self.max_health)
        return FightCharacter(
            character=self.character,
            initiative=self.initiative,
            max_health=self.max_health,
            current_health=new_hp,
            temporary_health=0,
            conditions=self.conditions - {Condition.UNCONSCIOUS},
            resources=self.resources,
            team_id=self.team_id,
            speed=self.speed,
            position=self.position,
        )


class UnsummonedFightCharacter(_CombatantBase[NonNegativeInt]):
    current_health: NonNegativeInt = 0

    @classmethod
    def reserved_for_summon(
        cls,
        presentable: PresentableCharacter,
        initiative: int,
        team_id: TeamId,
        position: Position,
    ) -> UnsummonedFightCharacter:
        return cls(
            character=presentable,
            initiative=initiative,
            max_health=presentable.health,
            current_health=0,
            team_id=team_id,
            position=position,
        )

    @classmethod
    def from_vanished[T: IntEnum](cls, fc: FightCharacter[T]) -> UnsummonedFightCharacter:
        return cls(
            character=fc.character,
            initiative=fc.initiative,
            max_health=fc.max_health,
            current_health=0,
            team_id=fc.team_id,
            position=fc.position,
        )


type AnyActiveCombatant[SlotT: IntEnum] = (
    InstanceOf[FightCharacter[SlotT]]
    | InstanceOf[SpellcasterFightCharacter[SlotT]]
    | InstanceOf[DownedFightCharacter]
    | InstanceOf[StabilizedFightCharacter]
    | InstanceOf[DeadFightCharacter]
    | InstanceOf[UnsummonedFightCharacter]
)
