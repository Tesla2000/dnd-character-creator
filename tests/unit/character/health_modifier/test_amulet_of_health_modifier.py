import pytest

from dnd.character.health_modifier import AmuletOfHealthModifier
from dnd.character.health_modifier import HealthModifierType


@pytest.mark.unit
class TestAmuletOfHealthModifier:
    def test_type_value(self) -> None:
        assert AmuletOfHealthModifier().type == HealthModifierType.AMULET_OF_HEALTH

    def test_apply_boosts_low_constitution(self) -> None:
        class _Context:
            level = 5
            constitution_modifier = 2

        assert AmuletOfHealthModifier().apply(_Context()) == 10

    def test_apply_boosts_zero_constitution_modifier(self) -> None:
        class _Context:
            level = 5
            constitution_modifier = 0

        assert AmuletOfHealthModifier().apply(_Context()) == 20

    def test_apply_no_effect_when_constitution_already_high(self) -> None:
        class _Context:
            level = 7
            constitution_modifier = 4

        assert AmuletOfHealthModifier().apply(_Context()) == 0

    def test_apply_never_negative_above_amulet_constitution(self) -> None:
        class _Context:
            level = 7
            constitution_modifier = 5

        assert AmuletOfHealthModifier().apply(_Context()) == 0
