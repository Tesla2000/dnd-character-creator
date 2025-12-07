from pydantic import BaseModel, NonNegativeInt, Field


class RaceStatistics(BaseModel):
    strength: NonNegativeInt
    dexterity: NonNegativeInt
    constitution: NonNegativeInt
    intelligence: NonNegativeInt
    wisdom: NonNegativeInt
    charisma: NonNegativeInt
    any_of_your_choice: NonNegativeInt = Field(
        description="Typically 'Ability Score Increase: n different ability "
        "scores of your choice increase [...]'"
    )
