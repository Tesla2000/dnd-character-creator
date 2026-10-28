# from collections.abc import Callable
#
# import pytest
#
# from dnd.character.spells.max_spell_levels import SpellSlots
#
# _ALL_ZERO = SpellSlots(0, 0, 0, 0, 0, 0, 0, 0, 0)
# _ONE_EACH = SpellSlots(1, 1, 1, 1, 1, 1, 1, 1, 1)
#
# _SPEND_SLOT: tuple[
#     tuple[Callable[[SpellSlots], SpellSlots], Callable[[SpellSlots], int]], ...
# ] = (
#     (SpellSlots.spend_level_1_slot, lambda slots: slots.level_1),
#     (SpellSlots.spend_level_2_slot, lambda slots: slots.level_2),
#     (SpellSlots.spend_level_3_slot, lambda slots: slots.level_3),
#     (SpellSlots.spend_level_4_slot, lambda slots: slots.level_4),
#     (SpellSlots.spend_level_5_slot, lambda slots: slots.level_5),
#     (SpellSlots.spend_level_6_slot, lambda slots: slots.level_6),
#     (SpellSlots.spend_level_7_slot, lambda slots: slots.level_7),
#     (SpellSlots.spend_level_8_slot, lambda slots: slots.level_8),
#     (SpellSlots.spend_level_9_slot, lambda slots: slots.level_9),
# )
#
#
# @pytest.mark.unit
# class TestSpellSlotsSpend:
#     @pytest.mark.parametrize(("spend", "remaining"), _SPEND_SLOT)
#     def test_spend_slot_decrements_when_available(
#         self,
#         spend: Callable[[SpellSlots], SpellSlots],
#         remaining: Callable[[SpellSlots], int],
#     ) -> None:
#         assert remaining(spend(_ONE_EACH)) == 0
#
#     @pytest.mark.parametrize(("spend", "remaining"), _SPEND_SLOT)
#     def test_spend_slot_raises_when_empty(
#         self,
#         spend: Callable[[SpellSlots], SpellSlots],
#         remaining: Callable[[SpellSlots], int],
#     ) -> None:
#         with pytest.raises(ValueError):
#             spend(_ALL_ZERO)
#
#
# @pytest.mark.unit
# class TestSpellSlotsMaxLevel:
#     def test_max_level_returns_zero_when_no_slots_remain(self) -> None:
#         assert _ALL_ZERO.max_level() == 0
#
#     def test_max_level_returns_highest_nonzero_level(self) -> None:
#         slots = SpellSlots(1, 0, 1, 0, 0, 0, 0, 0, 0)
#         assert slots.max_level() == 3
