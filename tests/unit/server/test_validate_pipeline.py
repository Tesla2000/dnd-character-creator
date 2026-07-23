import typing

import pytest
from pydantic import BaseModel

from dnd.character.blueprint.building_blocks.null_block import NullBlock
from dnd.character.blueprint.building_blocks.race_assigner.random_race_assigner import (
    RandomRaceAssigner,
)
from dnd.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd.character.blueprint.states.sorcerer.base import SorcererBlueprint
from dnd.character.blueprint.states.state import EmptyBlueprint
from dnd.character.race.race import Race
from dnd.choices.stats_creation.statistic import Statistic
from dnd.character.blueprint.states.state import Blueprint
from dnd.server._validate_pipeline import (
    _arg_compatible,
    _collect_class_bindings,
    _generic_args,
    _generic_origin,
    _substitute,
    _validate_pipeline,
)

_PRIORITY = (
    Statistic.STRENGTH,
    Statistic.DEXTERITY,
    Statistic.CONSTITUTION,
    Statistic.INTELLIGENCE,
    Statistic.WISDOM,
    Statistic.CHARISMA,
)
_INITIAL_PIPELINE = (
    StandardArray(stats_priority=_PRIORITY),
    RandomRaceAssigner(),
)


@pytest.mark.unit
class TestArgCompatible:
    def test_typevar_accepts_any_concrete_type(self) -> None:
        tv = typing.TypeVar("T")
        assert _arg_compatible(Race, tv) is True

    def test_typevar_accepts_none_type(self) -> None:
        tv = typing.TypeVar("T")
        assert _arg_compatible(type(None), tv) is True

    def test_same_concrete_type_is_compatible(self) -> None:
        assert _arg_compatible(Race, Race) is True

    def test_subclass_is_compatible_with_parent(self) -> None:
        class Parent:
            pass

        class Child(Parent):
            pass

        assert _arg_compatible(Child, Parent) is True

    def test_unrelated_types_are_incompatible(self) -> None:
        assert _arg_compatible(Race, int) is False

    def test_literal_equal_is_compatible(self) -> None:
        assert _arg_compatible(typing.Literal[0], typing.Literal[0]) is True

    def test_literal_subset_is_compatible(self) -> None:
        assert _arg_compatible(typing.Literal[0], typing.Literal[0, 1]) is True

    def test_literal_superset_is_incompatible(self) -> None:
        assert _arg_compatible(typing.Literal[0, 1], typing.Literal[0]) is False

    def test_none_matches_none_type(self) -> None:
        assert _arg_compatible(type(None), type(None)) is True


@pytest.mark.unit
class TestGenericHelpers:
    def test_generic_origin_of_empty_blueprint_is_blueprint(self) -> None:
        origin = _generic_origin(type(EmptyBlueprint()))
        assert issubclass(origin, Blueprint)

    def test_generic_args_of_empty_blueprint_has_20_params(self) -> None:
        args = _generic_args(type(EmptyBlueprint()))
        assert len(args) == 20


@pytest.mark.unit
class TestValidatePipeline:
    def test_empty_pipeline_raises_for_missing_fields(self) -> None:
        with pytest.raises(TypeError, match="race"):
            _validate_pipeline(EmptyBlueprint(), [])

    def test_null_block_raises_for_insufficient_pipeline(self) -> None:
        with pytest.raises(TypeError, match="race"):
            _validate_pipeline(EmptyBlueprint(), [NullBlock()])

    def test_null_block_after_initial_pipeline_raises_for_insufficient_pipeline(
        self,
    ) -> None:
        with pytest.raises(TypeError):
            _validate_pipeline(EmptyBlueprint(), [*_INITIAL_PIPELINE, NullBlock()])

    def test_multiple_null_blocks_raise_for_insufficient_pipeline(self) -> None:
        with pytest.raises(TypeError, match="race"):
            _validate_pipeline(
                EmptyBlueprint(), [NullBlock(), NullBlock(), NullBlock()]
            )

    def test_initial_pipeline_alone_raises_for_insufficient_pipeline(self) -> None:
        with pytest.raises(TypeError):
            _validate_pipeline(EmptyBlueprint(), list(_INITIAL_PIPELINE))

    def test_race_assigner_twice_raises_type_error(self) -> None:
        with pytest.raises(TypeError, match="RandomRaceAssigner"):
            _validate_pipeline(
                EmptyBlueprint(), [*_INITIAL_PIPELINE, RandomRaceAssigner()]
            )

    def test_type_error_includes_block_index(self) -> None:
        with pytest.raises(TypeError, match="Block 2"):
            _validate_pipeline(
                EmptyBlueprint(), [*_INITIAL_PIPELINE, RandomRaceAssigner()]
            )

    def test_pipeline_validates_iterable_not_just_list(self) -> None:
        with pytest.raises(TypeError, match="race"):
            _validate_pipeline(EmptyBlueprint(), iter([NullBlock()]))


@pytest.mark.unit
class TestArgCompatibleTypeVarBound:
    def test_current_typevar_without_bound_is_compatible(self) -> None:
        tv: typing.TypeVar = typing.TypeVar("T")
        assert _arg_compatible(tv, Race) is True

    def test_current_typevar_with_compatible_bound_recurses(self) -> None:
        tv: typing.TypeVar = typing.TypeVar("T", bound=int)
        assert _arg_compatible(tv, object) is True

    def test_current_typevar_with_incompatible_bound_recurses(self) -> None:
        tv: typing.TypeVar = typing.TypeVar("T", bound=int)
        assert _arg_compatible(tv, Race) is False


@pytest.mark.unit
class TestArgCompatibleTypeAlias:
    def test_type_alias_unwraps_to_matching_type(self) -> None:
        type _RaceAlias = Race

        assert _arg_compatible(_RaceAlias, Race) is True


@pytest.mark.unit
class TestArgCompatibleUnions:
    def test_current_union_all_members_compatible(self) -> None:
        assert _arg_compatible(int | str, object) is True

    def test_current_union_one_member_incompatible(self) -> None:
        assert _arg_compatible(int | str, str) is False

    def test_expected_union_any_member_compatible(self) -> None:
        assert _arg_compatible(int, int | str) is True

    def test_expected_union_no_member_compatible(self) -> None:
        assert _arg_compatible(list, int | str) is False


@pytest.mark.unit
class TestArgCompatibleLiteralZero:
    def test_int_subclass_current_matches_literal_zero(self) -> None:
        assert _arg_compatible(int, typing.Literal[0]) is True

    def test_annotated_int_current_matches_literal_zero(self) -> None:
        assert (
            _arg_compatible(typing.Annotated[int, "meta"], typing.Literal[0]) is True
        )

    def test_non_int_current_does_not_match_literal_zero(self) -> None:
        assert _arg_compatible(str, typing.Literal[0]) is False

    def test_current_not_matching_and_expected_not_zero_literal(self) -> None:
        assert _arg_compatible(str, typing.Literal[1, 2]) is False


@pytest.mark.unit
class TestArgCompatibleTypeVsLiteral:
    def test_expected_type_current_literal_all_instances(self) -> None:
        assert _arg_compatible(typing.Literal[1, 2], int) is True

    def test_expected_type_current_literal_not_all_instances(self) -> None:
        assert _arg_compatible(typing.Literal[1, "two"], int) is False


@pytest.mark.unit
class TestArgCompatibleGenericOrigins:
    def test_non_type_origin_falls_back_to_equality(self) -> None:
        assert _arg_compatible(typing.Literal[1, 2], list[int]) is False

    def test_unrelated_generic_origins_incompatible(self) -> None:
        assert _arg_compatible(list[int], dict[str, int]) is False

    def test_matching_generic_origin_with_compatible_args(self) -> None:
        assert _arg_compatible(list[int], list[object]) is True

    def test_matching_generic_origin_with_incompatible_arg(self) -> None:
        assert _arg_compatible(list[int], list[str]) is False


@pytest.mark.unit
class TestSubstitute:
    def test_substitutes_bound_typevar(self) -> None:
        tv: typing.TypeVar = typing.TypeVar("T")
        assert _substitute(tv, {tv: int}) is int

    def test_substitutes_typevar_inside_generic_container(self) -> None:
        tv: typing.TypeVar = typing.TypeVar("T")
        assert _substitute(list[tv], {tv: int}) == list[int]

    def test_leaves_unbound_arg_unchanged(self) -> None:
        assert _substitute(int, {}) is int


_HolderT = typing.TypeVar("_HolderT")


class _GenericHolder(BaseModel, typing.Generic[_HolderT]):
    value: int = 0


@pytest.mark.unit
class TestCollectClassBindings:
    def test_binds_typevar_to_concrete_arg(self) -> None:
        bindings = _collect_class_bindings(_GenericHolder[int])
        assert bindings == {_HolderT: int}


class _GenericBindingA(BaseModel, typing.Generic[_HolderT]):
    a: int = 0


class _GenericBindingB(BaseModel, typing.Generic[_HolderT]):
    b: int = 0


class _CombinedBindings(_GenericBindingA[int], _GenericBindingB[str]):
    pass


@pytest.mark.unit
class TestCollectClassBindingsSkipsAlreadyBound:
    def test_first_binding_wins_for_shared_typevar(self) -> None:
        bindings = _collect_class_bindings(_CombinedBindings)
        assert bindings == {_HolderT: int}


@pytest.mark.unit
class TestValidatePipelineBranches:
    def test_non_basemodel_input_hint_uses_type_directly(self) -> None:
        class _ObjectInputBlock:
            def apply(self, blueprint: object) -> EmptyBlueprint:
                return blueprint  # type: ignore[return-value]

        with pytest.raises(TypeError, match="race"):
            _validate_pipeline(EmptyBlueprint(), [_ObjectInputBlock()])

    def test_origin_mismatch_raises_type_error(self) -> None:
        class _RequiresSorcererBlock:
            def apply(self, blueprint: SorcererBlueprint) -> SorcererBlueprint:
                return blueprint  # type: ignore[return-value]

        with pytest.raises(TypeError, match="SorcererBlueprint"):
            _validate_pipeline(EmptyBlueprint(), [_RequiresSorcererBlock()])

    def test_return_typevar_is_skipped(self) -> None:
        _T: typing.TypeVar = typing.TypeVar("_T")

        class _PassThroughReturnBlock:
            def apply(self, blueprint: EmptyBlueprint) -> _T:  # type: ignore[valid-type]
                return blueprint  # type: ignore[return-value]

        with pytest.raises(TypeError, match="race"):
            _validate_pipeline(EmptyBlueprint(), [_PassThroughReturnBlock()])

    def test_return_hint_bare_blueprint_skips_arg_tracking(self) -> None:
        class _ReturnsBareBlueprintBlock:
            def apply(self, blueprint: EmptyBlueprint) -> Blueprint:  # type: ignore[type-arg]
                return blueprint  # type: ignore[return-value]

        with pytest.raises(TypeError, match="race"):
            _validate_pipeline(EmptyBlueprint(), [_ReturnsBareBlueprintBlock()])
