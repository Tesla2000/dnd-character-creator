from typing import Annotated
from typing import Union

from dnd.character.blueprint.building_blocks.level_up.spell_assignment.llm import (
    SorcererLLMSpellAssigner,
    WizardLLMSpellAssigner,
)
from dnd.character.blueprint.building_blocks.level_up.spell_assignment.random import (
    DruidRandomSpellAssigner,
    RangerRandomSpellAssigner,
    SorcererRandomSpellAssigner,
    WizardRandomSpellAssigner,
)
from pydantic import Field

AnyWizardSpellAssigner = Annotated[
    Union[WizardRandomSpellAssigner, WizardLLMSpellAssigner],
    Field(discriminator="type"),
]

AnySorcererSpellAssigner = Annotated[
    Union[SorcererRandomSpellAssigner, SorcererLLMSpellAssigner],
    Field(discriminator="type"),
]

AnyDruidSpellAssigner = DruidRandomSpellAssigner

AnyRangerSpellAssigner = RangerRandomSpellAssigner

AnySpellAssigner = Annotated[
    Union[
        WizardRandomSpellAssigner,
        SorcererRandomSpellAssigner,
        DruidRandomSpellAssigner,
        RangerRandomSpellAssigner,
        WizardLLMSpellAssigner,
        SorcererLLMSpellAssigner,
    ],
    Field(discriminator="type"),
]

__all__ = [
    "WizardRandomSpellAssigner",
    "SorcererRandomSpellAssigner",
    "DruidRandomSpellAssigner",
    "RangerRandomSpellAssigner",
    "WizardLLMSpellAssigner",
    "SorcererLLMSpellAssigner",
    "AnyWizardSpellAssigner",
    "AnySorcererSpellAssigner",
    "AnyDruidSpellAssigner",
    "AnyRangerSpellAssigner",
    "AnySpellAssigner",
]
