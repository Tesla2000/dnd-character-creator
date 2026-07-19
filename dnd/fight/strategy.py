import random
from typing import Generic, Protocol

from dnd.character.actions.combat import AnyCombatAction
from dnd.fight._combatant_slot import SlotT


class Strategy(Protocol[SlotT]):
    def choose(
        self, groups: tuple[tuple[AnyCombatAction[SlotT], ...], ...]
    ) -> AnyCombatAction[SlotT]: ...


class RandomStrategy(Generic[SlotT]):
    def choose(
        self, groups: tuple[tuple[AnyCombatAction[SlotT], ...], ...]
    ) -> AnyCombatAction[SlotT]:
        return random.choice(random.choice(groups))
