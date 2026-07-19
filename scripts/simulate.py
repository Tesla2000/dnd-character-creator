import sys

from dnd.character._ability_name import AbilityName
from dnd.character.presentable_character import PresentableCharacter
from dnd.choices.equipment_creation.weapons import WeaponName
from dnd.fight._team_id import TeamId
from dnd.fight.battlemap import Battlemap
from dnd.fight.fight_character import FightCharacter
from dnd.fight.simulator import Simulator
from dnd.fight.strategy import RandomStrategy

_STATS = {
    "strength": 17,
    "dexterity": 13,
    "constitution": 16,
    "intelligence": 9,
    "wisdom": 11,
    "charisma": 8,
}

_BARBARIAN_BASE: dict[str, object] = {
    "race": "Human",
    "stats": _STATS,
    "health_base": 45,
    "character_data": {"name": ""},
    "classes": {
        "wizard": 0,
        "sorcerer": 0,
        "fighter": 0,
        "barbarian": 5,
        "rogue": 0,
        "cleric": 0,
        "druid": 0,
        "paladin": 0,
        "ranger": 0,
        "monk": 0,
        "bard": 0,
        "warlock": 0,
        "artificer": 0,
    },
    "speed": 30,
    "dark_vision_range": 0,
    "saving_throw_proficiencies": [],
    "other_active_abilities": [],
    "weapons": [WeaponName.BATTLEAXE],
    "actions": [AbilityName.ATTACK_WITH_BATTLEAXE, AbilityName.RAGE],
}


def _make_barbarian(name: str, initiative: int, team_id: TeamId) -> FightCharacter:
    data = {**_BARBARIAN_BASE, "character_data": {"name": name}}
    pc = PresentableCharacter.model_validate(data)
    return FightCharacter.from_presentable(
        pc, initiative=initiative, team_id=team_id
    ).model_copy(update={"position": (0, 0) if team_id == TeamId.A else (1, 0)})


def main() -> None:
    fc_a = _make_barbarian("Grog", initiative=15, team_id=TeamId.A)
    fc_b = _make_barbarian("Zog", initiative=12, team_id=TeamId.B)
    battlemap = Battlemap(combatants=(fc_a, fc_b))
    strategy = RandomStrategy()
    result = Simulator(battlemap, strategy_a=strategy, strategy_b=strategy).run()
    for line in result.log:
        sys.stdout.write(line)
    winner = f"Team {result.winner.name}" if result.winner is not None else "Draw"
    sys.stdout.write(f"\n{winner} wins in {result.rounds} rounds.")


if __name__ == "__main__":  # pragma: no cover
    main()
