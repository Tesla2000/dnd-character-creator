from __future__ import annotations

from typing import Generator

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.feats import Feat


class FeatAdder(BuildingBlock):
    """Adds a feat to the character's feat list.

    Appends to existing feats, allowing incremental feat additions.
    Raises error if feat already exists.

    Example:
        >>> builder = Builder([
        ...     FeatAdder(feat=Feat.TOUGH),
        ...     FeatAdder(feat=Feat.ALERT),
        ...     FeatAdder(feat=Feat.LUCKY),
        ... ])  # Character will have all three feats
    """

    feat: Feat

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Add the feat to the existing feat tuple.

        Args:
            blueprint: The current blueprint state.

        Yields:
            Blueprint with the feat added.

        Raises:
            ValueError: If feat already exists.
        """
        existing_feats = blueprint.feats

        # Raise if feat already exists
        if self.feat in existing_feats:
            raise ValueError(
                f"Feat {self.feat} already exists in character feats"
            )

        new_feats = existing_feats + (self.feat,)
        yield Blueprint(feats=new_feats)