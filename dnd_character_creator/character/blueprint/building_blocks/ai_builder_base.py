from __future__ import annotations

from abc import abstractmethod
from typing import Any, Mapping

from frozendict import frozendict
from langchain_openai import ChatOpenAI
from pydantic import Field

from dnd_character_creator.character.blueprint.building_blocks.building_block import (
    BuildingBlock,
)
from dnd_character_creator.character.blueprint.building_blocks.character_base_template import (
    CharacterBaseTemplate,
)


class AIBuilderBase(BuildingBlock):
    """Base class for AI-powered character builders.

    Provides common functionality for AI building blocks that use LLM
    structured output to generate character parameters from descriptions.
    """

    description: str = Field(
        description="Natural language description of the character to generate"
    )

    model_name: str = Field(
        description="OpenAI model name to use for generation",
    )

    temperature: float = Field(
        default=0.7, description="Temperature for AI generation (0-2)"
    )

    ai_model_kwargs: Mapping[str, Any] = Field(
        default_factory=frozendict,
        description="Additional kwargs to pass to ChatOpenAI",
    )

    def _create_llm(self) -> ChatOpenAI:
        """Create a ChatOpenAI instance with configured parameters.

        Returns:
            Configured ChatOpenAI instance.
        """
        return ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            **self.ai_model_kwargs
        )

    def _generate_character_template(
        self, prompt: str
    ) -> CharacterBaseTemplate:
        """Generate character parameters using AI.

        Args:
            prompt: The prompt to send to the AI.

        Returns:
            CharacterBaseTemplate with AI-generated values.
        """
        llm = self._create_llm()
        template = llm.with_structured_output(CharacterBaseTemplate)
        return template.invoke(prompt)
