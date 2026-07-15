from __future__ import annotations

import types
import typing
from collections.abc import Iterable
from typing import TypeAlias

from pydantic import BaseModel
from pydantic._internal._generics import PydanticGenericMetadata

from dnd.character.blueprint.building_blocks import AnyBuildingBlock
from dnd.character.blueprint.states.state import AnyBluprint
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.presentable_character import PresentableCharacter

_Bindings: TypeAlias = dict[object, object]


def _generic_origin(cls: type[BaseModel]) -> type:
    meta: PydanticGenericMetadata = cls.__pydantic_generic_metadata__
    origin = meta["origin"]
    return origin if isinstance(origin, type) else cls


def _generic_args(cls: type[BaseModel]) -> tuple[object, ...]:
    meta: PydanticGenericMetadata = cls.__pydantic_generic_metadata__
    args: tuple[object, ...] = meta["args"]
    return args


def _unwrap_alias(t: object) -> object:
    """Resolve TypeAliasType to its underlying value."""
    if isinstance(t, typing.TypeAliasType):
        return _unwrap_alias(t.__value__)
    return t


def _arg_compatible(current: object, expected: object) -> bool:
    if isinstance(expected, typing.TypeVar):
        return True
    if isinstance(current, typing.TypeVar):
        bound = current.__bound__
        if bound is None:
            return True
        return _arg_compatible(_unwrap_alias(bound), _unwrap_alias(expected))
    if current is expected:
        return True
    current = _unwrap_alias(current)
    expected = _unwrap_alias(expected)
    if current is expected:
        return True
    expected_origin = typing.get_origin(expected)
    current_origin = typing.get_origin(current)
    _union_origins = (typing.Union, types.UnionType)
    # Check current union first: A|B <: C iff A <: C and B <: C
    if current_origin in _union_origins:
        return all(_arg_compatible(c, expected) for c in typing.get_args(current))
    if expected_origin in _union_origins:
        return any(_arg_compatible(current, e) for e in typing.get_args(expected))
    if expected_origin is typing.Literal:
        if current_origin is typing.Literal:
            return set(typing.get_args(current)) <= set(typing.get_args(expected))
        # For Literal[0]: accept int-compatible types — value may be 0 at runtime;
        # model_validate is the real enforcement gate.
        if typing.get_args(expected) == (0,):
            if isinstance(current, type) and issubclass(current, int):
                return True
            if current_origin is typing.Annotated:
                inner = (
                    typing.get_args(current)[0] if typing.get_args(current) else None
                )
                return isinstance(inner, type) and issubclass(inner, int)
        return False
    if isinstance(expected, type) and isinstance(current, type):
        return issubclass(current, expected)
    if isinstance(expected, type) and current_origin is typing.Literal:
        return all(isinstance(v, expected) for v in typing.get_args(current))
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


def _collect_class_bindings(block_type: type) -> _Bindings:
    """Resolve class-level TypeVars to concrete types via Pydantic's generic metadata."""
    bindings: _Bindings = {}
    for cls in block_type.__mro__:
        meta = vars(cls).get("__pydantic_generic_metadata__", {})
        origin = meta.get("origin")
        args: tuple[object, ...] = meta.get("args", ())
        if origin is None or not args:
            continue
        origin_meta = vars(origin).get("__pydantic_generic_metadata__", {})
        params: tuple[object, ...] = origin_meta.get("parameters", ())
        for tv, arg in zip(params, args):
            if tv not in bindings:
                bindings[tv] = _substitute(arg, bindings)
    return bindings


def _substitute(arg: object, bindings: _Bindings) -> object:
    if arg in bindings:
        return _substitute(bindings[arg], bindings)
    origin = typing.get_origin(arg)
    if origin is not None:
        args = typing.get_args(arg)
        new_args = tuple(_substitute(a, bindings) for a in args)
        if new_args != args:
            return origin[new_args] if len(new_args) > 1 else origin[new_args[0]]
    return arg


def _expand_to_blueprint_args(
    cls: type,
    cls_args: tuple[object, ...],
    outer_bindings: _Bindings | None = None,
) -> tuple[object, ...] | None:
    """Expand a Blueprint subclass with given type args to Blueprint's 19 type args."""
    bindings: _Bindings = dict(outer_bindings or {})
    cls_meta = vars(cls).get("__pydantic_generic_metadata__", {})
    params = cls_meta.get("parameters", ())
    for tv, a in zip(params, cls_args):
        bindings[tv] = a

    for base in vars(cls).get("__orig_bases__", []):
        base_meta = vars(base).get("__pydantic_generic_metadata__")
        if base_meta is None:
            continue
        base_origin = base_meta.get("origin")
        base_args: tuple[object, ...] = base_meta.get("args", ())
        if base_origin is Blueprint:
            return tuple(_substitute(a, bindings) for a in base_args)
        if (
            base_origin is not None
            and isinstance(base_origin, type)
            and issubclass(base_origin, Blueprint)
        ):
            substituted = tuple(_substitute(a, bindings) for a in base_args)
            result = _expand_to_blueprint_args(base_origin, substituted, bindings)
            if result is not None:
                return result
        if (
            base_origin is None
            and isinstance(base, type)
            and base is not Blueprint
            and issubclass(base, Blueprint)
        ):
            result = _expand_to_blueprint_args(base, (), bindings)
            if result is not None:
                return result
    return None


def _to_blueprint_level(origin: type, args: tuple[object, ...]) -> tuple[object, ...]:
    """Return Blueprint-level args for a Blueprint (sub)class, or args unchanged."""
    if origin is Blueprint:
        return args
    if isinstance(origin, type) and issubclass(origin, Blueprint):
        expanded = _expand_to_blueprint_args(origin, args)
        if expanded is not None:
            return expanded
    return args


def _presentable_blueprint_args() -> tuple[object, ...]:
    """Return the Blueprint type args required by PresentableCharacter."""
    for cls in PresentableCharacter.__mro__:
        meta = vars(cls).get("__pydantic_generic_metadata__")
        if meta and meta.get("origin") is Blueprint:
            args: tuple[object, ...] = meta["args"]
            return args
    return ()


_BLUEPRINT_ARG_NAMES = [
    "race",
    "stats",
    "health",
    "stat choices remaining",
    "skill choices remaining",
    "wizard level",
    "sorcerer level",
    "fighter level",
    "barbarian level",
    "rogue level",
    "cleric level",
    "druid level",
    "paladin level",
    "ranger level",
    "monk level",
    "bard level",
    "warlock level",
    "artificer level",
    "character data",
]


def _validate_presentable(current_args: tuple[object, ...]) -> None:
    """Raise TypeError if current_args cannot satisfy PresentableCharacter's constraints."""
    required = _presentable_blueprint_args()
    if not required:
        return
    for i, (curr, req) in enumerate(zip(current_args, required)):
        if not _arg_compatible(curr, req):
            name = (
                _BLUEPRINT_ARG_NAMES[i]
                if i < len(_BLUEPRINT_ARG_NAMES)
                else f"arg[{i}]"
            )
            raise TypeError(
                f"Pipeline result is missing required field: {name!r}"
                f" (got {curr!r}, need {req!r})"
            )


def _validate_pipeline(
    initial: AnyBluprint,
    building_blocks: Iterable[AnyBuildingBlock],
) -> None:
    """Raise TypeError if building_blocks cannot be chained starting from initial,
    or if the final state does not satisfy PresentableCharacter's requirements."""
    initial_cls = type(initial)
    current_origin: type = _generic_origin(initial_cls)
    current_args: tuple[object, ...] = _generic_args(initial_cls)
    # Blueprint-level args tracked separately for presentable check
    bp_tracked: tuple[object, ...] = _to_blueprint_level(current_origin, current_args)

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

        # Expand current state to Blueprint level for arg comparison
        bp_input_args = _to_blueprint_level(input_origin, input_args)

        for j, (curr_arg, inp_arg) in enumerate(zip(bp_tracked, bp_input_args)):
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

        # Propagate pass-through TypeVars (same TypeVar object in both input and output)
        # so that concrete values from earlier blocks survive through blocks that don't
        # touch those positions. Fresh output-only TypeVars represent newly-set values
        # and are kept as TypeVars for bound-based compatibility checking later.
        bp_new_args = _to_blueprint_level(new_origin, new_args)
        if bp_new_args:
            class_bindings = _collect_class_bindings(type(block))
            bp_new_args = tuple(_substitute(a, class_bindings) for a in bp_new_args)
            pass_through_tvars = {
                a for a in bp_input_args if isinstance(a, typing.TypeVar)
            }
            bp_tracked = tuple(
                bp_tracked[j]
                if isinstance(a, typing.TypeVar)
                and a in pass_through_tvars
                and j < len(bp_tracked)
                else a
                for j, a in enumerate(bp_new_args)
            )

        current_origin = new_origin
        current_args = new_args

    _validate_presentable(bp_tracked)
