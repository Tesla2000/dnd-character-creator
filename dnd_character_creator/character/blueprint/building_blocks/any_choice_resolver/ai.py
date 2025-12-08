"""AI-powered choice resolver for ANY_OF_YOUR_CHOICE placeholders."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.blueprint_formatter import (
    BlueprintFormatter,
)
from dnd_character_creator.character.blueprint.building_blocks.any_choice_resolver.base import (
    AnyChoiceResolver,
)
from dnd_character_creator.choices.language import Language
from dnd_character_creator.feats import Feat
from dnd_character_creator.other_profficiencies import GamingSet
from dnd_character_creator.other_profficiencies import MusicalInstrument
from dnd_character_creator.other_profficiencies import ToolProficiency
from dnd_character_creator.skill_proficiency import Skill
from frozendict import frozendict
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from pydantic import Field


class AnyChoiceSelection(BaseModel):
    """Schema for AI to select placeholder replacements."""

    languages: set[Language] = Field(default_factory=set)
    skill_proficiencies: set[Skill] = Field(default_factory=set)
    feats: set[Feat] = Field(default_factory=set)
    tool_proficiencies: set[
        ToolProficiency | GamingSet | MusicalInstrument
    ] = Field(default_factory=set)


class AIAnyChoiceResolver(AnyChoiceResolver):
    """AI-powered resolver for ANY_OF_YOUR_CHOICE placeholders.

    Uses an LLM to make intelligent selections when resolving ANY_OF_YOUR_CHOICE
    placeholders in languages, skills, feats, and tool proficiencies based on
    character context.

    Example:
        >>> resolver = AIAnyChoiceResolver(
        ...     model_name="gpt-4o-mini",
        ...     temperature=0.3
        ... )
        >>> builder = Builder().add(resolver)
    """

    model_name: str = Field(
        description="OpenAI model name to use for choice resolution"
    )

    temperature: float = Field(
        default=0.3,
        description="Temperature for AI selection (lower = more deterministic)",
    )

    ai_model_kwargs: Mapping[str, Any] = Field(
        default_factory=frozendict,
        description="Additional kwargs to pass to ChatOpenAI",
    )

    formatter: BlueprintFormatter = Field(
        default_factory=BlueprintFormatter,
        description="Blueprint formatter for creating AI prompts",
    )

    def _select_from_available(self, available: list) -> Any:
        """Not used in AI implementation - overrides _get_change instead."""
        raise NotImplementedError(
            "AIAnyChoiceResolver overrides _get_change directly"
        )

    def _create_llm(self) -> ChatOpenAI:
        """Create a ChatOpenAI instance with configured parameters.

        Returns:
            Configured ChatOpenAI instance.
        """
        return ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            **self.ai_model_kwargs,
        )

    def _build_prompt(self, blueprint: Blueprint) -> str:
        """Build a prompt for AI placeholder resolution.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Formatted prompt string.
        """
        system_prompt = (
            "You are resolving ANY_OF_YOUR_CHOICE placeholders for a D&D 5e character.\n"
            "Replace each placeholder with the most appropriate specific choice based on "
            "the character's class, background, and concept.\n"
        )

        # Use formatter with custom system prompt
        character_description = self.formatter.format(
            blueprint, system_prompt=system_prompt
        )

        instructions = ["\n## Placeholders to Resolve\n"]

        # Check what placeholders exist
        has_placeholders = False

        if Language.ANY_OF_YOUR_CHOICE in blueprint.languages:
            count = list(blueprint.languages).count(
                Language.ANY_OF_YOUR_CHOICE
            )
            instructions.append(
                f"Languages: {count} ANY_OF_YOUR_CHOICE placeholder(s) to replace"
            )
            instructions.append(
                f"  Available: {', '.join(language.value for language in Language if language != Language.ANY_OF_YOUR_CHOICE)}"
            )
            has_placeholders = True

        if Skill.ANY_OF_YOUR_CHOICE in blueprint.skill_proficiencies:
            count = list(blueprint.skill_proficiencies).count(
                Skill.ANY_OF_YOUR_CHOICE
            )
            instructions.append(
                f"Skill Proficiencies: {count} ANY_OF_YOUR_CHOICE placeholder(s) to replace"
            )
            instructions.append(
                f"  Available: {', '.join(s.value for s in Skill if s != Skill.ANY_OF_YOUR_CHOICE)}"
            )
            has_placeholders = True

        if Feat.ANY_OF_YOUR_CHOICE in blueprint.feats:
            count = list(blueprint.feats).count(Feat.ANY_OF_YOUR_CHOICE)
            instructions.append(
                f"Feats: {count} ANY_OF_YOUR_CHOICE placeholder(s) to replace"
            )
            available_feats = [
                f.value
                for f in Feat
                if f
                not in (
                    Feat.ANY_OF_YOUR_CHOICE,
                    Feat.ABILITY_SCORE_IMPROVEMENT,
                )
            ]
            instructions.append(f"  Available: {', '.join(available_feats)}")
            has_placeholders = True

        # Check tool proficiencies
        tool_placeholders = sum(
            1
            for t in blueprint.tool_proficiencies
            if (
                (
                    isinstance(t, ToolProficiency)
                    and t == ToolProficiency.ANY_OF_YOUR_CHOICE
                )
                or (
                    isinstance(t, GamingSet)
                    and t == GamingSet.ANY_OF_YOUR_CHOICE
                )
                or (
                    isinstance(t, MusicalInstrument)
                    and t == MusicalInstrument.ANY_OF_YOUR_CHOICE
                )
            )
        )
        if tool_placeholders > 0:
            instructions.append(
                f"Tool Proficiencies: {tool_placeholders} ANY_OF_YOUR_CHOICE placeholder(s) to replace"
            )
            has_placeholders = True

        if not has_placeholders:
            return ""  # No placeholders to resolve

        instructions.append(
            "\n## Selection Instructions\n"
            "Return the complete sets with placeholders replaced by specific choices.\n"
            "Choose options that best fit the character's class, background, and concept.\n"
            "Avoid duplicates unless the character already has them."
        )

        return character_description + "\n".join(instructions)

    def _get_change(self, blueprint: Blueprint) -> Blueprint:
        """Replace ANY_OF_YOUR_CHOICE placeholders using AI.

        Args:
            blueprint: Current character blueprint.

        Returns:
            Blueprint with placeholders replaced by specific choices.
        """
        # Check if there are any placeholders
        has_language_placeholder = (
            Language.ANY_OF_YOUR_CHOICE in blueprint.languages
        )
        has_skill_placeholder = (
            Skill.ANY_OF_YOUR_CHOICE in blueprint.skill_proficiencies
        )
        has_feat_placeholder = Feat.ANY_OF_YOUR_CHOICE in blueprint.feats
        has_tool_placeholder = any(
            (
                isinstance(t, ToolProficiency)
                and t == ToolProficiency.ANY_OF_YOUR_CHOICE
            )
            or (isinstance(t, GamingSet) and t == GamingSet.ANY_OF_YOUR_CHOICE)
            or (
                isinstance(t, MusicalInstrument)
                and t == MusicalInstrument.ANY_OF_YOUR_CHOICE
            )
            for t in blueprint.tool_proficiencies
        )

        if not (
            has_language_placeholder
            or has_skill_placeholder
            or has_feat_placeholder
            or has_tool_placeholder
        ):
            # No placeholders to resolve
            return Blueprint()

        # Build prompt and get AI selection
        prompt = self._build_prompt(blueprint)

        llm = self._create_llm()
        structured_llm = llm.with_structured_output(AnyChoiceSelection)
        selection = structured_llm.invoke(prompt)

        # Validate and apply selections
        new_languages = set(blueprint.languages)
        new_skills = set(blueprint.skill_proficiencies)
        new_feats = set(blueprint.feats)
        new_tools = set(blueprint.tool_proficiencies)

        # Replace language placeholders
        if has_language_placeholder:
            count = list(blueprint.languages).count(
                Language.ANY_OF_YOUR_CHOICE
            )
            if len(selection.languages) != count:
                raise ValueError(
                    f"AI returned {len(selection.languages)} languages "
                    f"but expected {count}"
                )
            new_languages.discard(Language.ANY_OF_YOUR_CHOICE)
            new_languages.update(selection.languages)

        # Replace skill placeholders
        if has_skill_placeholder:
            count = list(blueprint.skill_proficiencies).count(
                Skill.ANY_OF_YOUR_CHOICE
            )
            if len(selection.skill_proficiencies) != count:
                raise ValueError(
                    f"AI returned {len(selection.skill_proficiencies)} skills "
                    f"but expected {count}"
                )
            new_skills.discard(Skill.ANY_OF_YOUR_CHOICE)
            new_skills.update(selection.skill_proficiencies)

        # Replace feat placeholders
        if has_feat_placeholder:
            count = list(blueprint.feats).count(Feat.ANY_OF_YOUR_CHOICE)
            if len(selection.feats) != count:
                raise ValueError(
                    f"AI returned {len(selection.feats)} feats "
                    f"but expected {count}"
                )
            new_feats.discard(Feat.ANY_OF_YOUR_CHOICE)
            new_feats.update(selection.feats)

        # Replace tool placeholders
        if has_tool_placeholder:
            # Remove all tool placeholders and add selections
            new_tools = {
                t
                for t in new_tools
                if not (
                    (
                        isinstance(t, ToolProficiency)
                        and t == ToolProficiency.ANY_OF_YOUR_CHOICE
                    )
                    or (
                        isinstance(t, GamingSet)
                        and t == GamingSet.ANY_OF_YOUR_CHOICE
                    )
                    or (
                        isinstance(t, MusicalInstrument)
                        and t == MusicalInstrument.ANY_OF_YOUR_CHOICE
                    )
                )
            }
            new_tools.update(selection.tool_proficiencies)

        return Blueprint(
            languages=new_languages,
            skill_proficiencies=new_skills,
            feats=new_feats,
            tool_proficiencies=new_tools,
        )
