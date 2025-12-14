from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dnd_character_creator.character.blueprint.blueprint import Blueprint

from dnd_character_creator.character.feature.feature import Feature
from dnd_character_creator.character.stats import Stats
from dnd_character_creator.choices.stats_creation.statistic import Statistic


class SavingThrowBonusFeature(Feature):
    """A feature that provides bonuses to saving throws.

    Can provide a universal bonus to all saves, or a bonus to a specific
    ability's saving throw.

    Examples:
        - Resilient feat (grants proficiency in one save)
        - Aura of Protection (paladin feature)
        - Lucky feat
    """

    stat: Statistic | None = None
    bonus: int = 1

    def assign_to(self, blueprint: Blueprint) -> Blueprint:
        """Add saving throw bonus to character.

        If stat is specified, adds bonus to that specific save.
        Otherwise, adds bonus to all saves.
        """
        if self.stat is None:
            # Universal bonus to all saves
            new_saving_throw_bonuses = Stats(
                strength=blueprint.saving_throw_bonuses.strength + self.bonus,
                dexterity=blueprint.saving_throw_bonuses.dexterity
                + self.bonus,
                constitution=blueprint.saving_throw_bonuses.constitution
                + self.bonus,
                intelligence=blueprint.saving_throw_bonuses.intelligence
                + self.bonus,
                wisdom=blueprint.saving_throw_bonuses.wisdom + self.bonus,
                charisma=blueprint.saving_throw_bonuses.charisma + self.bonus,
            )
        else:
            # Bonus to specific save
            stat_name = self.stat.value.lower()
            current_bonus = getattr(blueprint.saving_throw_bonuses, stat_name)
            new_saving_throw_bonuses = Stats(
                **{
                    **blueprint.saving_throw_bonuses.model_dump(),
                    stat_name: current_bonus + self.bonus,
                }
            )

        return type(blueprint)(
            saving_throw_bonuses=new_saving_throw_bonuses,
            other_active_abilities=blueprint.other_active_abilities
            + (f"{self.name}: {self.description}",),
        )
