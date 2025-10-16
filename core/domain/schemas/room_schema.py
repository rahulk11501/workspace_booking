from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator

class RoomSchema(BaseModel):
    room_type: str = Field(..., description="Type of room: PRIVATE, CONFERENCE, SHARED")
    capacity: int = Field(..., ge=1, description="Maximum number of users for the room")
    id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True, frozen=True)

    @field_validator("room_type")
    def validate_room_type(cls, v):
        allowed = ["PRIVATE", "CONFERENCE", "SHARED"]
        if v not in allowed:
            raise ValueError(f"room_type must be one of {allowed}")
        return v

    @field_validator("capacity")
    def validate_capacity(cls, v, info):
        room_type = info.data.get("room_type")
        if room_type == "PRIVATE" and v != 1:
            raise ValueError("Private rooms must have capacity = 1")
        if room_type == "CONFERENCE" and v < 3:
            raise ValueError("Conference rooms must allow at least 3 members")
        if room_type == "SHARED" and v > 4:
            raise ValueError("Shared desks can have max 4 users")
        return v
