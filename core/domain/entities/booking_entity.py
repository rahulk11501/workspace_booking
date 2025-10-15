from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from .room_entity import RoomEntity
from .user_entity import UserEntity
from .team_entity import TeamEntity

@dataclass(frozen=True)
class BookingEntity:
    room: RoomEntity
    user: Optional[UserEntity]
    team: Optional[TeamEntity]
    slot_start: datetime
    slot_end: datetime
    created_at: datetime
    id: Optional[int] = None
