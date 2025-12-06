
from DND_character_creator.choices.spell_slots.spell_slots import ThirdLevel, \
    Cantrip, FirstLevel, SecondLevel, FourthLevel, FifthLevel, SixthLevel, \
    SeventhLevel, EighthLevel, NinthLevel, Spell
from pydantic import BaseModel, Field


class Spells(BaseModel):
    cantrips: list[Cantrip] = Field(default_factory=list)
    first_level_spells: list[FirstLevel] = Field(default_factory=list)
    second_level_spells: list[SecondLevel] = Field(default_factory=list)
    third_level_spells: list[ThirdLevel] = Field(default_factory=list)
    fourth_level_spells: list[FourthLevel] = Field(default_factory=list)
    fifth_level_spells: list[FifthLevel] = Field(default_factory=list)
    sixth_level_spells: list[SixthLevel] = Field(default_factory=list)
    seventh_level_spells: list[SeventhLevel] = Field(default_factory=list)
    eighth_level_spells: list[EighthLevel] = Field(default_factory=list)
    ninth_level_spells: list[NinthLevel] = Field(default_factory=list)

    @property
    def spells_by_level(self) -> list[list[Spell]]:
        return Spells.model_dump(self).values()