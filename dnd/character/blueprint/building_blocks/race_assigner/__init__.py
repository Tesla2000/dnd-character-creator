from typing import Annotated
from typing import Union

from dnd.character.blueprint.building_blocks.get_discriminator import (
    get_discriminator,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    AarakocraRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    AasimarRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    BugbearRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    CentaurRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    ChangelingRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    DragonbornRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    DwarfRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    ElfRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    FirbolgRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    GenasiAirRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    GenasiEarthRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    GenasiFireRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    GenasiWaterRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    GnomeRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    GoblinRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    GoliathRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    GrungRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    HalfElfRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    HalflingRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    HalfOrcRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    HobgoblinRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    HumanRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    KalashtarRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    KenkuRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    KoboldRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    LeoninRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    LizardfolkRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    MinotaurRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    OrcRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    SatyrRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    ShifterRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    TabaxiRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    TieflingRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    TortleRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    VerdanRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    WarforgedRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    RaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    YuanTiPurebloodRaceAssigner,
)
from dnd.character.blueprint.building_blocks.race_assigner.random_race_assigner import (
    RandomRaceAssigner,
)
from dnd.character.blueprint.state import HasStats
from pydantic import Tag

AnyRaceAssigner = Annotated[
    Union[
        Annotated[
            AarakocraRaceAssigner[HasStats], Tag(AarakocraRaceAssigner.get_block_type())
        ],
        Annotated[
            AasimarRaceAssigner[HasStats], Tag(AasimarRaceAssigner.get_block_type())
        ],
        Annotated[
            BugbearRaceAssigner[HasStats], Tag(BugbearRaceAssigner.get_block_type())
        ],
        Annotated[
            CentaurRaceAssigner[HasStats], Tag(CentaurRaceAssigner.get_block_type())
        ],
        Annotated[
            ChangelingRaceAssigner[HasStats],
            Tag(ChangelingRaceAssigner.get_block_type()),
        ],
        Annotated[
            DragonbornRaceAssigner[HasStats],
            Tag(DragonbornRaceAssigner.get_block_type()),
        ],
        Annotated[DwarfRaceAssigner[HasStats], Tag(DwarfRaceAssigner.get_block_type())],
        Annotated[ElfRaceAssigner[HasStats], Tag(ElfRaceAssigner.get_block_type())],
        Annotated[
            FirbolgRaceAssigner[HasStats], Tag(FirbolgRaceAssigner.get_block_type())
        ],
        Annotated[
            GenasiAirRaceAssigner[HasStats], Tag(GenasiAirRaceAssigner.get_block_type())
        ],
        Annotated[
            GenasiEarthRaceAssigner[HasStats],
            Tag(GenasiEarthRaceAssigner.get_block_type()),
        ],
        Annotated[
            GenasiFireRaceAssigner[HasStats],
            Tag(GenasiFireRaceAssigner.get_block_type()),
        ],
        Annotated[
            GenasiWaterRaceAssigner[HasStats],
            Tag(GenasiWaterRaceAssigner.get_block_type()),
        ],
        Annotated[GnomeRaceAssigner[HasStats], Tag(GnomeRaceAssigner.get_block_type())],
        Annotated[
            GoblinRaceAssigner[HasStats], Tag(GoblinRaceAssigner.get_block_type())
        ],
        Annotated[
            GoliathRaceAssigner[HasStats], Tag(GoliathRaceAssigner.get_block_type())
        ],
        Annotated[GrungRaceAssigner[HasStats], Tag(GrungRaceAssigner.get_block_type())],
        Annotated[
            HalfElfRaceAssigner[HasStats], Tag(HalfElfRaceAssigner.get_block_type())
        ],
        Annotated[
            HalflingRaceAssigner[HasStats], Tag(HalflingRaceAssigner.get_block_type())
        ],
        Annotated[
            HalfOrcRaceAssigner[HasStats], Tag(HalfOrcRaceAssigner.get_block_type())
        ],
        Annotated[
            HobgoblinRaceAssigner[HasStats], Tag(HobgoblinRaceAssigner.get_block_type())
        ],
        Annotated[HumanRaceAssigner[HasStats], Tag(HumanRaceAssigner.get_block_type())],
        Annotated[
            KalashtarRaceAssigner[HasStats], Tag(KalashtarRaceAssigner.get_block_type())
        ],
        Annotated[KenkuRaceAssigner[HasStats], Tag(KenkuRaceAssigner.get_block_type())],
        Annotated[
            KoboldRaceAssigner[HasStats], Tag(KoboldRaceAssigner.get_block_type())
        ],
        Annotated[
            LeoninRaceAssigner[HasStats], Tag(LeoninRaceAssigner.get_block_type())
        ],
        Annotated[
            LizardfolkRaceAssigner[HasStats],
            Tag(LizardfolkRaceAssigner.get_block_type()),
        ],
        Annotated[
            MinotaurRaceAssigner[HasStats], Tag(MinotaurRaceAssigner.get_block_type())
        ],
        Annotated[OrcRaceAssigner[HasStats], Tag(OrcRaceAssigner.get_block_type())],
        Annotated[SatyrRaceAssigner[HasStats], Tag(SatyrRaceAssigner.get_block_type())],
        Annotated[
            ShifterRaceAssigner[HasStats], Tag(ShifterRaceAssigner.get_block_type())
        ],
        Annotated[
            TabaxiRaceAssigner[HasStats], Tag(TabaxiRaceAssigner.get_block_type())
        ],
        Annotated[
            TieflingRaceAssigner[HasStats], Tag(TieflingRaceAssigner.get_block_type())
        ],
        Annotated[
            TortleRaceAssigner[HasStats], Tag(TortleRaceAssigner.get_block_type())
        ],
        Annotated[
            VerdanRaceAssigner[HasStats], Tag(VerdanRaceAssigner.get_block_type())
        ],
        Annotated[
            WarforgedRaceAssigner[HasStats], Tag(WarforgedRaceAssigner.get_block_type())
        ],
        Annotated[
            YuanTiPurebloodRaceAssigner[HasStats],
            Tag(YuanTiPurebloodRaceAssigner.get_block_type()),
        ],
        Annotated[
            RandomRaceAssigner[HasStats], Tag(RandomRaceAssigner.get_block_type())
        ],
        Annotated[RaceAssigner[HasStats], Tag(RaceAssigner.get_block_type())],
    ],
    get_discriminator(),
]

__all__ = [
    "AarakocraRaceAssigner",
    "AasimarRaceAssigner",
    "BugbearRaceAssigner",
    "CentaurRaceAssigner",
    "ChangelingRaceAssigner",
    "DragonbornRaceAssigner",
    "DwarfRaceAssigner",
    "ElfRaceAssigner",
    "FirbolgRaceAssigner",
    "GenasiAirRaceAssigner",
    "GenasiEarthRaceAssigner",
    "GenasiFireRaceAssigner",
    "GenasiWaterRaceAssigner",
    "GnomeRaceAssigner",
    "GoblinRaceAssigner",
    "GoliathRaceAssigner",
    "GrungRaceAssigner",
    "HalfElfRaceAssigner",
    "HalflingRaceAssigner",
    "HalfOrcRaceAssigner",
    "HobgoblinRaceAssigner",
    "HumanRaceAssigner",
    "KalashtarRaceAssigner",
    "KenkuRaceAssigner",
    "KoboldRaceAssigner",
    "LeoninRaceAssigner",
    "LizardfolkRaceAssigner",
    "MinotaurRaceAssigner",
    "OrcRaceAssigner",
    "SatyrRaceAssigner",
    "ShifterRaceAssigner",
    "TabaxiRaceAssigner",
    "TieflingRaceAssigner",
    "TortleRaceAssigner",
    "VerdanRaceAssigner",
    "WarforgedRaceAssigner",
    "YuanTiPurebloodRaceAssigner",
    "RandomRaceAssigner",
    "RaceAssigner",
    "AnyRaceAssigner",
]
