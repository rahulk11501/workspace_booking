# core/domain/schemas/user_schema.py
from pydantic import BaseModel, ConfigDict, Field

class UserSchema(BaseModel):
    name: str = Field(..., max_length=100)
    age: int = Field(..., ge=0)
    gender: str = Field(..., max_length=10)

    model_config = ConfigDict(from_attributes=True)
