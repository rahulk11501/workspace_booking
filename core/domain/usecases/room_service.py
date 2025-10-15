from typing import List, Optional
from core.domain.entities.room_entity import RoomEntity
from core.domain.repositories.room_repository import RoomRepository

class RoomService:
    def __init__(self, repository: RoomRepository):
        self.repository = repository

    def get_room(self, room_id: int) -> Optional[RoomEntity]:
        return self.repository.get(room_id)

    def list_rooms(self) -> List[RoomEntity]:
        return self.repository.list()

    def create_room(self, room: RoomEntity) -> RoomEntity:
        return self.repository.create(room)

    def update_room(self, room: RoomEntity) -> RoomEntity:
        return self.repository.update(room)

    def delete_room(self, room_id: int) -> None:
        self.repository.delete(room_id)
