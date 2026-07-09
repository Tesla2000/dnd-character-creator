import pytest
from dnd.server.example_generators.example_building_blocks import (
    example_building_blocks,
)


@pytest.fixture
def building_blocks():
    return example_building_blocks()
