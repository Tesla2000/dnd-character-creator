from __future__ import annotations

from collections.abc import Generator
from typing import Literal

from dnd.character.blueprint.building_blocks.all_choices_resolver.base_resolver import (
    AllChoicesResolverBase,
)
from dnd.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd.character.blueprint.building_blocks.equipment_chooser import (
    AnyEquipmentChooser,
)
from dnd.character.blueprint.building_blocks.feat_choice_resolver import (
    AnyFeatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.language_choice_resolver import (
    AnyLanguageChoiceResolver,
)
from dnd.character.blueprint.building_blocks.skill_choice_resolver import (
    AnySkillChoiceResolver,
)
from dnd.character.blueprint.building_blocks.stat_choice_resolver import (
    AnyStatChoiceResolver,
)
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.building_blocks.tool_proficiency_choice_resolver import (
    AnyToolProficiencyChoiceResolver,
)
from dnd.character.blueprint.state import BlueprintProtocol
from dnd.character.delta.delta import Delta


class AllChoicesResolver(AllChoicesResolverBase, BuildingBlock):
    """Resolves all character choices by chaining individual resolvers sequentially.

    Combines language, skill, feat, tool, stat, and equipment resolvers into a
    single pipeline that processes all character choices in order. Each resolver
    handles its specific choice type independently.

    Example:
        >>> resolver = AllChoicesResolver(
        ...     language_choice_resolver=RandomLanguageChoiceResolver(),
        ...     skill_choice_resolver=RandomSkillChoiceResolver(),
        ...     feat_choice_resolver=RandomFeatChoiceResolver(),
        ...     tool_proficiency_choice_resolver=RandomToolProficiencyChoiceResolver(),
        ...     stat_choice_resolver=PriorityStatChoiceResolver(priority=stats_priority),
        ...     equipment_chooser=RandomEquipmentChooser(),
        ... )
    """

    type: Literal[BuildingBlockType.ALL_CHOICES_RESOLVER] = (
        BuildingBlockType.ALL_CHOICES_RESOLVER
    )

    language_choice_resolver: AnyLanguageChoiceResolver
    skill_choice_resolver: AnySkillChoiceResolver
    feat_choice_resolver: AnyFeatChoiceResolver
    tool_proficiency_choice_resolver: AnyToolProficiencyChoiceResolver
    stat_choice_resolver: AnyStatChoiceResolver
    equipment_chooser: AnyEquipmentChooser

    def flatten(self) -> Generator[BuildingBlock]:
        for block in (
            self.language_choice_resolver,
            self.skill_choice_resolver,
            self.feat_choice_resolver,
            self.tool_proficiency_choice_resolver,
            self.stat_choice_resolver,
            self.equipment_chooser,
        ):
            yield from block.flatten()

    def get_change(
        self, state: BlueprintProtocol
    ) -> Generator[Delta, None, BlueprintProtocol]:
        current: BlueprintProtocol = state
        for block in self.flatten():
            current = yield from block.get_change(current)
        return current
