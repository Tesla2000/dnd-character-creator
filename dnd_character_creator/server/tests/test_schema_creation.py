from dnd_character_creator.character.blueprint.simplified_blocks import (
    SimplifiedBlocks,
)
from pydantic import TypeAdapter


def test_schema_creation():
    adapter = TypeAdapter(SimplifiedBlocks)
    adapter.json_schema()
