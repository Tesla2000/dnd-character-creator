from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks import \
    CombinedBlock
from dnd_character_creator.character.blueprint.building_blocks.level_up.level_up import \
    LevelUp


class LevelUpMultiple(CombinedBlock):
    blocks: tuple[LevelUp, ...]
