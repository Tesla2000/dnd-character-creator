from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks.all_choices_resolver.base_resolver import (
    AllChoicesResolverBase,
)
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser.base import (
    EquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver.base import (
    FeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.language_choice_resolver.base import (
    LanguageChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.skill_choice_resolver.base import (
    SkillChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.skill_proficiency_choice_resolver.base import (
    SkillProficiencyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.stat_choice_resolver.base import (
    StatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.tool_proficiency_choice_resolver.base import (
    ToolProficiencyChoiceResolver,
)


class AllChoicesResolver(AllChoicesResolverBase, CombinedBlock):
    blocks: tuple[
        LanguageChoiceResolver,
        SkillProficiencyChoiceResolver,
        FeatChoiceResolver,
        ToolProficiencyChoiceResolver,
        StatChoiceResolver,
        SkillChoiceResolver,
        EquipmentChooser,
    ]
