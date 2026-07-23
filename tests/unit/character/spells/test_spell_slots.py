import pytest

from dnd.character.spells import get_class_spells_set
from dnd.character.spells.spell_slots import ClassSpellLevel
from dnd.choices.class_creation.character_class import Class

_ALL_CLASS_SPELL_LEVELS: tuple[ClassSpellLevel, ...] = (
    *((Class.ARTIFICER, level) for level in range(0, 6)),
    *((Class.BARD, level) for level in range(0, 10)),
    *((Class.CLERIC, level) for level in range(0, 10)),
    *((Class.DRUID, level) for level in range(0, 10)),
    *((Class.PALADIN, level) for level in range(1, 6)),
    *((Class.RANGER, level) for level in range(1, 6)),
    *((Class.SORCERER, level) for level in range(0, 10)),
    *((Class.WARLOCK, level) for level in range(0, 10)),
    *((Class.WIZARD, level) for level in range(0, 10)),
)


@pytest.mark.unit
class TestGetClassSpellsSet:
    @pytest.mark.parametrize("query", _ALL_CLASS_SPELL_LEVELS)
    def test_returns_frozenset_for_every_class_and_level(
        self, query: ClassSpellLevel
    ) -> None:
        result = get_class_spells_set(query)
        assert isinstance(result, frozenset)
        assert len(result) > 0
