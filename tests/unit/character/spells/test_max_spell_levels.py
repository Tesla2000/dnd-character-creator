import pytest

from dnd.character.spells.max_spell_levels import SpellSlots

_ALL_ZERO = SpellSlots(0, 0, 0, 0, 0, 0, 0, 0, 0)
_ONE_EACH = SpellSlots(1, 1, 1, 1, 1, 1, 1, 1, 1)

_SPEND_METHODS: tuple[tuple[str, str], ...] = (
    ("spend_level_1_slot", "level_1"),
    ("spend_level_2_slot", "level_2"),
    ("spend_level_3_slot", "level_3"),
    ("spend_level_4_slot", "level_4"),
    ("spend_level_5_slot", "level_5"),
    ("spend_level_6_slot", "level_6"),
    ("spend_level_7_slot", "level_7"),
    ("spend_level_8_slot", "level_8"),
    ("spend_level_9_slot", "level_9"),
)


@pytest.mark.unit
class TestSpellSlotsSpend:
    @pytest.mark.parametrize("method_name,field_name", _SPEND_METHODS)
    def test_spend_slot_decrements_when_available(
        self, method_name: str, field_name: str
    ) -> None:
        result = getattr(_ONE_EACH, method_name)()
        assert getattr(result, field_name) == 0

    @pytest.mark.parametrize(
        "method_name", [method_name for method_name, _ in _SPEND_METHODS]
    )
    def test_spend_slot_raises_when_empty(self, method_name: str) -> None:
        with pytest.raises(ValueError):
            getattr(_ALL_ZERO, method_name)()


@pytest.mark.unit
class TestSpellSlotsMaxLevel:
    def test_max_level_returns_zero_when_no_slots_remain(self) -> None:
        assert _ALL_ZERO.max_level() == 0

    def test_max_level_returns_highest_nonzero_level(self) -> None:
        slots = SpellSlots(1, 0, 1, 0, 0, 0, 0, 0, 0)
        assert slots.max_level() == 3
