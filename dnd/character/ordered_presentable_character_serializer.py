from typing import TypeAlias

from pydantic import ConfigDict, BaseModel

from dnd.character.presentable_character import PresentableCharacter

_SerializedCharacter: TypeAlias = dict[str, object]


class OrderedPresentableCharacterSerializer(BaseModel):
    model_config = ConfigDict(frozen=True)

    pinned_fields: tuple[str, ...] = (
        "health",
        "ac",
        "speed",
        "stats",
        "saving_throw_modifiers",
    )

    def serialize(self, character: PresentableCharacter) -> _SerializedCharacter:
        data = character.model_dump(mode="json")
        result = {k: data[k] for k in self.pinned_fields if k in data}
        result.update(
            sorted((k, v) for k, v in data.items() if k not in self.pinned_fields)
        )
        return result
