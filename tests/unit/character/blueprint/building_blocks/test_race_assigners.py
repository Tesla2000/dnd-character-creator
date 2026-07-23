import pytest
from pydantic import ValidationError

from dnd.character.blueprint.building_blocks.race_assigner.base_race_assigner import (
    RaceSubracePair,
)
from dnd.character.blueprint.building_blocks.race_assigner.race_assigner import (
    AarakocraRaceAssigner,
    AasimarRaceAssigner,
    BugbearRaceAssigner,
    CentaurRaceAssigner,
    ChangelingRaceAssigner,
    DragonbornRaceAssigner,
    DwarfRaceAssigner,
    ElfRaceAssigner,
    FirbolgRaceAssigner,
    GenasiAirRaceAssigner,
    GenasiEarthRaceAssigner,
    GenasiFireRaceAssigner,
    GenasiWaterRaceAssigner,
    GnomeRaceAssigner,
    GoblinRaceAssigner,
    GoliathRaceAssigner,
    GrungRaceAssigner,
    HalfElfRaceAssigner,
    HalfOrcRaceAssigner,
    HalflingRaceAssigner,
    HobgoblinRaceAssigner,
    HumanRaceAssigner,
    KalashtarRaceAssigner,
    KenkuRaceAssigner,
    KoboldRaceAssigner,
    LeoninRaceAssigner,
    LizardfolkRaceAssigner,
    MinotaurRaceAssigner,
    OrcRaceAssigner,
    RaceAssigner,
    SatyrRaceAssigner,
    ShifterRaceAssigner,
    TabaxiRaceAssigner,
    TieflingRaceAssigner,
    TortleRaceAssigner,
    VerdanRaceAssigner,
    WarforgedRaceAssigner,
    YuanTiPurebloodRaceAssigner,
)
from dnd.character.blueprint.states.state import Blueprint
from dnd.character.health_modifier import DwarfHealthModifier
from dnd.character.race.race import Race
from dnd.character.race.subraces import SubraceName
from dnd.character.stats import Stats


@pytest.mark.unit
@pytest.mark.parametrize(
    "assigner_cls, subrace, expected_race",
    [
        (
            HumanRaceAssigner,
            SubraceName.HUMAN_STANDARD_HUMAN_PLAYERSHANDBOOK,
            Race.HUMAN,
        ),
        (ElfRaceAssigner, SubraceName.ELF_HIGH_ELF_PLAYERSHANDBOOK, Race.ELF),
        (DwarfRaceAssigner, SubraceName.DWARF_HILL_DWARF_PLAYERSHANDBOOK, Race.DWARF),
        (
            HalflingRaceAssigner,
            SubraceName.HALFLING_LIGHTFOOT_PLAYERSHANDBOOK,
            Race.HALFLING,
        ),
        (
            HalfElfRaceAssigner,
            SubraceName.HALF_ELF_HIGH_ELF_HERITAGE_PLAYERSHANDBOOK,
            Race.HALF_ELF,
        ),
        (
            HalfOrcRaceAssigner,
            SubraceName.HALF_ORC_HALF_ORC_PLAYERSHANDBOOK,
            Race.HALF_ORC,
        ),
        (
            TieflingRaceAssigner,
            SubraceName.TIEFLING_BLOODLINE_OF_ASMODEUS_PLAYERSHANDBOOK,
            Race.TIEFLING,
        ),
        (
            DragonbornRaceAssigner,
            SubraceName.DRAGONBORN_DRAGONBORN_PLAYERSHANDBOOK,
            Race.DRAGONBORN,
        ),
        (GnomeRaceAssigner, SubraceName.GNOME_ROCK_GNOME_PLAYERSHANDBOOK, Race.GNOME),
        (
            AasimarRaceAssigner,
            SubraceName.AASIMAR_FALLEN_AASIMAR_VOLOSGUIDETOMONSTERS,
            Race.AASIMAR,
        ),
        (
            GenasiAirRaceAssigner,
            SubraceName.GENASI_AIR_AIR_GENASI_ELEMENTALEVILPLAYERSCOMPANION,
            Race.GENASI_AIR,
        ),
        (
            GenasiWaterRaceAssigner,
            SubraceName.GENASI_WATER_WATER_GENASI_ELEMENTALEVILPLAYERSCOMPANION,
            Race.GENASI_WATER,
        ),
        (
            GenasiFireRaceAssigner,
            SubraceName.GENASI_FIRE_FIRE_GENASI_ELEMENTALEVILPLAYERSCOMPANION,
            Race.GENASI_FIRE,
        ),
        (
            GenasiEarthRaceAssigner,
            SubraceName.GENASI_EARTH_EARTH_GENASI_ELEMENTALEVILPLAYERSCOMPANION,
            Race.GENASI_EARTH,
        ),
        (
            GoliathRaceAssigner,
            SubraceName.GOLIATH_GOLIATH_ELEMENTALEVILPLAYERSGUIDE,
            Race.GOLIATH,
        ),
        (
            FirbolgRaceAssigner,
            SubraceName.FIRBOLG_FIRBOLG_VOLOSGUIDETOMONSTERS,
            Race.FIRBOLG,
        ),
        (
            TabaxiRaceAssigner,
            SubraceName.TABAXI_TABAXI_VOLOSGUIDETOMONSTERS,
            Race.TABAXI,
        ),
        (
            LizardfolkRaceAssigner,
            SubraceName.LIZARDFOLK_LIZARDFOLK_VOLOSGUIDETOMONSTERS,
            Race.LIZARDFOLK,
        ),
        (
            KenkuRaceAssigner,
            SubraceName.KENKU_KENKU_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.KENKU,
        ),
        (
            TortleRaceAssigner,
            SubraceName.TORTLE_TORTLE_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.TORTLE,
        ),
        (
            AarakocraRaceAssigner,
            SubraceName.AARAKOCRA_AARAKOCRA_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.AARAKOCRA,
        ),
        (
            BugbearRaceAssigner,
            SubraceName.BUGBEAR_BUGBEAR_VOLOSGUIDETOMONSTERS,
            Race.BUGBEAR,
        ),
        (
            GoblinRaceAssigner,
            SubraceName.GOBLIN_GOBLIN_VOLOSGUIDETOMONSTERS,
            Race.GOBLIN,
        ),
        (
            HobgoblinRaceAssigner,
            SubraceName.HOBGOBLIN_HOBGOBLIN_VOLOSGUIDETOMONSTERS,
            Race.HOBGOBLIN,
        ),
        (
            KoboldRaceAssigner,
            SubraceName.KOBOLD_KOBOLD_VOLOSGUIDETOMONSTERS,
            Race.KOBOLD,
        ),
        (OrcRaceAssigner, SubraceName.ORC_ORC_VOLOSGUIDETOMONSTERS, Race.ORC),
        (
            WarforgedRaceAssigner,
            SubraceName.WARFORGED_WARFORGED_EBERRONRISINGFROMTHELASTWAR,
            Race.WARFORGED,
        ),
        (
            ChangelingRaceAssigner,
            SubraceName.CHANGELING_CHANGELING_EBERRONRISINGFROMTHELASTWAR,
            Race.CHANGELING,
        ),
        (
            ShifterRaceAssigner,
            SubraceName.SHIFTER_BEASTHIDE_EBERRONRISINGFROMTHELASTWAR,
            Race.SHIFTER,
        ),
        (
            MinotaurRaceAssigner,
            SubraceName.MINOTAUR_MINOTAUR_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.MINOTAUR,
        ),
        (
            CentaurRaceAssigner,
            SubraceName.CENTAUR_GRUUL_CENTAUR_GUILDMASTERSGUIDETORAVNICA,
            Race.CENTAUR,
        ),
        (
            SatyrRaceAssigner,
            SubraceName.SATYR_SATYR_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.SATYR,
        ),
        (LeoninRaceAssigner, SubraceName.LEONIN_LEONIN_LEONINFEATURES, Race.LEONIN),
        (VerdanRaceAssigner, SubraceName.VERDAN_VERDAN_PLAYERSHANDBOOK, Race.VERDAN),
        (GrungRaceAssigner, SubraceName.GRUNG_GRUNG_PLAYERSHANDBOOK, Race.GRUNG),
        (
            KalashtarRaceAssigner,
            SubraceName.KALASHTAR_KALASHTAR_EBERRONRISINGFROMTHELASTWAR,
            Race.KALASHTAR,
        ),
        (
            YuanTiPurebloodRaceAssigner,
            SubraceName.YUAN_TI_PUREBLOOD_VOLOSGUIDETOMONSTERS,
            Race.YUAN_TI_PUREBLOOD,
        ),
    ],
)
def test_race_assigner(
    assigner_cls: type, subrace: SubraceName, expected_race: Race
) -> None:
    a = assigner_cls(subrace=subrace)
    assert a._get_race_and_subrace() == RaceSubracePair(
        race=expected_race, subrace=subrace
    )


@pytest.mark.unit
def test_dwarf_race_assigner_adds_health_modifier() -> None:
    assigner = DwarfRaceAssigner(subrace=SubraceName.DWARF_HILL_DWARF_PLAYERSHANDBOOK)
    stats = Stats(
        strength=10,
        dexterity=10,
        constitution=10,
        intelligence=10,
        wisdom=10,
        charisma=10,
    )
    result = assigner.apply(Blueprint(stats=stats))
    assert len(result.health_modifiers) == 1
    assert isinstance(result.health_modifiers[0], DwarfHealthModifier)


def test_race_assigner_apply() -> None:
    assigner = HumanRaceAssigner(
        subrace=SubraceName.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK
    )
    stats = Stats(
        strength=10,
        dexterity=10,
        constitution=10,
        intelligence=10,
        wisdom=10,
        charisma=10,
    )
    blueprint = Blueprint(stats=stats)
    result = assigner.apply(blueprint)
    assert result.race == Race.HUMAN
    assert result.subrace == SubraceName.HUMAN_VARIANT_HUMAN_PLAYERSHANDBOOK
    assert result.stats is not None


@pytest.mark.unit
@pytest.mark.parametrize(
    "assigner_cls, subrace, expected_race",
    [
        (ElfRaceAssigner, SubraceName.ELF_HIGH_ELF_PLAYERSHANDBOOK, Race.ELF),
        (
            HalflingRaceAssigner,
            SubraceName.HALFLING_LIGHTFOOT_PLAYERSHANDBOOK,
            Race.HALFLING,
        ),
        (
            HalfElfRaceAssigner,
            SubraceName.HALF_ELF_HIGH_ELF_HERITAGE_PLAYERSHANDBOOK,
            Race.HALF_ELF,
        ),
        (
            DragonbornRaceAssigner,
            SubraceName.DRAGONBORN_DRAGONBORN_PLAYERSHANDBOOK,
            Race.DRAGONBORN,
        ),
        (
            AasimarRaceAssigner,
            SubraceName.AASIMAR_FALLEN_AASIMAR_VOLOSGUIDETOMONSTERS,
            Race.AASIMAR,
        ),
        (
            GenasiAirRaceAssigner,
            SubraceName.GENASI_AIR_AIR_GENASI_ELEMENTALEVILPLAYERSCOMPANION,
            Race.GENASI_AIR,
        ),
        (
            GenasiWaterRaceAssigner,
            SubraceName.GENASI_WATER_WATER_GENASI_ELEMENTALEVILPLAYERSCOMPANION,
            Race.GENASI_WATER,
        ),
        (
            GenasiFireRaceAssigner,
            SubraceName.GENASI_FIRE_FIRE_GENASI_ELEMENTALEVILPLAYERSCOMPANION,
            Race.GENASI_FIRE,
        ),
        (
            GenasiEarthRaceAssigner,
            SubraceName.GENASI_EARTH_EARTH_GENASI_ELEMENTALEVILPLAYERSCOMPANION,
            Race.GENASI_EARTH,
        ),
        (
            FirbolgRaceAssigner,
            SubraceName.FIRBOLG_FIRBOLG_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.FIRBOLG,
        ),
        (
            KenkuRaceAssigner,
            SubraceName.KENKU_KENKU_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.KENKU,
        ),
        (
            AarakocraRaceAssigner,
            SubraceName.AARAKOCRA_AARAKOCRA_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.AARAKOCRA,
        ),
        (
            BugbearRaceAssigner,
            SubraceName.BUGBEAR_BUGBEAR_VOLOSGUIDETOMONSTERS,
            Race.BUGBEAR,
        ),
        (
            GoblinRaceAssigner,
            SubraceName.GOBLIN_GOBLIN_VOLOSGUIDETOMONSTERS,
            Race.GOBLIN,
        ),
        (
            HobgoblinRaceAssigner,
            SubraceName.HOBGOBLIN_HOBGOBLIN_VOLOSGUIDETOMONSTERS,
            Race.HOBGOBLIN,
        ),
        (
            KoboldRaceAssigner,
            SubraceName.KOBOLD_KOBOLD_VOLOSGUIDETOMONSTERS,
            Race.KOBOLD,
        ),
        (OrcRaceAssigner, SubraceName.ORC_ORC_VOLOSGUIDETOMONSTERS, Race.ORC),
        (
            WarforgedRaceAssigner,
            SubraceName.WARFORGED_WARFORGED_EBERRONRISINGFROMTHELASTWAR,
            Race.WARFORGED,
        ),
        (
            ChangelingRaceAssigner,
            SubraceName.CHANGELING_CHANGELING_EBERRONRISINGFROMTHELASTWAR,
            Race.CHANGELING,
        ),
        (
            ShifterRaceAssigner,
            SubraceName.SHIFTER_BEASTHIDE_EBERRONRISINGFROMTHELASTWAR,
            Race.SHIFTER,
        ),
        (
            MinotaurRaceAssigner,
            SubraceName.MINOTAUR_MINOTAUR_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.MINOTAUR,
        ),
        (
            CentaurRaceAssigner,
            SubraceName.CENTAUR_GRUUL_CENTAUR_GUILDMASTERSGUIDETORAVNICA,
            Race.CENTAUR,
        ),
        (
            SatyrRaceAssigner,
            SubraceName.SATYR_SATYR_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
            Race.SATYR,
        ),
        (VerdanRaceAssigner, SubraceName.VERDAN_VERDAN_PLAYERSHANDBOOK, Race.VERDAN),
        (
            KalashtarRaceAssigner,
            SubraceName.KALASHTAR_KALASHTAR_EBERRONRISINGFROMTHELASTWAR,
            Race.KALASHTAR,
        ),
        (
            YuanTiPurebloodRaceAssigner,
            SubraceName.YUAN_TI_PUREBLOOD_VOLOSGUIDETOMONSTERS,
            Race.YUAN_TI_PUREBLOOD,
        ),
    ],
)
def test_race_assigner_apply_variants(
    assigner_cls: type, subrace: SubraceName, expected_race: Race
) -> None:
    assigner = assigner_cls(subrace=subrace)
    stats = Stats(
        strength=10,
        dexterity=10,
        constitution=10,
        intelligence=10,
        wisdom=10,
        charisma=10,
    )
    result = assigner.apply(Blueprint(stats=stats))
    assert result.race == expected_race
    assert result.subrace == subrace
    assert result.stats is not None
    assert result.n_stat_choices == 0
    assert result.n_skill_choices == 0


@pytest.mark.unit
def test_generic_race_assigner_apply() -> None:
    assigner = RaceAssigner(
        race=Race.HUMAN,
        subrace=SubraceName.HUMAN_STANDARD_HUMAN_PLAYERSHANDBOOK,
    )
    stats = Stats(
        strength=10,
        dexterity=10,
        constitution=10,
        intelligence=10,
        wisdom=10,
        charisma=10,
    )
    result = assigner.apply(Blueprint(stats=stats))
    assert result.race == Race.HUMAN
    assert result.subrace == SubraceName.HUMAN_STANDARD_HUMAN_PLAYERSHANDBOOK
    assert result.n_stat_choices == 0
    assert result.n_skill_choices == 0


@pytest.mark.unit
@pytest.mark.parametrize(
    "assigner_cls, subrace",
    [
        (GoliathRaceAssigner, SubraceName.GOLIATH_GOLIATH_ELEMENTALEVILPLAYERSGUIDE),
        (TabaxiRaceAssigner, SubraceName.TABAXI_TABAXI_VOLOSGUIDETOMONSTERS),
        (
            LizardfolkRaceAssigner,
            SubraceName.LIZARDFOLK_LIZARDFOLK_VOLOSGUIDETOMONSTERS,
        ),
        (
            TortleRaceAssigner,
            SubraceName.TORTLE_TORTLE_MORDENKAINENPRESENTSMONSTERSOFTHEMULTIVERSE,
        ),
    ],
)
def test_race_assigner_apply_without_skill_resolver_raises(
    assigner_cls: type, subrace: SubraceName
) -> None:
    """These assigners grant subrace skill choices but declare no
    skill_choice_resolver field, so n_skill_choices is never reset to 0
    before the result is validated against the Literal[0] blueprint state.
    Every subrace option available on these assigners has this property,
    so apply() always raises for them -- a pre-existing production issue,
    not something this test suite works around.
    """
    assigner = assigner_cls(subrace=subrace)
    stats = Stats(
        strength=10,
        dexterity=10,
        constitution=10,
        intelligence=10,
        wisdom=10,
        charisma=10,
    )
    with pytest.raises(ValidationError):
        assigner.apply(Blueprint(stats=stats))
