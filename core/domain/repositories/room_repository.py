from typing import Protocol
from core.domain.entities.room_entity import RoomEntity
from .base_repository import BaseRepository

class RoomRepository(BaseRepository[RoomEntity], Protocol):
    pass
