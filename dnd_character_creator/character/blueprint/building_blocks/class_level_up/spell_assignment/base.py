from __future__ import annotations

from abc import ABC

from dnd_character_creator.character.blueprint.building_blocks import \
    BuildingBlock
from dnd_character_creator.choices.class_creation.character_class import Class


class SpellAssigner(BuildingBlock, ABC):
    """Abstract base class for spell assignment strategies.

    Subclasses must implement _select_spells to determine which specific
    spells to assign from the available spell list.
    """

    class_: Class

