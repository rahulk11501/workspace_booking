# core/schemas/booking_schema.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from .room_schema import RoomSchema
from .user_schema import UserSchema
from .team_schema import TeamSchema

class BookingSchema(BaseModel):
    id: int | None = None
    room: RoomSchema
    user: Optional[UserSchema] = None
    team: Optional[TeamSchema] = None
    slot_start: datetime
    slot_end: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
    def __str__(self):
        if self.user:
            return f"{self.user.name} - {self.room.room_type} ({self.slot_start})"
        if self.team:
            return f"{self.team.name} - {self.room.room_type} ({self.slot_start})"
        return f"Booking {self.id} - {self.room.room_type}"