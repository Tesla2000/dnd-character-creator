from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Generator
from typing import Any
from typing import Callable
from typing import Literal
from typing import Self
from typing import TYPE_CHECKING
from typing import Union

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from pydantic import BaseModel
from pydantic import computed_field
from pydantic import ConfigDict
from pydantic import InstanceOf
from pydantic.main import IncEx

if TYPE_CHECKING:
    from dnd_character_creator.character.blueprint.building_blocks import (
        AnyBuildingBlock,
    )

BLOCK_TYPE_FIELD_NAME = "block_type"


class SerializableBlock(BaseModel):
    model_config = ConfigDict(frozen=True)

    @computed_field(alias=BLOCK_TYPE_FIELD_NAME)
    @property
    def block_type(self) -> str:
        """Return the class name as the block type for polymorphic serialization."""
        return self.get_block_type()

    @classmethod
    def get_block_type(cls) -> str:
        return cls.__name__

    def model_dump(
        self,
        *,
        mode: Literal["json", "python"] | str = "python",
        include: IncEx | None = None,
        exclude: IncEx | None = None,
        context: Any | None = None,
        by_alias: bool | None = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        exclude_computed_fields: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal["none", "warn", "error"] = True,
        fallback: Callable[[Any], Any] | None = None,
        serialize_as_any: bool = False,
    ) -> dict[str, Any]:
        return super().model_dump(
            mode=mode,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            exclude_computed_fields=exclude_computed_fields,
            round_trip=round_trip,
            warnings=warnings,
            fallback=fallback,
            serialize_as_any=True,
        )

    def model_dump_json(
        self,
        *,
        indent: int | None = None,
        ensure_ascii: bool = False,
        include: IncEx | None = None,
        exclude: IncEx | None = None,
        context: Any | None = None,
        by_alias: bool | None = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        exclude_computed_fields: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal["none", "warn", "error"] = True,
        fallback: Callable[[Any], Any] | None = None,
        serialize_as_any: bool = False,
    ) -> str:
        return super().model_dump_json(
            indent=indent,
            ensure_ascii=ensure_ascii,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            exclude_computed_fields=exclude_computed_fields,
            round_trip=round_trip,
            warnings=warnings,
            fallback=fallback,
            serialize_as_any=True,
        )


class CombinedBlock(SerializableBlock):
    """Combines multiple building blocks to apply sequentially."""

    blocks: tuple[
        Union["AnyBuildingBlock", Self, InstanceOf[BuildingBlock]], ...
    ]

    def __add__(self, other: Any) -> Self:
        allowed_types = (BuildingBlock, CombinedBlock)
        if not isinstance(other, allowed_types):
            raise ValueError(
                f"Only instances of {allowed_types} allowed for {type(self).__name__} addition"
            )
        if isinstance(other, CombinedBlock):
            return type(self)(blocks=self.blocks + other.blocks)
        if isinstance(other, BuildingBlock):
            return type(self)(blocks=self.blocks + (other,))
        raise ValueError("What?")

    def flatten(self) -> Generator[BuildingBlock, None, None]:
        for block in self.blocks:
            if not isinstance(block, CombinedBlock):
                yield block
            else:
                yield from block.flatten()


class BuildingBlock(SerializableBlock, ABC):
    @abstractmethod
    def get_change(self, blueprint: Blueprint) -> Blueprint:
        """Returns Blueprint differences to apply.

        Receives the current blueprint state from yield returns,
        allowing decisions based on current state.
        """

    def __add__(self, other: BuildingBlock) -> CombinedBlock:
        return CombinedBlock(blocks=(self, other))
