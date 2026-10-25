# from random import randint
# from typing import ClassVar
#
# from pydantic import BaseModel, ConfigDict, NonNegativeInt, PositiveInt
#
# from dnd.fight._attack_result import _AttackResult
#
#
# class _Attack(BaseModel):
#     model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
#
#     n_dice: PositiveInt
#     dice_size: PositiveInt
#     attack_bonus: int
#     damage_bonus: int
#     name: str = ""
#     extra_n_dice: NonNegativeInt = 0
#     extra_dice_size: PositiveInt = 1
#     extra_damage_type: str = ""
#
#     def perform(self) -> _AttackResult:
#         roll1 = randint(1, 20)
#         roll2 = randint(1, 20)
#         damage = (
#             sum(randint(1, self.dice_size) for _ in range(self.n_dice))
#             + self.damage_bonus
#         )
#         crit_damage = damage + sum(
#             randint(1, self.dice_size) for _ in range(self.n_dice)
#         )
#         extra_damage = sum(
#             randint(1, self.extra_dice_size) for _ in range(self.extra_n_dice)
#         )
#         extra_crit_damage = extra_damage + sum(
#             randint(1, self.extra_dice_size) for _ in range(self.extra_n_dice)
#         )
#         return _AttackResult(
#             first_roll=roll1 + self.attack_bonus if roll1 != 20 else "critical",
#             second_roll=roll2 + self.attack_bonus if roll2 != 20 else "critical",
#             damage=damage,
#             crit_damage=crit_damage,
#             extra_damage=extra_damage,
#             extra_crit_damage=extra_crit_damage,
#             extra_damage_type=self.extra_damage_type,
#         )
