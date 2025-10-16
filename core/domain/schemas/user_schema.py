from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., max_length=100)
    age: int = Field(..., ge=0)
    gender: str = Field(..., max_length=10)

    model_config = ConfigDict(from_attributes=True, frozen=True)

    @field_validator("gender")
    def validate_gender(cls, v):
        if v not in ["Male", "Female", "Other"]:
            raise ValueError(f"Invalid gender: {v}")
        return v
