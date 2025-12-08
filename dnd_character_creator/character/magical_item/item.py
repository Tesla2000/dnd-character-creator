from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.magical_item.level import Level
from dnd_character_creator.character.magical_item.source import Source


class MagicalItem(BaseModel):
    name: str
    description: str
    level: Level
    source: Source
    attuned: bool

    def assign_to(self, blueprint: Blueprint) -> Blueprint:
        return type(blueprint)(magical_items=blueprint.magical_items + (self,))
