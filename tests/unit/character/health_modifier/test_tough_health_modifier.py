import pytest

from dnd.character.health_modifier import HealthModifierType
from dnd.character.health_modifier import ToughHealthModifier


@pytest.mark.unit
class TestToughHealthModifier:
    def test_type_value(self) -> None:
        assert ToughHealthModifier().type == HealthModifierType.TOUGH

    def test_apply_returns_double_level(self) -> None:
        class _Context:
            level = 5

        assert ToughHealthModifier().apply(_Context()) == 10

    def test_apply_level_one(self) -> None:
        class _Context:
            level = 1

        assert ToughHealthModifier().apply(_Context()) == 2
