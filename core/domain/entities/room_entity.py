from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class RoomEntity:
    room_type: str
    capacity: int
    id: Optional[int] = None
