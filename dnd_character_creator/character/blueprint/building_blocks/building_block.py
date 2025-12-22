from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Generator
from typing import Any
from typing import Callable
from typing import Literal
from typing import Self
from typing import Union

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from pydantic import BaseModel
from pydantic import computed_field
from pydantic import ConfigDict
from pydantic.config import ExtraValues
from pydantic.main import IncEx

_BLOCK_TYPE_FIELD_NAME = "block_type"


class _SerializableBlock(BaseModel):

    @computed_field(alias=_BLOCK_TYPE_FIELD_NAME)  # type: ignore[prop-decorator]
    @property
    def block_type(self) -> str:
        """Return the class name as the block type for polymorphic serialization."""
        return self.get_block_type()

    @classmethod
    def get_block_type(cls) -> str:
        return cls.__name__

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """Register subclasses for polymorphic deserialization."""
        super().__init_subclass__(**kwargs)
        if (
            ABC not in cls.__bases__
            and _SerializableBlock not in cls.__bases__
        ):
            _TYPE_REGISTRY[cls.__name__] = cls

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


class CombinedBlock(_SerializableBlock):
    """Combines multiple building blocks to apply sequentially."""

    blocks: tuple[Union[BuildingBlock, Self], ...]

    def add(self, other: Union[BuildingBlock, Self]) -> Self:
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

    def __add__(self, other) -> Self:
        return self.add(other)

    def flatten(self) -> Generator[BuildingBlock, None, None]:
        for block in self.blocks:
            if not isinstance(block, CombinedBlock):
                yield block
            else:
                yield from block.flatten()

    @classmethod
    def model_validate(
        cls,
        obj: Any,
        *,
        strict: bool | None = None,
        extra: ExtraValues | None = None,
        from_attributes: bool | None = None,
        context: Any | None = None,
        by_alias: bool | None = None,
        by_name: bool | None = None,
    ) -> Self:
        if isinstance(obj, dict):
            obj["blocks"] = list(
                BuildingBlock.model_validate(
                    elem,
                    strict=strict,
                    extra=extra,
                    from_attributes=from_attributes,
                    context=context,
                    by_alias=by_alias,
                    by_name=by_name,
                )
                for elem in obj["blocks"]
            )
        return super().model_validate(
            obj,
            strict=strict,
            extra=extra,
            from_attributes=from_attributes,
            context=context,
            by_alias=by_alias,
            by_name=by_name,
        )


class BuildingBlock(_SerializableBlock, ABC):
    model_config = ConfigDict(frozen=True)

    @classmethod
    def model_validate(
        cls,
        obj: Any,
        *,
        strict: bool | None = None,
        extra: ExtraValues | None = None,
        from_attributes: bool | None = None,
        context: Any | None = None,
        by_alias: bool | None = None,
        by_name: bool | None = None,
    ) -> Self:
        try:
            return super().model_validate(
                obj,
                strict=strict,
                extra=extra,
                from_attributes=from_attributes,
                context=context,
                by_alias=by_alias,
                by_name=by_name,
            )
        except TypeError as e:
            if not isinstance(obj, dict) or _BLOCK_TYPE_FIELD_NAME not in obj:
                raise e
            return _TYPE_REGISTRY[obj[_BLOCK_TYPE_FIELD_NAME]].model_validate(
                obj,
                strict=strict,
                extra=extra,
                from_attributes=from_attributes,
                context=context,
                by_alias=by_alias,
                by_name=by_name,
            )

    @abstractmethod
    def get_change(self, blueprint: Blueprint) -> Blueprint:
        """Returns Blueprint differences to apply.

        Receives the current blueprint state from yield returns,
        allowing decisions based on current state.
        """

    def __add__(self, other: BuildingBlock) -> CombinedBlock:
        return CombinedBlock(blocks=(self, other))


_TYPE_REGISTRY: dict[str, type[_SerializableBlock]] = {
    CombinedBlock.get_block_type(): CombinedBlock
}
