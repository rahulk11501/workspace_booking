# core/schemas/team_schema.py
from pydantic import BaseModel, ConfigDict, field_validator
from typing import List
from .user_schema import UserSchema

class TeamSchema(BaseModel):
    id: int | None = None
    name: str
    members: List[UserSchema] = []

    model_config = ConfigDict(from_attributes=True)

    @field_validator("members", mode="before")
    def convert_members_manager(cls, v):
        """
        Convert Django ManyRelatedManager or QuerySet to a list
        before Pydantic validation.
        """
        # if v is a manager, turn into a list
        if hasattr(v, "all"):
            return list(v.all())
        # already a list
        return v
