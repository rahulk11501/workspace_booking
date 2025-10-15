from typing import Optional
from pydantic import BaseModel, ConfigDict

class RoomSchema(BaseModel):
    id: Optional[int] = None
    room_type: str
    capacity: int

    model_config = ConfigDict(from_attributes=True, frozen=True)
