import pytest

from dnd.choices.abilities.action import (
    AndAction,
    AttackAction,
    BasicAction,
    OrAction,
    SavingThrowAction,
)
from dnd.choices.abilities.action_type import ActionType
from dnd.choices.stats_creation.statistic import Statistic


@pytest.mark.unit
class TestActionModels:
    def test_basic_action_fields(self) -> None:
        action = BasicAction(
            action_type=ActionType.ACTION, name="Dodge", description="Dodge attacks."
        )
        assert action.type == "basic"
        assert action.range_tails == 1
        assert action.radius_tails == 0

    def test_attack_action_fields(self) -> None:
        action = AttackAction(
            action_type=ActionType.ACTION,
            name="Claw",
            description="A claw attack.",
            n_dice=2,
            dice_size=6,
            attack_bonus=5,
            damage_bonus=4,
        )
        assert action.type == "attack"

    def test_saving_throw_action_fields(self) -> None:
        action = SavingThrowAction(
            action_type=ActionType.ACTION,
            name="Breath Weapon",
            description="A cone of fire.",
            n_dice=6,
            dice_size=6,
            dc=15,
            saving_throw_type=Statistic.DEXTERITY,
        )
        assert action.type == "saving_throw"

    def test_or_action_fields(self) -> None:
        leaf = BasicAction(
            action_type=ActionType.ACTION, name="Dodge", description="Dodge attacks."
        )
        action = OrAction(
            action_type=ActionType.ACTION,
            name="Choice",
            description="Pick one.",
            options=(leaf,),
        )
        assert action.type == "or"
        assert action.options == (leaf,)

    def test_and_action_fields(self) -> None:
        leaf = BasicAction(
            action_type=ActionType.ACTION, name="Dodge", description="Dodge attacks."
        )
        action = AndAction(
            action_type=ActionType.ACTION,
            name="Both",
            description="Do both.",
            options=(leaf,),
        )
        assert action.type == "and"
        assert action.options == (leaf,)


@pytest.mark.unit
class TestActionType:
    def test_all_action_types_are_distinct_strings(self) -> None:
        values = {member.value for member in ActionType}
        assert len(values) == len(list(ActionType))
