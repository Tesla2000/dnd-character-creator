from __future__ import annotations

from dnd_character_creator.character.ability import Ability
from pydantic import BaseModel


class AbilitiesTemplate(BaseModel):
    abilities: list[Ability]
