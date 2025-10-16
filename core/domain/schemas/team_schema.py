from typing import List, Optional, Any
from pydantic import BaseModel, ConfigDict, field_validator
from .user_schema import UserSchema

class TeamSchema(BaseModel):
    id: Optional[int] = None
    name: str
    members: List[UserSchema] = []

    model_config = ConfigDict(from_attributes=True, frozen=True)

    @field_validator("members", mode="before")
    @classmethod
    def normalize_members(cls, v: Any) -> List[UserSchema]:
        """Convert Django QuerySet, Manager, or list to UserSchema list."""
        if hasattr(v, "all"):  # Django manager/queryset
            v = list(v.all())
        elif v is None:
            v = []
        members_list = []
        for item in v:
            if isinstance(item, dict):
                members_list.append(UserSchema.model_validate(item))
            else:
                members_list.append(UserSchema.model_validate(item))
        return members_list
