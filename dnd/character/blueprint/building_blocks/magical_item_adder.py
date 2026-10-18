from typing import Literal

from dnd.character.ac_modifier import FlatAcModifier
from dnd.character.blueprint.building_blocks.building_block import BuildingBlock
from dnd.character.blueprint.building_blocks.building_block_type import (
    BuildingBlockType,
)
from dnd.character.blueprint.states.state import _BPT
from dnd.character.magical_item.item import MagicalItem
from dnd.character.magical_item.items import MAGICAL_ITEMS
from dnd.character.magical_item.specialized_items import ACAndSavingThrowBonusItem
from dnd.character.magical_item.specialized_items import SpellSaveDcBonusItem
from dnd.character.spell_attack_bonus_modifier import FlatSpellAttackBonus
from dnd.character.spell_save_dc_modifier import FlatSpellSaveDcBonus
from dnd.character.stats import Stats
from dnd.choices.stats_creation.statistic import Statistic
from pydantic import Field
from pydantic import field_validator


class MagicalItemAdder(BuildingBlock):
    """Adds a specific magical item and applies its AC, saving throw, spell save DC and spell attack bonuses."""

    type: Literal[BuildingBlockType.MAGICAL_ITEM_ADDER] = (
        BuildingBlockType.MAGICAL_ITEM_ADDER
    )

    item_name: str = Field(
        description="Exact name of the magical item, e.g. 'Cloak of Protection'"
    )

    @field_validator("item_name")
    @classmethod
    def _validate_item_name(cls, value: str) -> str:
        names = [item.name for item in MAGICAL_ITEMS]
        if value not in names:
            raise ValueError(f"Unknown magical item '{value}'. Available: {names}")
        return value

    def _find_item(self) -> MagicalItem:
        return next(item for item in MAGICAL_ITEMS if item.name == self.item_name)

    def apply(self, blueprint: _BPT) -> _BPT:
        item = self._find_item()
        update: dict[str, object] = {"magical_items": blueprint.magical_items + (item,)}
        if isinstance(item, ACAndSavingThrowBonusItem):
            update["ac_modifiers"] = blueprint.ac_modifiers + (
                FlatAcModifier(amount=item.ac_bonus),
            )
            update["saving_throw_bonuses"] = Stats.from_mapping(
                {
                    s: blueprint.saving_throw_bonuses.get_stat(s)
                    + item.saving_throw_bonus
                    for s in Statistic
                }
            )
        if isinstance(item, SpellSaveDcBonusItem):
            update["spell_save_dc_modifiers"] = blueprint.spell_save_dc_modifiers + (
                FlatSpellSaveDcBonus(bonus=item.spell_save_dc_bonus),
            )
            update["spell_attack_bonus_modifiers"] = (
                blueprint.spell_attack_bonus_modifiers
                + (FlatSpellAttackBonus(bonus=item.spell_attack_bonus),)
            )
        return blueprint.model_copy(update=update)
