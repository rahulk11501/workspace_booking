# core/schemas/room_schema.py
from pydantic import BaseModel, ConfigDict

class RoomSchema(BaseModel):
    id: int | None = None
    room_type: str
    capacity: int

    model_config = ConfigDict(from_attributes=True)
