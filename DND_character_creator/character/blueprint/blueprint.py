from typing import Type, Optional

from pydantic import create_model
from pydantic.fields import FieldInfo
from pydantic_core import PydanticUndefined

from DND_character_creator.character.character import Character

def _make_field_optional(field_info: FieldInfo) -> tuple[type, FieldInfo]:
    overrides = {}
    if field_info.default is PydanticUndefined and field_info.default_factory is None:
        overrides["default"] = None
        overrides["annotation"] = Optional[field_info.annotation]
    return (overrides.get("annotation", field_info.annotation), FieldInfo.merge_field_infos(field_info, **overrides))


Blueprint: Type[Character] = create_model("Blueprint", __base__=Character,**{
    field_name: _make_field_optional(field_info) for field_name, field_info in Character.model_fields.items()
})