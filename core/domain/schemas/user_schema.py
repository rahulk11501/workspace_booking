from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional

class UserSchema(BaseModel):
    name: str = Field(..., max_length=100)
    age: int = Field(..., ge=0, le=120, description="Age must be between 0 and 120")
    gender: str = Field(..., pattern="^(Male|Female|Other)$")
    id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True, frozen=True)
