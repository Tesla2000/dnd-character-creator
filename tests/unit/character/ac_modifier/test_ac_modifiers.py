import pytest

from dnd.character.ac_modifier import BarbarianUnarmoredDefenseAcModifier
from dnd.character.ac_modifier import FlatAcModifier
from dnd.character.ac_modifier._base import _AcModifierContext
from dnd.character.armor.names import SHIELD
from dnd.character.race.race import Race
from dnd.character.stats import Stats
from dnd.other_profficiencies import ArmorProficiency


class _StubContext:
    def __init__(
        self,
        strength: int = 10,
        dexterity: int = 10,
        constitution: int = 10,
        wisdom: int = 10,
        other_equipment: tuple[str, ...] = (),
        armor_proficiencies: frozenset[ArmorProficiency] = frozenset(),
    ) -> None:
        self.race: Race | None = None
        self.stats = Stats(
            strength=strength,
            dexterity=dexterity,
            constitution=constitution,
            intelligence=10,
            wisdom=wisdom,
            charisma=10,
        )
        self.other_equipment = other_equipment
        self.armor_proficiencies = armor_proficiencies


_StubContext.__annotations__["race"] = "Race | None"

# Satisfy the Protocol at type-check time
_context_check: _AcModifierContext = _StubContext()


@pytest.mark.unit
class TestBarbarianUnarmoredDefense:
    def test_no_shield_returns_ten_plus_dex_plus_con(self) -> None:
        modifier = BarbarianUnarmoredDefenseAcModifier()
        ctx = _StubContext(dexterity=14, constitution=16)
        assert modifier.apply(ctx) == 10 + 2 + 3

    def test_shield_with_proficiency_adds_two(self) -> None:
        modifier = BarbarianUnarmoredDefenseAcModifier()
        ctx = _StubContext(
            dexterity=14,
            constitution=16,
            other_equipment=(SHIELD,),
            armor_proficiencies=frozenset({ArmorProficiency.SHIELDS}),
        )
        assert modifier.apply(ctx) == 10 + 2 + 3 + 2

    def test_shield_without_proficiency_no_bonus(self) -> None:
        modifier = BarbarianUnarmoredDefenseAcModifier()
        ctx = _StubContext(
            dexterity=14,
            constitution=16,
            other_equipment=(SHIELD,),
            armor_proficiencies=frozenset(),
        )
        assert modifier.apply(ctx) == 10 + 2 + 3


@pytest.mark.unit
class TestFlatAcModifier:
    def test_apply_returns_amount(self) -> None:
        modifier = FlatAcModifier(amount=1)
        ctx = _StubContext()
        assert modifier.apply(ctx) == 1

    def test_apply_returns_zero_for_zero_amount(self) -> None:
        modifier = FlatAcModifier(amount=0)
        ctx = _StubContext()
        assert modifier.apply(ctx) == 0
