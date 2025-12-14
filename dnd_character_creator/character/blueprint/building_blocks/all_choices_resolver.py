from __future__ import annotations

from dnd_character_creator.character.blueprint.building_blocks import (
    CombinedBlock,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    SkillChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks import (
    StatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.equipment_chooser.base import (
    EquipmentChooser,
)
from dnd_character_creator.character.blueprint.building_blocks.feat_choice_resolver import (
    FeatChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.initial_data_filler.base_filler import (
    InitialDataFiller,
)
from dnd_character_creator.character.blueprint.building_blocks.language_choice_resolver import (
    LanguageChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.skill_proficiency_choice_resolver import (
    SkillProficiencyChoiceResolver,
)
from dnd_character_creator.character.blueprint.building_blocks.tool_proficiency_choice_resolver import (
    ToolProficiencyChoiceResolver,
)


class AllChoicesResolver(CombinedBlock):
    blocks: tuple[
        LanguageChoiceResolver,
        SkillProficiencyChoiceResolver,
        FeatChoiceResolver,
        ToolProficiencyChoiceResolver,
        StatChoiceResolver,
        SkillChoiceResolver,
        InitialDataFiller,
        EquipmentChooser,
    ]
