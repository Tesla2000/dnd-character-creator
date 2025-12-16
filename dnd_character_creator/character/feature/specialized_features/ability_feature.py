from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd_character_creator.character.blueprint.blueprint import Blueprint

from dnd_character_creator.character.feature.feature import Feature


class AbilityFeature(Feature):
    """A feature that adds a descriptive ability to the character.

    This is the simplest type of feature that just adds text to
    other_active_abilities. It's equivalent to the base Feature class
    but provides semantic clarity for features that represent abilities
    without mechanical modifiers.

    Examples:
        - Relentless Endurance
        - Trance
        - Fey Ancestry
    """

    def assign_to(self, blueprint: Blueprint) -> Blueprint:
        """Add this ability to the character's other_active_abilities."""
        return type(blueprint)(
            other_active_abilities=blueprint.other_active_abilities
            + (f"{self.name}: {self.description}",)
        )
