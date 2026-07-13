import typing
from collections.abc import Iterable

from pydantic import BaseModel
from pydantic._internal._generics import PydanticGenericMetadata

from dnd.character.blueprint.building_blocks import AnyBuildingBlock
from dnd.character.blueprint.states.state import AnyBluprint


def _generic_origin(cls: type[BaseModel]) -> type:
    meta: PydanticGenericMetadata = cls.__pydantic_generic_metadata__
    origin = meta["origin"]
    return origin if isinstance(origin, type) else cls


def _generic_args(cls: type[BaseModel]) -> tuple[object, ...]:
    meta: PydanticGenericMetadata = cls.__pydantic_generic_metadata__
    args: tuple[object, ...] = meta["args"]
    return args


def _arg_compatible(current: object, expected: object) -> bool:
    if isinstance(expected, typing.TypeVar):
        return True
    if current is expected:
        return True
    expected_origin = typing.get_origin(expected)
    current_origin = typing.get_origin(current)
    if expected_origin is typing.Literal:
        if current_origin is typing.Literal:
            return set(typing.get_args(current)) <= set(typing.get_args(expected))
        return False
    if isinstance(expected, type) and isinstance(current, type):
        return issubclass(current, expected)
    if expected_origin is not None and current_origin is not None:
        if not (isinstance(expected_origin, type) and isinstance(current_origin, type)):
            return current == expected
        if not issubclass(current_origin, expected_origin):
            return False
        for c, e in zip(typing.get_args(current), typing.get_args(expected)):
            if not _arg_compatible(c, e):
                return False
        return True
    return current == expected


def _validate_pipeline(
    initial: AnyBluprint,
    building_blocks: Iterable[AnyBuildingBlock],
) -> None:
    """Raise TypeError if building_blocks cannot be chained starting from initial."""
    initial_cls = type(initial)
    current_origin: type = _generic_origin(initial_cls)
    current_args: tuple[object, ...] = _generic_args(initial_cls)

    for i, block in enumerate(building_blocks):
        hints = typing.get_type_hints(block.apply)
        input_hint = hints["blueprint"]
        return_hint = hints["return"]

        if isinstance(input_hint, typing.TypeVar):
            continue

        input_type: type = input_hint
        if issubclass(input_type, BaseModel):
            input_origin = _generic_origin(input_type)
            input_args = _generic_args(input_type)
        else:
            input_origin = input_type
            input_args = ()

        if not issubclass(current_origin, input_origin):
            raise TypeError(
                f"Block {i} ({type(block).__name__}): expected {input_origin.__name__},"
                f" got {current_origin.__name__}"
            )

        for j, (curr_arg, inp_arg) in enumerate(zip(current_args, input_args)):
            if not _arg_compatible(curr_arg, inp_arg):
                raise TypeError(
                    f"Block {i} ({type(block).__name__}): type arg [{j}] mismatch"
                    f" — got {curr_arg!r}, expected {inp_arg!r}"
                )

        if isinstance(return_hint, typing.TypeVar):
            continue

        return_type: type[BaseModel] = return_hint
        new_origin = _generic_origin(return_type)
        new_args = _generic_args(return_type)
        current_origin = new_origin
        current_args = tuple(
            current_args[j]
            if isinstance(a, typing.TypeVar) and j < len(current_args)
            else a
            for j, a in enumerate(new_args)
        )
