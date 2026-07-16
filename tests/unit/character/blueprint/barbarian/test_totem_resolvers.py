import pytest

from dnd.character.blueprint.building_blocks.totem_choice_resolver.random import (
    RandomTotemChoiceResolver,
)
from dnd.choices.abilities.totem_animal import TotemAnimal


@pytest.mark.unit
def test_random_totem_resolver_returns_totem_animal() -> None:
    resolver = RandomTotemChoiceResolver()
    result = resolver.resolve()
    assert isinstance(result, TotemAnimal)


@pytest.mark.unit
def test_random_totem_resolver_seed_is_deterministic() -> None:
    resolver_a = RandomTotemChoiceResolver(seed=42)
    resolver_b = RandomTotemChoiceResolver(seed=42)
    assert resolver_a.resolve() == resolver_b.resolve()


@pytest.mark.unit
def test_random_totem_resolver_different_seeds_may_differ() -> None:
    results = {RandomTotemChoiceResolver(seed=i).resolve() for i in range(20)}
    assert len(results) > 1


@pytest.mark.unit
def test_random_totem_resolver_no_seed() -> None:
    resolver = RandomTotemChoiceResolver(seed=None)
    result = resolver.resolve()
    assert result in list(TotemAnimal)
