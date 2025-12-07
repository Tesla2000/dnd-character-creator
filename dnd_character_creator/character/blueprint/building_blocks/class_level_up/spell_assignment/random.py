from __future__ import annotations

import random
from itertools import chain, filterfalse
from typing import Generator, Optional, ClassVar

from frozendict import frozendict
from pydantic import ConfigDict

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.class_level_up.spell_assignment.base import \
    SpellAssigner
from dnd_character_creator.choices.class_creation.character_class import Class
from dnd_character_creator.character.spells.max_spell_levels import (
    CasterType,
    MAX_SPELL_LEVELS,
)
from dnd_character_creator.character.spells import (
    Cantrip,
    EighthLevel,
    FifthLevel,
    FirstLevel,
    FourthLevel,
    NinthLevel,
    SecondLevel,
    SeventhLevel,
    SixthLevel,
    Spell,
    ThirdLevel,
    filter_accessible,
)
from dnd_character_creator.character.spells import (
    spellcasting_ability_map,
)
from dnd_character_creator.character.spells.spells import Spells


class RandomSpellAssigner(SpellAssigner):
    """Randomly selects spells from available class spell list.

    Provides deterministic randomness when seed is set, useful for
    reproducible character generation.

    Example:
        >>> assigner = RandomSpellAssigner(
        ...     class_=Class.WIZARD,
        ...     seed=42,  # Reproducible
        ... )
    """

    model_config = ConfigDict(frozen=True)

    class_: Class
    seed: Optional[int] = None

    _class_to_caster: ClassVar[frozendict[Class, CasterType]] = frozendict({
        Class.BARD: CasterType.FULL,
        Class.CLERIC: CasterType.FULL,
        Class.DRUID: CasterType.FULL,
        Class.SORCERER: CasterType.FULL,
        Class.WIZARD: CasterType.FULL,
        Class.ARTIFICER: CasterType.HALF,
        Class.PALADIN: CasterType.HALF,
        Class.RANGER: CasterType.HALF,
        Class.WARLOCK: CasterType.WARLOCK,
        Class.FIGHTER: CasterType.ELDRITCH_KNIGHT,
        Class.ROGUE: CasterType.ELDRITCH_KNIGHT,
    })

    def get_change(
        self, blueprint: Blueprint
    ) -> Generator[Blueprint, Blueprint, None]:
        """Calculate and apply random spell assignments.

        Args:
            blueprint: The current blueprint state.

        Yields:
            Blueprint with updated spells.

        Raises:
            ValueError: If character doesn't have the specified class.
        """
        # 1. Validate class is spellcaster
        if self.class_ not in spellcasting_ability_map:
            # Not a spellcasting class, yield empty and return
            yield Blueprint()
            return

        # 5. Determine spells to learn
        spells_to_learn = self._get_spells_to_learn(
            blueprint
        )

        if not spells_to_learn:
            # No spells to learn for this class for this level
            yield Blueprint()
            return


        if self.seed is not None:
            random.seed(self.seed)

        # 8. Select spells for each level
        spells = blueprint.spells
        for spell_level, count in spells_to_learn.items():
            # Get available spells for this level
            available = self._get_available_spells(
                spell_level
            )

            # Filter out already-known spells
            existing_spells = set(chain.from_iterable(dict(blueprint.spells).values()))
            available_filtered = tuple(
                filterfalse(existing_spells.__contains__, available)
            )

            # Random selection
            n = min(count, len(available_filtered))
            selected = random.sample(available_filtered, n)

            # Merge with existing
            merged = existing_spells.union(selected)
            spells = spells.model_copy(update={tuple(blueprint.spells.model_fields.keys())[spell_level]: merged})

        yield Blueprint(spells=spells)

    def _get_effective_caster_level(self, blueprint: Blueprint) -> int:
        """Calculate effective caster level for multiclassing.

        For spell slots, combine levels from all caster classes:
        - Full casters (Wizard, Sorcerer, etc.): count full levels
        - Half casters (Paladin, Ranger): count half levels
        - Third casters (Eldritch Knight): count third levels

        Args:
            blueprint: Current character blueprint.

        Returns:
            Effective caster level for determining max spell level.
        """
        if self.class_ in (Class.SORCERER, Class.WIZARD):
            return blueprint.classes[Class.SORCERER] + blueprint.classes[Class.WIZARD]
        raise NotImplementedError("To be implemented")

    def _get_max_spell_level(self, blueprint: Blueprint) -> int:
        """Get the maximum spell level based on effective caster level.

        Args:
            effective_caster_level: The effective caster level.

        Returns:
            Maximum spell level (0-9).
        """
        effective_caster_level = self._get_effective_caster_level(blueprint)
        if effective_caster_level == 0:
            return 0
        caster_type = self._class_to_caster[self.class_]
        return MAX_SPELL_LEVELS[caster_type][
            min(effective_caster_level, 20) - 1
        ]

    @staticmethod
    def _is_first_level(blueprint: Blueprint) -> bool:
        return (blueprint.classes.get(Class.WIZARD, 0) + blueprint.classes.get(Class.SORCERER, 0)) == 1

    def _get_spells_to_learn(
        self, blueprint: Blueprint
    ) -> dict[int, int]:
        if self.class_ == Class.WIZARD:
            # Wizard-specific spell learning rules
            if self._is_first_level(blueprint):
                return {0: 3, 1: 6}
            return {self._get_max_spell_level(blueprint): 2}
        raise NotImplementedError("For non-wizards, no specific spell learning rules yet")

    def _get_available_spells(
        self, spell_level: int
    ) -> frozenset[Spell]:
        """Get all accessible spells for class at spell level.

        Args:
            spell_level: The spell level (0-9).

        Returns:
            List of available spells.
        """
        # Map spell level to spell class
        spell_level_to_class = {
            0: Cantrip,
            1: FirstLevel,
            2: SecondLevel,
            3: ThirdLevel,
            4: FourthLevel,
            5: FifthLevel,
            6: SixthLevel,
            7: SeventhLevel,
            8: EighthLevel,
            9: NinthLevel,
        }

        spell_type = spell_level_to_class[spell_level]
        return filter_accessible(spell_type, self.class_)

    def _get_spell_attr_name(self, spell_level: int) -> str:
        """Get the Spells model attribute name for a spell level.

        Args:
            spell_level: The spell level (0-9).

        Returns:
            Attribute name (e.g., 'first_level_spells').
        """
        spell_level_to_attr = {
            0: "cantrips",
            1: "first_level_spells",
            2: "second_level_spells",
            3: "third_level_spells",
            4: "fourth_level_spells",
            5: "fifth_level_spells",
            6: "sixth_level_spells",
            7: "seventh_level_spells",
            8: "eighth_level_spells",
            9: "ninth_level_spells",
        }
        return spell_level_to_attr[spell_level]
