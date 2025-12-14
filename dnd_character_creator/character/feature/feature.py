from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from dnd_character_creator.character.blueprint.blueprint import Blueprint


class Feature(BaseModel):
    """Base class for character features that can be assigned to a blueprint.

    Features represent abilities, traits, or characteristics that a character
    can gain from their race, class, background, feats, or other sources.
    Each feature has a name and description, and can modify the character's
    blueprint when assigned.
    """

    name: str
    description: str

    def assign_to(self, blueprint: Blueprint) -> Blueprint:
        """Assign this feature to a blueprint.

        The base implementation adds the feature to other_active_abilities.
        Subclasses can override this to modify other blueprint fields.

        Args:
            blueprint: The character blueprint to modify

        Returns:
            A new blueprint with this feature applied
        """
        return type(blueprint)(
            other_active_abilities=blueprint.other_active_abilities
            + (f"{self.name}: {self.description}",)
        )
