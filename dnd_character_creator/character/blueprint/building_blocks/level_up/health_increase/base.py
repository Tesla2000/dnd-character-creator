from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar, Generator

from frozendict import frozendict

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.choices.equipment_creation.weapons import HitDieSize
from dnd_character_creator.character.race.race import Race
from dnd_character_creator.feats import Feat


class HealthIncrease(BuildingBlock, ABC):
    """Abstract base class for health increase strategies when leveling up.

    Subclasses must implement _get_hit_die_value to determine how much
    health to gain from the hit die (fixed value, random roll, etc.).
    """

    class_: Class

    _class2hit_die: ClassVar[frozendict[Class, HitDieSize]] = frozendict(
        {
            Class.BARBARIAN: HitDieSize.TWELVE,
            Class.BARD: HitDieSize.EIGHT,
            Class.CLERIC: HitDieSize.EIGHT,
            Class.DRUID: HitDieSize.EIGHT,
            Class.FIGHTER: HitDieSize.TEN,
            Class.MONK: HitDieSize.EIGHT,
            Class.PALADIN: HitDieSize.TEN,
            Class.RANGER: HitDieSize.TEN,
            Class.ROGUE: HitDieSize.EIGHT,
            Class.SORCERER: HitDieSize.SIX,
            Class.WARLOCK: HitDieSize.EIGHT,
            Class.WIZARD: HitDieSize.SIX,
            Class.ARTIFICER: HitDieSize.EIGHT,
        }
    )

    @abstractmethod
    def _get_hit_die_value(self, hit_die: HitDieSize) -> int:
        """Get the hit die value for health increase.

        Args:
            hit_die: The hit die for the class.

        Returns:
            The hit die value to add to health.
        """
        pass

    def _get_change(
        self, blueprint: Blueprint
    ) -> Blueprint:
        """Calculate and apply health increase.

        Args:
            blueprint: The current blueprint state.

        Yields:
            Blueprint with updated health.

        Raises:
            ValueError: If stats are not configured.
        """
        current_health = blueprint.health
        hit_die = self._class2hit_die[self.class_]

        # First level always gets max hit die value
        if current_health is None:
            hit_die_value = hit_die.value
            current_health = 0
        else:
            hit_die_value = self._get_hit_die_value(hit_die)

        if blueprint.stats is None:
            raise ValueError("Character's constitution is not configured")

        # Constitution modifier
        constitution_modifier = blueprint.stats.constitution // 2 - 5
        health_increase = hit_die_value + constitution_modifier

        # Feat bonuses
        if Feat.TOUGH in blueprint.feats:
            health_increase += 2

        # Race bonuses
        if blueprint.race == Race.DWARF:
            health_increase += 1

        return Blueprint(health=current_health + health_increase)
