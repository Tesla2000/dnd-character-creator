from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections.abc import Iterable
from typing import TypeVar

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.choices.language import Language
from dnd_character_creator.feats import Feat
from dnd_character_creator.other_profficiencies import GamingSet
from dnd_character_creator.other_profficiencies import MusicalInstrument
from dnd_character_creator.other_profficiencies import ToolProficiency
from dnd_character_creator.skill_proficiency import Skill
from pydantic import ConfigDict

T = TypeVar("T")


class AnyChoiceResolver(BuildingBlock, ABC):
    """Abstract base class for resolving ANY_OF_YOUR_CHOICE placeholders.

    Subclasses must implement _select_from_available to determine how to pick
    concrete values when placeholders are encountered.
    """

    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def _select_from_available(self, available: list[T]) -> T:
        """Select an item from available options.

        Args:
            available: List of options excluding ANY_OF_YOUR_CHOICE placeholder.

        Returns:
            Selected item.
        """

    def _resolve_set(self, items: Iterable[T], placeholder_value: T) -> set[T]:
        resolved = set()
        for item in items:
            if item == placeholder_value:
                enum_class = type(item)
                available = [v for v in enum_class if v != placeholder_value]
                resolved.add(self._select_from_available(available))
            else:
                resolved.add(item)
        return resolved

    def _resolve_set_feat(
        self, items: Iterable[T], placeholder_value: T
    ) -> set[T]:
        resolved = set()
        for item in items:
            if item == placeholder_value:
                enum_class = type(item)
                available = [
                    v
                    for v in enum_class
                    if v
                    not in (placeholder_value, Feat.ABILITY_SCORE_IMPROVEMENT)
                ]
                resolved.add(self._select_from_available(available))
            else:
                resolved.add(item)
        return resolved

    def _resolve_tool_proficiencies(
        self,
        tools: tuple[ToolProficiency | GamingSet | MusicalInstrument, ...],
    ) -> set[ToolProficiency | GamingSet | MusicalInstrument]:
        """Resolve ANY_OF_YOUR_CHOICE placeholders in tool proficiencies.

        Handles union type with special logic for each tool type.

        Args:
            tools: Set of tool proficiencies potentially containing placeholders.

        Returns:
            Set with placeholders replaced by concrete choices.
        """
        resolved = set()
        for tool in tools:
            if (
                isinstance(tool, ToolProficiency)
                and tool == ToolProficiency.ANY_OF_YOUR_CHOICE
            ):
                available = [
                    t
                    for t in ToolProficiency
                    if t != ToolProficiency.ANY_OF_YOUR_CHOICE
                ]
                resolved.add(self._select_from_available(available))
            elif (
                isinstance(tool, GamingSet)
                and tool == GamingSet.ANY_OF_YOUR_CHOICE
            ):
                available = [
                    g for g in GamingSet if g != GamingSet.ANY_OF_YOUR_CHOICE
                ]
                resolved.add(self._select_from_available(available))
            elif (
                isinstance(tool, MusicalInstrument)
                and tool == MusicalInstrument.ANY_OF_YOUR_CHOICE
            ):
                available = [
                    m
                    for m in MusicalInstrument
                    if m != MusicalInstrument.ANY_OF_YOUR_CHOICE
                ]
                resolved.add(self._select_from_available(available))
            else:
                resolved.add(tool)
        return resolved

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Replace ANY_OF_YOUR_CHOICE placeholders in blueprint with concrete choices."""

        return Blueprint(
            languages=self._resolve_set(
                blueprint.languages, Language.ANY_OF_YOUR_CHOICE
            ),
            skill_proficiencies=self._resolve_set(
                blueprint.skill_proficiencies, Skill.ANY_OF_YOUR_CHOICE
            ),
            feats=self._resolve_set_feat(
                blueprint.feats, Feat.ANY_OF_YOUR_CHOICE
            ),
            tool_proficiencies=self._resolve_tool_proficiencies(
                blueprint.tool_proficiencies
            ),
        )
