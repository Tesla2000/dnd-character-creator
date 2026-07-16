from enum import auto
from enum import StrEnum
from typing import ClassVar
from typing import NamedTuple

from dnd.character.spells.spell_slots import SpellLevel

from frozendict import frozendict
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import PositiveInt


class FirstLevelSpellSlots(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    first: PositiveInt


class SecondLevelSpellSlots(FirstLevelSpellSlots):
    second: PositiveInt


class ThirdLevelSpellSlots(SecondLevelSpellSlots):
    third: PositiveInt


class FourthLevelSpellSlots(ThirdLevelSpellSlots):
    fourth: PositiveInt


class FifthLevelSpellSlots(FourthLevelSpellSlots):
    fifth: PositiveInt


class SixthLevelSpellSlots(FifthLevelSpellSlots):
    sixth: PositiveInt


class SeventhLevelSpellSlots(SixthLevelSpellSlots):
    seventh: PositiveInt


class EighthLevelSpellSlots(SeventhLevelSpellSlots):
    eighth: PositiveInt


class NinthLevelSpellSlots(EighthLevelSpellSlots):
    ninth: PositiveInt


type AnySpellSlots = (
    FirstLevelSpellSlots
    | SecondLevelSpellSlots
    | ThirdLevelSpellSlots
    | FourthLevelSpellSlots
    | FifthLevelSpellSlots
    | SixthLevelSpellSlots
    | SeventhLevelSpellSlots
    | EighthLevelSpellSlots
    | NinthLevelSpellSlots
)


class FullCasterSpellSlots(NamedTuple):
    level_1: FirstLevelSpellSlots
    level_2: FirstLevelSpellSlots
    level_3: SecondLevelSpellSlots
    level_4: SecondLevelSpellSlots
    level_5: ThirdLevelSpellSlots
    level_6: ThirdLevelSpellSlots
    level_7: FourthLevelSpellSlots
    level_8: FourthLevelSpellSlots
    level_9: FifthLevelSpellSlots
    level_10: FifthLevelSpellSlots
    level_11: SixthLevelSpellSlots
    level_12: SixthLevelSpellSlots
    level_13: SeventhLevelSpellSlots
    level_14: SeventhLevelSpellSlots
    level_15: EighthLevelSpellSlots
    level_16: EighthLevelSpellSlots
    level_17: NinthLevelSpellSlots
    level_18: NinthLevelSpellSlots
    level_19: NinthLevelSpellSlots
    level_20: NinthLevelSpellSlots


FULL_CASTER_SPELL_SLOTS = FullCasterSpellSlots(
    level_1=FirstLevelSpellSlots(first=2),
    level_2=FirstLevelSpellSlots(first=3),
    level_3=SecondLevelSpellSlots(first=4, second=2),
    level_4=SecondLevelSpellSlots(first=4, second=3),
    level_5=ThirdLevelSpellSlots(first=4, second=3, third=2),
    level_6=ThirdLevelSpellSlots(first=4, second=3, third=3),
    level_7=FourthLevelSpellSlots(first=4, second=3, third=3, fourth=1),
    level_8=FourthLevelSpellSlots(first=4, second=3, third=3, fourth=2),
    level_9=FifthLevelSpellSlots(first=4, second=3, third=3, fourth=3, fifth=1),
    level_10=FifthLevelSpellSlots(first=4, second=3, third=3, fourth=3, fifth=2),
    level_11=SixthLevelSpellSlots(
        first=4, second=3, third=3, fourth=3, fifth=2, sixth=1
    ),
    level_12=SixthLevelSpellSlots(
        first=4, second=3, third=3, fourth=3, fifth=2, sixth=1
    ),
    level_13=SeventhLevelSpellSlots(
        first=4, second=3, third=3, fourth=3, fifth=2, sixth=1, seventh=1
    ),
    level_14=SeventhLevelSpellSlots(
        first=4, second=3, third=3, fourth=3, fifth=2, sixth=1, seventh=1
    ),
    level_15=EighthLevelSpellSlots(
        first=4, second=3, third=3, fourth=3, fifth=2, sixth=1, seventh=1, eighth=1
    ),
    level_16=EighthLevelSpellSlots(
        first=4, second=3, third=3, fourth=3, fifth=2, sixth=1, seventh=1, eighth=1
    ),
    level_17=NinthLevelSpellSlots(
        first=4,
        second=3,
        third=3,
        fourth=3,
        fifth=2,
        sixth=1,
        seventh=1,
        eighth=1,
        ninth=1,
    ),
    level_18=NinthLevelSpellSlots(
        first=4,
        second=3,
        third=3,
        fourth=3,
        fifth=3,
        sixth=1,
        seventh=1,
        eighth=1,
        ninth=1,
    ),
    level_19=NinthLevelSpellSlots(
        first=4,
        second=3,
        third=3,
        fourth=3,
        fifth=3,
        sixth=2,
        seventh=1,
        eighth=1,
        ninth=1,
    ),
    level_20=NinthLevelSpellSlots(
        first=4,
        second=3,
        third=3,
        fourth=3,
        fifth=3,
        sixth=2,
        seventh=2,
        eighth=1,
        ninth=1,
    ),
)


class MaxSpellLevelsByCharacterLevel(NamedTuple):
    level_1: SpellLevel
    level_2: SpellLevel
    level_3: SpellLevel
    level_4: SpellLevel
    level_5: SpellLevel
    level_6: SpellLevel
    level_7: SpellLevel
    level_8: SpellLevel
    level_9: SpellLevel
    level_10: SpellLevel
    level_11: SpellLevel
    level_12: SpellLevel
    level_13: SpellLevel
    level_14: SpellLevel
    level_15: SpellLevel
    level_16: SpellLevel
    level_17: SpellLevel
    level_18: SpellLevel
    level_19: SpellLevel
    level_20: SpellLevel


class CasterType(StrEnum):
    """Types of spellcasting progression."""

    FULL = auto()
    HALF = auto()
    ELDRITCH_KNIGHT = auto()
    WARLOCK = auto()
    NONE = auto()


MAX_SPELL_LEVELS: frozendict[CasterType, MaxSpellLevelsByCharacterLevel] = frozendict(
    {
        CasterType.FULL: MaxSpellLevelsByCharacterLevel(
            1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9
        ),
        CasterType.HALF: MaxSpellLevelsByCharacterLevel(
            0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5
        ),
        CasterType.WARLOCK: MaxSpellLevelsByCharacterLevel(
            1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5
        ),
        CasterType.ELDRITCH_KNIGHT: MaxSpellLevelsByCharacterLevel(
            0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4
        ),
        CasterType.NONE: MaxSpellLevelsByCharacterLevel(
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ),
    }
)
