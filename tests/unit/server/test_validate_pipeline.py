import typing

import pytest

from dnd.character.blueprint.building_blocks.all_choices_resolver.base import (
    AllChoicesResolver,
)
from dnd.character.blueprint.building_blocks.equipment_chooser.random import (
    RandomEquipmentChooser,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver.random import (
    RandomFeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.initial_builder import InitialBuilder
from dnd.character.blueprint.building_blocks.language_choice_resolver.random import (
    RandomLanguageChoiceResolver,
)
from dnd.character.blueprint.building_blocks.null_block import NullBlock
from dnd.character.blueprint.building_blocks.race_assigner.random_race_assigner import (
    RandomRaceAssigner,
)
from dnd.character.blueprint.building_blocks.skill_choice_resolver.random import (
    RandomSkillChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stat_choice_resolver.priority import (
    PriorityStatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stats_builder.standard_array import (
    StandardArray,
)
from dnd.character.blueprint.building_blocks.tool_proficiency_choice_resolver.random import (
    RandomToolProficiencyChoiceResolver,
)
from dnd.character.blueprint.states.state import EmptyBlueprint
from dnd.character.race.race import Race
from dnd.choices.stats_creation.statistic import Statistic
from dnd.character.blueprint.states.state import Blueprint
from dnd.server._validate_pipeline import (
    _arg_compatible,
    _generic_args,
    _generic_origin,
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
_ACR = AllChoicesResolver(
    language_choice_resolver=RandomLanguageChoiceResolver(),
    skill_choice_resolver=RandomSkillChoiceResolver(),
    feat_choice_resolver=RandomFeatChoiceResolver(),
    tool_proficiency_choice_resolver=RandomToolProficiencyChoiceResolver(),
    stat_choice_resolver=PriorityStatChoiceResolver(priority=_PRIORITY),
    equipment_chooser=RandomEquipmentChooser(),
)
_INITIAL_BUILDER = InitialBuilder(
    stats_builder=StandardArray(stats_priority=_PRIORITY),
    race_assigner=RandomRaceAssigner(),
    all_choices_resolver=_ACR,
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

    def test_generic_args_of_empty_blueprint_has_19_params(self) -> None:
        args = _generic_args(type(EmptyBlueprint()))
        assert len(args) == 19


@pytest.mark.unit
class TestValidatePipeline:
    def test_empty_pipeline_is_valid(self) -> None:
        _validate_pipeline(EmptyBlueprint(), [])

    def test_null_block_passes_on_empty_blueprint(self) -> None:
        _validate_pipeline(EmptyBlueprint(), [NullBlock()])

    def test_null_block_passes_after_initial_builder(self) -> None:
        _validate_pipeline(EmptyBlueprint(), [_INITIAL_BUILDER, NullBlock()])

    def test_multiple_null_blocks_are_valid(self) -> None:
        _validate_pipeline(EmptyBlueprint(), [NullBlock(), NullBlock(), NullBlock()])

    def test_initial_builder_on_empty_blueprint_is_valid(self) -> None:
        _validate_pipeline(EmptyBlueprint(), [_INITIAL_BUILDER])

    def test_initial_builder_twice_raises_type_error(self) -> None:
        with pytest.raises(TypeError, match="InitialBuilder"):
            _validate_pipeline(EmptyBlueprint(), [_INITIAL_BUILDER, _INITIAL_BUILDER])

    def test_type_error_includes_block_index(self) -> None:
        with pytest.raises(TypeError, match="Block 1"):
            _validate_pipeline(EmptyBlueprint(), [_INITIAL_BUILDER, _INITIAL_BUILDER])

    def test_pipeline_validates_iterable_not_just_list(self) -> None:
        _validate_pipeline(EmptyBlueprint(), iter([NullBlock()]))
