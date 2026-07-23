import pytest

from dnd.character._spell_modifier_context import SpellModifierContext
from dnd.character.spell_attack_bonus_modifier import FlatSpellAttackBonus
from dnd.character.spell_attack_bonus_modifier import ProficiencyBonus
from dnd.character.spell_attack_bonus_modifier import SpellcastingAbility
from dnd.character.stats import Stats
from dnd.choices.stats_creation.statistic import Statistic


class _StubContext:
    def __init__(self, stats: Stats, proficiency_bonus: int = 2) -> None:
        self.stats = stats
        self.proficiency_bonus = proficiency_bonus


_context_check: SpellModifierContext = _StubContext(
    Stats(
        strength=10,
        dexterity=10,
        constitution=10,
        intelligence=10,
        wisdom=10,
        charisma=10,
    )
)

_STATS = Stats(
    strength=12,
    dexterity=14,
    constitution=16,
    intelligence=18,
    wisdom=20,
    charisma=8,
)

_STATISTIC_TO_EXPECTED_MODIFIER: tuple[tuple[Statistic, int], ...] = (
    (Statistic.STRENGTH, 12 // 2 - 5),
    (Statistic.DEXTERITY, 14 // 2 - 5),
    (Statistic.CONSTITUTION, 16 // 2 - 5),
    (Statistic.INTELLIGENCE, 18 // 2 - 5),
    (Statistic.WISDOM, 20 // 2 - 5),
    (Statistic.CHARISMA, 8 // 2 - 5),
)


@pytest.mark.unit
class TestFlatSpellAttackBonus:
    def test_apply_returns_bonus(self) -> None:
        modifier = FlatSpellAttackBonus(bonus=3)
        ctx = _StubContext(_STATS)
        assert modifier.apply(ctx) == 3


@pytest.mark.unit
class TestProficiencyBonus:
    def test_apply_returns_context_proficiency_bonus(self) -> None:
        modifier = ProficiencyBonus()
        ctx = _StubContext(_STATS, proficiency_bonus=5)
        assert modifier.apply(ctx) == 5


@pytest.mark.unit
class TestSpellcastingAbility:
    @pytest.mark.parametrize("statistic,expected", _STATISTIC_TO_EXPECTED_MODIFIER)
    def test_apply_returns_ability_modifier(
        self, statistic: Statistic, expected: int
    ) -> None:
        modifier = SpellcastingAbility(statistic=statistic)
        ctx = _StubContext(_STATS)
        assert modifier.apply(ctx) == expected

    def test_apply_raises_for_unrecognized_statistic(self) -> None:
        modifier = SpellcastingAbility.model_construct(statistic="invalid")
        ctx = _StubContext(_STATS)
        with pytest.raises(AssertionError):
            modifier.apply(ctx)
