
from dnd_character_creator.character.spells.spell_slots import ThirdLevel, \
    Cantrip, FirstLevel, SecondLevel, FourthLevel, FifthLevel, SixthLevel, \
    SeventhLevel, EighthLevel, NinthLevel, Spell
from pydantic import BaseModel, Field


class Spells(BaseModel):
    cantrips: tuple[Cantrip, ...] = Field(default_factory=tuple)
    first_level_spells: tuple[FirstLevel, ...] = Field(default_factory=tuple)
    second_level_spells: tuple[SecondLevel, ...] = Field(default_factory=tuple)
    third_level_spells: tuple[ThirdLevel, ...] = Field(default_factory=tuple)
    fourth_level_spells: tuple[FourthLevel, ...] = Field(default_factory=tuple)
    fifth_level_spells: tuple[FifthLevel, ...] = Field(default_factory=tuple)
    sixth_level_spells: tuple[SixthLevel, ...] = Field(default_factory=tuple)
    seventh_level_spells: tuple[SeventhLevel, ...] = Field(default_factory=tuple)
    eighth_level_spells: tuple[EighthLevel, ...] = Field(default_factory=tuple)
    ninth_level_spells: tuple[NinthLevel, ...] = Field(default_factory=tuple)

    def get_spells_by_level(self) -> tuple[tuple[Spell, ...]]:
        return Spells.model_dump(self).values()