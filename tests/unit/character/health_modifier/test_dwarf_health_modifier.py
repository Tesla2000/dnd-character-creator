import pytest

from dnd.character.health_modifier import DwarfHealthModifier
from dnd.character.health_modifier import HealthModifierType


@pytest.mark.unit
class TestDwarfHealthModifier:
    def test_type_value(self) -> None:
        assert DwarfHealthModifier().type == HealthModifierType.DWARF

    def test_apply_returns_level(self) -> None:
        class _Context:
            level = 5

        assert DwarfHealthModifier().apply(_Context()) == 5

    def test_apply_level_one(self) -> None:
        class _Context:
            level = 1

        assert DwarfHealthModifier().apply(_Context()) == 1
