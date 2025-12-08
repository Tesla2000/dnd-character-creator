from __future__ import annotations

from typing import Optional

from dnd_character_creator.character.blueprint.blueprint import Blueprint
from dnd_character_creator.character.blueprint.building_blocks.level_up.spell_assignment.base import (
    SpellAssigner,
)
from dnd_character_creator.character.spells import Spell
from dnd_character_creator.choices.class_creation.character_class import Class
from langchain_openai import ChatOpenAI
from pydantic import ConfigDict
from pydantic import create_model


class LLMSpellAssigner(SpellAssigner):
    """Uses LLM to select thematically appropriate spells.

    Selects spells based on character background, personality, and theme
    using an LLM to make intelligent choices that fit the character concept.

    Example:
        >>> assigner = LLMSpellAssigner(
        ...     class_=Class.WIZARD,
        ...     model_name="gpt-4o-mini",
        ...     character_description="Fire-focused evocation specialist",
        ... )
    """

    model_config = ConfigDict(frozen=True)

    class_: Class
    model_name: str = "gpt-4o-mini"
    temperature: float = 0.7
    character_description: Optional[str] = None

    def _select_spells(
        self,
        spell_level: int,
        count: int,
        available_spells: list[Spell],
        blueprint: Blueprint,
    ) -> tuple[Spell, ...]:
        """Use LLM to select thematically fitting spells.

        Args:
            spell_level: The spell level (0-9).
            count: Number of spells to select.
            available_spells: List of available spells to choose from.
            blueprint: Current character blueprint for context.

        Returns:
            Tuple of selected spells.
        """
        # Build context prompt
        spell_level_name = (
            "cantrips" if spell_level == 0 else f"level {spell_level} spells"
        )

        context = f"""You are selecting {count} {spell_level_name} for a D&D 5e character.

Character Details:
- Name: {blueprint.name or 'Unknown'}
- Class: {self.class_.value}
- Level: {blueprint.level or 1}
- Race: {blueprint.race.value if blueprint.race else 'Unknown'}
- Background: {blueprint.background.value if blueprint.background else 'Unknown'}
- Backstory: {blueprint.backstory or 'Generic adventurer'}
- Description: {self.character_description or 'Standard character'}
- Alignment: {blueprint.alignment.value if blueprint.alignment else 'Unknown'}

Available spells to choose from:
{'\n'.join(f"- {s.value}" for s in available_spells)}

Select exactly {count} spell(s) that:
1. Fit the character's theme, personality, and backstory
2. Complement their role and combat style
3. Provide tactical variety and utility
4. Match their alignment and values
5. Would make sense for their background and experience

Choose spells that tell a story about who this character is."""

        # Create dynamic response model for this spell level
        spell_enum = type(available_spells[0])
        SpellSelection = create_model(
            f"Level{spell_level}SpellSelection",
            spells=(tuple[spell_enum, ...], ...),
        )

        # Get LLM selection
        llm = ChatOpenAI(model=self.model_name, temperature=self.temperature)
        structured = llm.with_structured_output(SpellSelection)

        try:
            result = structured.invoke(context)
        except Exception as e:
            raise ValueError(
                f"LLM failed to select spells for level {spell_level}: {e}"
            )

        # Return exactly count spells
        return tuple(result.spells[:count])
