from typing import Literal

from pydantic import Field

from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.level_up.sorcerer.base import (
    SorcererSharedLevelBase,
)
from dnd.character.blueprint.building_blocks.metamagic_choice_resolver import (
    AnyMetamagicChoiceResolver,
)
from dnd.character.blueprint.building_blocks.metamagic_choice_resolver.random import (
    RandomMetamagicChoiceResolver,
)
from dnd.character.blueprint.sentinels import FirstSubclassPostLevel
from dnd.character.blueprint.states.sorcerer.base import _SBPT


class SorcererLevel3(
    SorcererSharedLevelBase[
        Literal[FirstSubclassPostLevel.SECOND],
        Literal[FirstSubclassPostLevel.THIRD],
    ]
):
    """Increments sorcerer to level 3."""

    type: Literal[BuildingBlockType.SORCERER_LEVEL_3] = (
        BuildingBlockType.SORCERER_LEVEL_3
    )
    metamagic_choice_resolver: AnyMetamagicChoiceResolver = Field(
        default_factory=RandomMetamagicChoiceResolver
    )

    def _update_blueprint(self, blueprint: _SBPT) -> _SBPT:
        r1 = blueprint.model_copy(
            update={
                "classes": blueprint.classes.model_copy(update={"sorcerer": 3}),
                "n_metamagic_choices": blueprint.n_metamagic_choices + 2,
            }
        )
        selected = self.metamagic_choice_resolver._select_metamagic(r1, 2)
        return r1.model_copy(
            update={
                "metamagic_options": r1.metamagic_options + selected,
                "n_metamagic_choices": 0,
            }
        )
