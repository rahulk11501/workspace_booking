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
    def normalize_members(cls, value: Any) -> List[UserSchema]:
        """Convert Django ManyRelatedManager or QuerySet to list before validation."""
        if hasattr(value, "all"):
            return list(value.all())
        return list(value) if value else []
