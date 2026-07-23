from dnd.character.stats import Stats
from dnd.fight._attack import _Attack
from dnd.fight._creature import _Creature

_BROWN_BEAR_CLAW = _Attack(name="Claw", n_dice=2, dice_size=6, attack_bonus=5, damage_bonus=4)

_BROWN_BEAR = _Creature(
    name="Brown Bear",
    stats=Stats(
        strength=19,
        dexterity=10,
        constitution=16,
        intelligence=2,
        wisdom=13,
        charisma=7,
    ),
    speed=40,
    dark_vision_range=0,
    saving_throw_proficiencies=(),
    other_active_abilities=(),
    initiative=10,
    n_hit_dice=4,
    hit_die_size=8,
    hp=34,
    attacks=(_BROWN_BEAR_CLAW,),
)

_POLAR_BEAR_CLAW = _Attack(name="Claw", n_dice=2, dice_size=6, attack_bonus=7, damage_bonus=5)

_POLAR_BEAR = _Creature(
    name="Polar Bear",
    stats=Stats(
        strength=20,
        dexterity=10,
        constitution=16,
        intelligence=2,
        wisdom=13,
        charisma=7,
    ),
    speed=40,
    dark_vision_range=0,
    saving_throw_proficiencies=(),
    other_active_abilities=(),
    initiative=10,
    n_hit_dice=6,
    hit_die_size=10,
    hp=42,
    attacks=(_POLAR_BEAR_CLAW,),
)


_WOLF_BITE = _Attack(name="Bite", n_dice=2, dice_size=4, attack_bonus=4, damage_bonus=2)

_WOLF = _Creature(
    name="Wolf",
    stats=Stats(
        strength=12,
        dexterity=15,
        constitution=12,
        intelligence=3,
        wisdom=12,
        charisma=6,
    ),
    speed=40,
    ac_bonus=1,
    dark_vision_range=0,
    saving_throw_proficiencies=(),
    other_active_abilities=(),
    initiative=10,
    n_hit_dice=2,
    hit_die_size=8,
    hp=11,
    attacks=(_WOLF_BITE,),
)


def beast_form_for_druid_level(level: int) -> _Creature:
    """Circle Forms: CR<=1 from level 2, CR<=druid_level//3 from level 6."""
    return _POLAR_BEAR if level >= 6 else _BROWN_BEAR
