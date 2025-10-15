from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from .room_schema import RoomSchema
from .user_schema import UserSchema
from .team_schema import TeamSchema

class BookingSchema(BaseModel):
    id: Optional[int] = None
    room: RoomSchema
    user: Optional[UserSchema] = None
    team: Optional[TeamSchema] = None
    slot_start: datetime
    slot_end: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True, frozen=True)

    def __str__(self) -> str:
        if self.user:
            return f"{self.user.name} - {self.room.room_type} ({self.slot_start:%Y-%m-%d %H:%M})"
        if self.team:
            return f"{self.team.name} - {self.room.room_type} ({self.slot_start:%Y-%m-%d %H:%M})"
        return f"Booking {self.id or 'N/A'} - {self.room.room_type}"
