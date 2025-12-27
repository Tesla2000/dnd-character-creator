from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.base_resolver import (
    AllChoicesResolverBase,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser import (
    AnyEquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver import (
    AnyFeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.language_choice_resolver import (
    AnyLanguageChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.skill_choice_resolver import (
    AnySkillChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stat_choice_resolver import (
    AnyStatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.tool_proficiency_choice_resolver import (
    AnyToolProficiencyChoiceResolver,
)


class AllChoicesResolver(AllChoicesResolverBase, CombinedBlock):
    blocks: tuple[
        AnyLanguageChoiceResolver,
        AnySkillChoiceResolver,
        AnyFeatChoiceResolver,
        AnyToolProficiencyChoiceResolver,
        AnyStatChoiceResolver,
        AnyEquipmentChooser,
    ]
