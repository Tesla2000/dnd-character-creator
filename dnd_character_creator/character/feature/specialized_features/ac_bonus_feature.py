from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd_character_creator.character.blueprint.blueprint import Blueprint

from dnd_character_creator.character.feature.feature import Feature


class ACBonusFeature(Feature):
    """A feature that provides a bonus to Armor Class.

    Examples:
        - Natural Armor features
        - Defense fighting style
        - Certain class features
    """

    ac_bonus: int

    def assign_to(self, blueprint: Blueprint) -> Blueprint:
        """Add AC bonus to character and record the feature."""
        return type(blueprint)(
            ac_bonus=blueprint.ac_bonus + self.ac_bonus,
            other_active_abilities=blueprint.other_active_abilities
            + (f"{self.name}: {self.description}",),
        )
