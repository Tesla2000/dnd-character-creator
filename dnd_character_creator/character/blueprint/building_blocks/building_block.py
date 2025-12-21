from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Generator
from typing import Any
from typing import ClassVar
from typing import Self
from typing import Union

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from pydantic import BaseModel
from pydantic import computed_field
from pydantic import ConfigDict
from pydantic import SerializeAsAny
from pydantic.config import ExtraValues

BLOCK_TYPE_FIELD_NAME = "block_type"


class BuildingBlock(BaseModel, ABC):
    model_config = ConfigDict(frozen=True)

    _type_registry: ClassVar[dict[str, type[BuildingBlock]]] = {}

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """Register subclasses for polymorphic deserialization."""
        super().__init_subclass__(**kwargs)
        if ABC not in cls.__bases__:  # Only register concrete classes
            BuildingBlock._type_registry[cls.__name__] = cls

    @computed_field(alias=BLOCK_TYPE_FIELD_NAME)  # type: ignore[prop-decorator]
    @property
    def block_type(self) -> str:
        """Return the class name as the block type for polymorphic serialization."""
        return self.get_block_type()

    @classmethod
    def get_block_type(cls) -> str:
        return cls.__name__

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
            if not isinstance(obj, dict) or BLOCK_TYPE_FIELD_NAME not in obj:
                raise e
            return BuildingBlock._type_registry[
                obj[BLOCK_TYPE_FIELD_NAME]
            ].model_validate(
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


class CombinedBlock(BaseModel):
    """Combines multiple building blocks to apply sequentially."""

    blocks: tuple[Union[SerializeAsAny[BuildingBlock], Self], ...]

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
