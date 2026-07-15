#!/usr/bin/env python3
"""
Generate block metadata JSON for the frontend.
Run from /workspace/frontend: python3 scripts/generate_blocks.py
"""

import enum
import json
import sys
import types as builtin_types
import typing
from pathlib import Path
from typing import get_args
from typing import get_origin
from typing import TypeAlias
from typing import TypedDict

from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.blueprint.states.state import EmptyBlueprint
from dnd.server._validate_pipeline import _presentable_blueprint_args
from pydantic import BaseModel
from pydantic.fields import FieldInfo

_Bindings: TypeAlias = dict[object, object]
_Config: TypeAlias = dict[str, object]


class _ItemSchema(TypedDict, total=False):
    type: str
    enum: list[str]


class _FieldSchema(TypedDict, total=False):
    type: str
    enum: list[str]
    description: str
    required: bool
    default: str | int | float | bool
    note: str
    items: _ItemSchema
    properties: dict[str, object]
    sub_block_types: list[object]


class _ArgSpec(TypedDict, total=False):
    kind: str
    name: str
    values: list[object]
    origin: str
    args: list[object]
    members: list[object]


class _BlueprintSig(TypedDict):
    origin: str
    args: list[object]


class _BlockBlueprintSig(TypedDict, total=False):
    input: _BlueprintSig | None
    output: _BlueprintSig | None


sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from dnd.character.blueprint.building_blocks import AnyBuildingBlock  # noqa: E402
from dnd.character.blueprint.building_blocks.building_block_type import (  # noqa: E402
    BuildingBlockType,
)


def _get_category(type_name: str) -> str:
    if type_name.startswith("AI_"):
        return "AI"
    if "SUBCLASS_ASSIGNER" in type_name:
        return "Subclass"
    if "RACE" in type_name:
        return "Race"
    if "LEVEL" in type_name or "HEALTH_INCREASE" in type_name:
        return "Leveling"
    if "SPELL" in type_name:
        return "Spells"
    if "FEAT" in type_name or "MAX_FIRST" in type_name or "MAX_IF_NOT" in type_name:
        return "Feats"
    if "SKILL" in type_name:
        return "Skills"
    if "STAT" in type_name or type_name == "STANDARD_ARRAY":
        return "Stats"
    if "LANGUAGE" in type_name:
        return "Languages"
    if "EQUIPMENT" in type_name or "WEAPON" in type_name or "MAGICAL_ITEM" in type_name:
        return "Equipment"
    if "TOOL_PROFICIENCY" in type_name:
        return "Tool Proficiencies"
    if (
        "NAME" in type_name
        or "AGE" in type_name
        or "SEX" in type_name
        or "ALIGNMENT" in type_name
        or "BACKGROUND" in type_name
    ):
        return "Identity"
    if "INITIAL" in type_name or "BUILDER" in type_name:
        return "Builders"
    if "ALL_CHOICES" in type_name:
        return "Choices"
    if "NULL" in type_name or "CONVERTER" in type_name:
        return "Utility"
    if "CHARACTER_DATA" in type_name:
        return "Identity"
    return "Other"


def _label(type_name: str) -> str:
    """Convert TYPE_NAME_LIKE_THIS to 'Type Name Like This'."""
    return type_name.replace("_", " ").title()


def _get_sub_block_types(
    ann: object, depth: int
) -> list[tuple[str, str, "type[BuildingBlock]"]] | None:
    """If ann is an Annotated/union of BuildingBlock subclasses, return [(type_value, label, cls), ...]."""
    if depth >= 2:
        return None

    # Unwrap Annotated
    if get_origin(ann) is typing.Annotated:
        inner_args = get_args(ann)
        if inner_args:
            ann = inner_args[0]

    origin = get_origin(ann)
    if origin is not typing.Union and not isinstance(ann, builtin_types.UnionType):
        return None

    members = [a for a in get_args(ann) if a is not type(None)]
    if not members:
        return None

    result: list[tuple[str, str, type[BuildingBlock]]] = []
    for member in members:
        if not (isinstance(member, type) and issubclass(member, BuildingBlock)):
            return None
        type_field = member.model_fields.get("type")
        if type_field is None:
            return None
        type_args = get_args(type_field.annotation)
        if not type_args or not isinstance(type_args[0], enum.Enum):
            return None
        enum_val = type_args[0]
        result.append((enum_val.value, _label(enum_val.name), member))

    return result


def _field_to_schema(field_name: str, field: FieldInfo, depth: int = 0) -> _FieldSchema:
    """Simplified field schema extraction without recursive Pydantic schema generation."""
    ann = field.annotation
    ann_str = str(ann)

    schema: _FieldSchema = {}

    if field.description:
        schema["description"] = field.description

    # Check for Literal type (enum-like)
    origin = get_origin(ann)
    if origin is not None:
        if origin is typing.Literal or str(origin) == "typing.Literal":
            args = get_args(ann)
            schema["type"] = "string"
            schema["enum"] = [
                str(a.value) if isinstance(a, enum.Enum) else str(a) for a in args
            ]
            return schema

    # Unwrap Optional (X | None or Union[X, None])
    if origin in (typing.Union,) or isinstance(ann, builtin_types.UnionType):
        inner_args = get_args(ann)
        non_none = [a for a in inner_args if a is not type(None)]
        if len(non_none) == 1:
            fake_field = FieldInfo(
                annotation=non_none[0], description=field.description
            )
            inner = _field_to_schema(field_name, fake_field, depth=depth)
            inner["required"] = False
            return inner
        # Multi-type union: check if it's a sub-block union
        sub_types = _get_sub_block_types(ann, depth)
        if sub_types is not None:
            sub_block_list: list[object] = [
                {
                    "type_value": tv,
                    "label": lbl,
                    "fields": _get_fields(cls, depth=depth + 1),
                }
                for tv, lbl, cls in sub_types
            ]
            schema["type"] = "sub_block"
            schema["sub_block_types"] = sub_block_list
            return schema
        # Fall through to complex
        schema["type"] = "object"
        schema["note"] = "complex nested type"
        return schema

    # Check for Annotated union of sub-blocks (e.g. AnyD6HealthIncrease)
    if get_origin(ann) is typing.Annotated:
        sub_types = _get_sub_block_types(ann, depth)
        if sub_types is not None:
            sub_block_list = [
                {
                    "type_value": tv,
                    "label": lbl,
                    "fields": _get_fields(cls, depth=depth + 1),
                }
                for tv, lbl, cls in sub_types
            ]
            schema["type"] = "sub_block"
            schema["sub_block_types"] = sub_block_list
            return schema

    # Common type mappings
    if ann is str or ann_str == "<class 'str'>":
        schema["type"] = "string"
    elif ann is int or ann_str == "<class 'int'>":
        schema["type"] = "integer"
    elif ann is float or ann_str == "<class 'float'>":
        schema["type"] = "number"
    elif ann is bool or ann_str == "<class 'bool'>":
        schema["type"] = "boolean"
    elif "Annotated" in ann_str and "int" in ann_str:
        schema["type"] = "integer"
        return schema
    else:
        # Try to detect enum types
        if isinstance(ann, type) and issubclass(ann, enum.Enum):
            schema["type"] = "string"
            schema["enum"] = [e.value for e in ann]
            return schema

        # Tuple of enum (e.g. stats_priority: tuple[Statistic, ...])
        if origin in (tuple, list) or str(origin) in (
            "<class 'tuple'>",
            "<class 'list'>",
        ):
            item_args = get_args(ann)
            if item_args:
                item_type = item_args[0]
                if isinstance(item_type, type) and issubclass(item_type, enum.Enum):
                    schema["type"] = "array"
                    schema["items"] = {
                        "type": "string",
                        "enum": [e.value for e in item_type],
                    }
                    return schema
            schema["type"] = "array"
            return schema

        # Expand Pydantic data models up to 3 levels deep
        if depth < 3 and isinstance(ann, type) and issubclass(ann, BaseModel):
            return {
                "type": "nested_model",
                "properties": _get_fields(ann, depth=depth + 1),
            }

        # Union / complex nested types
        if "Union" in ann_str or "Optional" in ann_str or "|" in ann_str:
            schema["type"] = "object"
            schema["note"] = "complex nested type"
        else:
            schema["type"] = "string"
            schema["note"] = f"serialized as: {ann_str[:80]}"

    if field.default is not None and str(field.default) != "PydanticUndefined":
        try:
            json.dumps(field.default)
            schema["default"] = field.default
        except (TypeError, ValueError):
            schema["default"] = str(field.default)

    return schema


def _get_fields(cls: type[BaseModel], depth: int = 0) -> dict[str, _FieldSchema]:
    """Get fields for a block class, excluding 'type' and excluded fields."""
    fields: dict[str, _FieldSchema] = {}

    for name, field in cls.model_fields.items():
        if name == "type":
            continue
        if field.exclude:
            continue
        try:
            schema = _field_to_schema(name, field, depth=depth)
            required = (
                str(field.default) == "PydanticUndefined"
                and field.default_factory is None
            )
            schema["required"] = required
            # Skip single-value Literal fields with a default — no user choice available
            enum_vals = schema.get("enum")
            if not required and enum_vals is not None and len(enum_vals) == 1:
                continue
            fields[name] = schema
        except Exception as e:
            fields[name] = {
                "type": "string",
                "note": f"parse error: {e}",
                "required": True,
            }

    return fields


def _compute_default_config(
    cls: type[BaseModel], fields: dict[str, _FieldSchema]
) -> _Config:
    """Compute initial config defaults for a block from its field schemas."""
    defaults: _Config = {}
    for name, schema in fields.items():
        field = cls.model_fields.get(name)

        # Sub-block: instantiate default_factory or use first sub_block_type
        if schema.get("type") == "sub_block":
            sub_types = schema.get("sub_block_types", [])
            if field is not None and field.default_factory is not None:
                factory = typing.cast(
                    typing.Callable[[], object], field.default_factory
                )
                try:
                    instance = factory()
                    if isinstance(instance, BaseModel):
                        defaults[name] = instance.model_dump(mode="json")
                        continue
                except Exception:
                    pass
            if sub_types:
                first = sub_types[0]
                if isinstance(first, dict):
                    defaults[name] = {"type": first.get("type_value", "")}
            continue

        # Enum: first value
        if schema.get("enum"):
            enum_vals = schema["enum"]
            if enum_vals:
                defaults[name] = enum_vals[0]
            continue

        # Array with enum items: all values in order
        items = schema.get("items")
        if (
            schema.get("type") == "array"
            and isinstance(items, dict)
            and items.get("enum")
        ):
            defaults[name] = list(items["enum"])
            continue

        # Scalar default from schema
        if schema.get("default") is not None:
            defaults[name] = schema["default"]

    return defaults


def _serialize_arg(arg: object) -> _ArgSpec:
    """Serialize one Blueprint type-parameter to a JSON-safe ArgSpec."""
    if isinstance(arg, typing.TypeVar):
        return {"kind": "free"}
    if arg is None or arg is type(None):
        return {"kind": "none"}
    # Unwrap TypeAliasType (PEP 695 `type X = ...`) to its underlying value
    if isinstance(arg, typing.TypeAliasType):
        return _serialize_arg(arg.__value__)
    origin = get_origin(arg)
    if origin is typing.Literal:
        raw = get_args(arg)
        vals: list[object] = [v.value if isinstance(v, enum.Enum) else v for v in raw]
        return {"kind": "literal", "values": vals}
    # Handle Union types (both typing.Union and Python 3.10+ X|Y syntax)
    if origin is typing.Union or isinstance(arg, builtin_types.UnionType):
        members = get_args(arg)
        return {"kind": "union", "members": [_serialize_arg(m) for m in members]}
    # Unwrap Annotated[X, ...] to just X
    if origin is typing.Annotated:
        inner_args = get_args(arg)
        return (
            _serialize_arg(inner_args[0])
            if inner_args
            else {"kind": "type", "name": "unknown"}
        )
    if origin is not None and isinstance(origin, type):
        return {
            "kind": "generic",
            "origin": origin.__name__,
            "args": [_serialize_arg(a) for a in get_args(arg)],
        }
    if isinstance(arg, type):
        return {"kind": "type", "name": arg.__name__}
    return {"kind": "type", "name": str(arg)}


def _collect_typevar_bindings(cls: type) -> _Bindings:
    """Collect TypeVar bindings from concrete parameterized base classes in the MRO."""
    bindings: _Bindings = {}
    for mro_cls in cls.__mro__[1:]:
        pmeta = vars(mro_cls).get("__pydantic_generic_metadata__")
        if pmeta is None:
            continue
        origin = pmeta.get("origin")
        args = pmeta.get("args", ())
        if origin is None or not args:
            continue
        origin_pmeta = vars(origin).get("__pydantic_generic_metadata__")
        if origin_pmeta is None:
            continue
        for tv, arg in zip(origin_pmeta.get("parameters", ()), args):
            if tv not in bindings:
                bindings[tv] = arg
    return bindings


def _substitute(arg: object, bindings: _Bindings) -> object:
    """Recursively replace TypeVars with concrete values (handles both old-style and PEP 695)."""
    if arg in bindings:
        return _substitute(bindings[arg], bindings)
    origin = get_origin(arg)
    if origin is not None:
        args = get_args(arg)
        new_args = tuple(_substitute(a, bindings) for a in args)
        if new_args != args:
            return origin[new_args] if len(new_args) > 1 else origin[new_args[0]]
    return arg


def _expand_to_blueprint_args(
    cls: type,
    cls_args: tuple[object, ...],
    outer_bindings: _Bindings,
) -> list[_ArgSpec]:
    """Expand a Blueprint subtype into the full 19 Blueprint type args."""
    cls_pmeta = vars(cls).get("__pydantic_generic_metadata__", {})
    type_params = cls_pmeta.get("parameters", ())
    local: _Bindings = {tv: a for tv, a in zip(type_params, cls_args)}
    combined: _Bindings = {**outer_bindings, **local}

    for base in vars(cls).get("__orig_bases__", []):
        base_pmeta = vars(base).get("__pydantic_generic_metadata__")
        if base_pmeta is None:
            continue
        base_origin = base_pmeta.get("origin")
        base_args = base_pmeta.get("args", ())
        if base_origin is Blueprint:
            return [_serialize_arg(_substitute(a, combined)) for a in base_args]
        if (
            base_origin is not None
            and isinstance(base_origin, type)
            and issubclass(base_origin, Blueprint)
        ):
            substituted_base_args = tuple(_substitute(a, combined) for a in base_args)
            return _expand_to_blueprint_args(
                base_origin, substituted_base_args, combined
            )
        # Unparameterized Blueprint subtype (e.g. WizardLevel18Blueprint inside WizardLevel20Blueprint):
        # recurse with empty cls_args — combined already carries all TypeVar bindings.
        if (
            base_origin is None
            and isinstance(base, type)
            and base is not Blueprint
            and issubclass(base, Blueprint)
        ):
            result = _expand_to_blueprint_args(base, (), combined)
            if result:
                return result
    return []


def _sig_from_hint(
    hint: object, bindings: _Bindings | None = None
) -> _BlueprintSig | None:
    """Return {origin, args} for a Blueprint (sub)class hint, or None if it is a free TypeVar."""
    bindings = bindings or {}
    if isinstance(hint, typing.TypeVar):
        return None
    try:
        hint_vars = vars(hint)
    except TypeError:
        return None
    meta = hint_vars.get("__pydantic_generic_metadata__")
    if meta is not None:
        raw_origin = meta.get("origin") or hint
        if not isinstance(raw_origin, type):
            return None
        args = tuple(_substitute(a, bindings) for a in meta.get("args", ()))
        if raw_origin is not Blueprint and issubclass(raw_origin, Blueprint):
            expanded: list[object] = list(
                _expand_to_blueprint_args(raw_origin, args, bindings)
            )
            return {"origin": raw_origin.__name__, "args": expanded}
        return {
            "origin": raw_origin.__name__,
            "args": [_serialize_arg(a) for a in args],
        }
    if isinstance(hint, type):
        return {"origin": hint.__name__, "args": []}
    return None


def _get_blueprint_sig(cls: type[BuildingBlock]) -> _BlockBlueprintSig | None:
    """Extract serialized input/output Blueprint signatures from cls.apply()."""
    apply_fn = next(
        (c.__dict__["apply"] for c in cls.__mro__ if "apply" in c.__dict__),
        None,
    )
    if apply_fn is None:
        return None
    try:
        hints = typing.get_type_hints(apply_fn)
    except Exception:
        return None
    bindings = _collect_typevar_bindings(cls)
    input_sig = _sig_from_hint(hints.get("blueprint"), bindings)
    output_sig = _sig_from_hint(hints.get("return"), bindings)
    if input_sig is None and output_sig is None:
        return None
    return {"input": input_sig, "output": output_sig}


def main() -> None:
    args = get_args(AnyBuildingBlock)
    union_args = get_args(args[0])

    type_to_class: dict[str, type[BuildingBlock]] = {}
    for cls in union_args:
        for fname, finfo in cls.model_fields.items():
            if fname == "type":
                ann = finfo.annotation
                type_args = get_args(ann)
                if type_args:
                    enum_val = type_args[0]
                    if isinstance(enum_val, enum.Enum):
                        type_to_class[enum_val.name] = cls
                break

    blocks = []
    origin_classes: dict[str, type] = {}
    for bt in BuildingBlockType:
        cls = type_to_class.get(bt.name)
        if cls is None:
            continue

        is_ai = bt.name.startswith("AI_") or "LLM" in bt.name
        blueprint_sig = _get_blueprint_sig(cls)
        fields = _get_fields(cls)
        default_config = _compute_default_config(cls, fields)

        block: dict[str, object] = {
            "type": bt.value,
            "type_name": bt.name,
            "label": _label(bt.name),
            "class_name": cls.__name__,
            "category": _get_category(bt.name),
            "description": (cls.__doc__ or "").strip().split("\n")[0],
            "is_ai": is_ai,
            "fields": fields,
            "default_config": default_config,
            "blueprint_sig": blueprint_sig,
        }
        blocks.append(block)

        # Collect origin classes for hierarchy
        if blueprint_sig is not None:
            apply_fn = next(
                (c.__dict__["apply"] for c in cls.__mro__ if "apply" in c.__dict__),
                None,
            )
            try:
                hints = typing.get_type_hints(apply_fn) if apply_fn is not None else {}
            except Exception:
                hints = {}
            for key in ("blueprint", "return"):
                hint = hints.get(key)
                if hint is None or isinstance(hint, typing.TypeVar):
                    continue
                if isinstance(hint, type):
                    meta = vars(hint).get("__pydantic_generic_metadata__")
                    if meta is not None:
                        orig = meta.get("origin")
                        if isinstance(orig, type):
                            origin_classes[orig.__name__] = orig
                    elif isinstance(hint, type):
                        origin_classes[hint.__name__] = hint

    # Build origin hierarchy for Blueprint subclasses
    def _is_unsubscripted(cls: type) -> bool:
        meta = vars(cls).get("__pydantic_generic_metadata__")
        return meta is None or meta.get("origin") is None

    origin_hierarchy: dict[str, list[str]] = {}
    for name, orig_cls in origin_classes.items():
        if (
            isinstance(orig_cls, type)
            and issubclass(orig_cls, Blueprint)
            and orig_cls is not Blueprint
        ):
            parents = [
                c.__name__
                for c in orig_cls.__mro__[1:]
                if isinstance(c, type)
                and issubclass(c, Blueprint)
                and c is not orig_cls
                and _is_unsubscripted(c)
            ]
            if parents:
                origin_hierarchy[name] = parents

    # Serialize EmptyBlueprint initial state
    empty_meta = vars(EmptyBlueprint).get("__pydantic_generic_metadata__", {})
    empty_blueprint_args = [_serialize_arg(a) for a in empty_meta.get("args", ())]

    # Serialize PresentableCharacter's required Blueprint args
    presentable_blueprint_args = [
        _serialize_arg(a) for a in _presentable_blueprint_args()
    ]

    output = Path(__file__).parent.parent / "src" / "data" / "blocks-generated.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(blocks, indent=2))
    sys.stdout.write(f"Generated {len(blocks)} blocks -> {output}\n")

    meta_output = Path(__file__).parent.parent / "src" / "data" / "pipeline-meta.json"
    meta_output.write_text(
        json.dumps(
            {
                "emptyBlueprintArgs": empty_blueprint_args,
                "originHierarchy": origin_hierarchy,
                "presentableBlueprintArgs": presentable_blueprint_args,
            },
            indent=2,
        )
    )
    sys.stdout.write(f"Generated pipeline-meta -> {meta_output}\n")


if __name__ == "__main__":
    main()
