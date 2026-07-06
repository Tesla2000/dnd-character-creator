from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Generator
from enum import StrEnum
from typing import TYPE_CHECKING
from typing import Literal
from typing import Never
from typing import assert_never
from typing import cast
from typing import overload

from typing_extensions import deprecated
from typing_protocol_intersection import ProtocolIntersection

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.state import Blueprint
from dnd.character.blueprint.state import BlueprintProtocol
from dnd.character.blueprint.state import HasClasses
from dnd.character.blueprint.state import HasHealthBase
from dnd.character.delta.delta import Delta
from dnd.choices.class_creation.character_class import Class
from dnd.choices.equipment_creation.weapons import HitDieSize
from pydantic import Field


class HealthDeltaType(StrEnum):
    HEALTH_BASE = "HealthBaseDelta"


class HealthBaseDelta(Delta):
    """Delta produced when HealthIncrease updates health_base."""

    delta_type: Literal[HealthDeltaType.HEALTH_BASE] = HealthDeltaType.HEALTH_BASE
    health_base: int

    def apply[T: BlueprintProtocol](
        self, state: T
    ) -> ProtocolIntersection[T, HasHealthBase]:

        if TYPE_CHECKING:

            class BlueprintWithHealthBase(Blueprint):
                health_base: int

        else:

            class BlueprintWithHealthBase(type(state)):
                health_base: int

        return cast(
            ProtocolIntersection[T, HasHealthBase],
            BlueprintWithHealthBase.model_validate(
                {**dict(state), "health_base": self.health_base}
            ),
        )


class HealthIncrease(BuildingBlock, ABC):
    """Abstract base class for health increase strategies when leveling up.

    Subclasses must implement _get_hit_die_value to determine how much
    health to gain from the hit die (fixed value, random roll, etc.).
    """

    class_: Class = Field(
        description="The character class for which health is being increased"
    )

    @classmethod
    def _class_hit_die(cls, class_: Class) -> HitDieSize:
        match class_:
            case Class.BARBARIAN:
                return HitDieSize.TWELVE
            case Class.FIGHTER | Class.PALADIN | Class.RANGER:
                return HitDieSize.TEN
            case Class.SORCERER | Class.WIZARD:
                return HitDieSize.SIX
            case (
                Class.BARD
                | Class.CLERIC
                | Class.DRUID
                | Class.MONK
                | Class.ROGUE
                | Class.WARLOCK
                | Class.ARTIFICER
            ):
                return HitDieSize.EIGHT
            case _ as never:
                assert_never(never)

    @abstractmethod
    def _get_hit_die_value(self, hit_die: HitDieSize) -> int: ...

    @overload
    def get_change[T: HasClasses](
        self, state: T
    ) -> Generator[HealthBaseDelta, None, ProtocolIntersection[T, HasHealthBase]]: ...

    @overload
    @deprecated("Pass a state satisfying HasClasses for precise return typing")
    def get_change[T: BlueprintProtocol](self, state: T) -> Never: ...

    def get_change[T: BlueprintProtocol](
        self, state: T
    ) -> Generator[Delta, None, BlueprintProtocol]:
        if not isinstance(state, HasClasses):
            raise TypeError(
                f"{type(self).__name__} requires HasClasses, got {type(state).__name__}"
            )
        hit_die = self._class_hit_die(self.class_)
        current_health: int | None = (
            state.health_base if isinstance(state, HasHealthBase) else None
        )

        if current_health is None:
            hit_die_value = hit_die.value
            current_health = 0
        else:
            hit_die_value = self._get_hit_die_value(hit_die)

        delta = HealthBaseDelta(health_base=current_health + hit_die_value)
        yield delta
        return delta.apply(state)
