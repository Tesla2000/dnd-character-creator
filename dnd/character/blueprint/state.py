from __future__ import annotations

from typing import ClassVar, Any
from typing import Generic
from typing import Literal
from typing import TypeAlias
from typing import TypeVar
from typing import cast

from dnd.character.armor.names import ArmorName
from dnd.character.magical_item.item import MagicalItem
from dnd.character.character import Level
from dnd.character.feature.feats import FeatName
from dnd.character.race.subraces import SubraceName
from dnd.character.spells.spells import Spells
from dnd.character.stats import Stats
from dnd.choices.class_creation.character_class import AnySubclass
from dnd.choices.equipment_creation.weapons import WeaponName
from dnd.choices.language import Language
from dnd.choices.stats_creation.statistic import Statistic
from dnd.other_profficiencies import ArmorProficiency
from dnd.other_profficiencies import GamingSet
from dnd.other_profficiencies import MusicalInstrument
from dnd.other_profficiencies import ToolProficiency
from dnd.other_profficiencies import WeaponProficiency
from dnd.skill_proficiency import Skill
from dnd.character.class_levels import ClassLevels
from pydantic import Field
from pydantic import NonNegativeInt, BaseModel, ConfigDict
from pydantic import PositiveInt
from dnd.character.blueprint.sentinels import AnyClassLevel
from dnd.character.blueprint.sentinels import AnySorcererLevel
from dnd.character.blueprint.sentinels import AnyStatChoices
from dnd.character.blueprint.sentinels import AnyWizardLevel
from dnd.character.blueprint.sentinels import ClassPreSubclassLevel
from dnd.character.blueprint.sentinels import FirstSubclassPreLevel
from dnd.character.blueprint.sentinels import MaybeCharacterData
from dnd.character.blueprint.sentinels import MaybeHealth
from dnd.character.blueprint.sentinels import MaybeRace
from dnd.character.blueprint.sentinels import MaybeStats
from dnd.character.blueprint.sentinels import SecondSubclassPreLevel
from dnd.character.blueprint.sentinels import SorcererPreSubclassLevel
from dnd.character.blueprint.sentinels import ThirdSubclassPreLevel
from dnd.character.blueprint.sentinels import WizardPreSubclassLevel
from dnd.character.blueprint.sentinels import _ARK
from dnd.character.blueprint.sentinels import _BAK
from dnd.character.blueprint.sentinels import _BDK
from dnd.character.blueprint.sentinels import _CDK
from dnd.character.blueprint.sentinels import _CLK
from dnd.character.blueprint.sentinels import _DRK
from dnd.character.blueprint.sentinels import _FGK
from dnd.character.blueprint.sentinels import _HeK
from dnd.character.blueprint.sentinels import _MOK
from dnd.character.blueprint.sentinels import _PAK
from dnd.character.blueprint.sentinels import _RAK
from dnd.character.blueprint.sentinels import _RK
from dnd.character.blueprint.sentinels import _ROK
from dnd.character.blueprint.sentinels import _SOK
from dnd.character.blueprint.sentinels import _SkCK
from dnd.character.blueprint.sentinels import _StCK
from dnd.character.blueprint.sentinels import _StK
from dnd.character.blueprint.sentinels import _WAK
from dnd.character.blueprint.sentinels import _WZK

type Equipment = WeaponName | ArmorName | str


class Blueprint(
    BaseModel,
    Generic[
        _RK,
        _StK,
        _HeK,
        _StCK,
        _SkCK,
        _WZK,
        _SOK,
        _FGK,
        _BAK,
        _ROK,
        _CLK,
        _DRK,
        _PAK,
        _RAK,
        _MOK,
        _BDK,
        _WAK,
        _ARK,
        _CDK,
    ],
):
    """Flat character state. Type params encode what's been set:
    _RK=Race means race is set; _HeK=PositiveInt means health is set;
    _WZK=WizardSubclassLevel[...] means wizard subclass is assigned; etc.
    Building blocks transform Blueprint[InKey] -> Blueprint[OutKey].
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    race: _RK = Field(default=cast(_RK, None))
    subrace: SubraceName | None = None
    speed: PositiveInt | None = None
    dark_vision_range: NonNegativeInt | None = None
    stats: _StK = Field(default=cast(_StK, None))
    health_base: _HeK = Field(default=cast(_HeK, None))

    classes: ClassLevels = Field(default_factory=ClassLevels)
    stats_cup: Stats = Field(
        default=Stats(
            strength=20,
            dexterity=20,
            constitution=20,
            intelligence=20,
            wisdom=20,
            charisma=20,
        )
    )
    saving_throw_bonuses: Stats = Field(
        default=Stats(
            strength=0,
            dexterity=0,
            constitution=0,
            intelligence=0,
            wisdom=0,
            charisma=0,
        )
    )
    initiative_bonus: int = 0
    ac_bonus: NonNegativeInt = 0
    spell_save_dc_bonus: NonNegativeInt = 0
    spellcasting_ability_bonus: NonNegativeInt = 0
    feats: tuple[FeatName, ...] = Field(default=())
    subclasses: tuple[AnySubclass, ...] = ()
    armors: tuple[ArmorName, ...] = ()
    weapons: tuple[WeaponName, ...] = ()
    other_equipment: tuple[str, ...] = ()
    spells: Spells = Field(default_factory=Spells)
    languages: tuple[Language, ...] = Field(default=())
    skill_proficiencies: tuple[Skill, ...] = Field(default=())
    tool_proficiencies: tuple[ToolProficiency | GamingSet | MusicalInstrument, ...] = (
        Field(default=())
    )
    weapon_proficiencies: frozenset[WeaponProficiency] = frozenset()
    armor_proficiencies: frozenset[ArmorProficiency] = frozenset()
    magical_items: tuple[MagicalItem, ...] = ()
    saving_throw_proficiencies: tuple[Statistic, ...] = ()
    other_active_abilities: tuple[str, ...] = ()
    n_stat_choices: _StCK = Field(default=cast(_StCK, 0))
    n_skill_choices: _SkCK = Field(default=cast(_SkCK, 0))
    skills_to_choose_from: frozenset[Skill] = Field(default_factory=frozenset)
    equipment_choices: tuple[tuple[Equipment, ...], ...] = ()
    level: Level | None = None
    character_data: _CDK = Field(default=cast(_CDK, None))


_Z = Literal[SecondSubclassPreLevel.ZEROTH]
_SZ = Literal[FirstSubclassPreLevel.ZEROTH]
_TZ = Literal[ThirdSubclassPreLevel.ZEROTH]

EmptyBlueprint: TypeAlias = Blueprint[
    None,
    None,
    None,
    Literal[0],
    Literal[0],
    WizardPreSubclassLevel[_Z, None],
    SorcererPreSubclassLevel[_SZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    ClassPreSubclassLevel[_TZ, None],
    None,
]
type AnyBluprint = Blueprint[
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
    Any,
]
_BPT = TypeVar("_BPT", bound=AnyBluprint)
