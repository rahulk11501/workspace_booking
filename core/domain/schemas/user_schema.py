from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., max_length=100)
    age: int = Field(..., ge=0)
    gender: str = Field(..., max_length=10)

    model_config = ConfigDict(from_attributes=True, frozen=True)
