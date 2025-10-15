from typing import List, Optional
from core.domain.entities.room_entity import RoomEntity
from core.domain.repositories.room_repository import RoomRepository
from core.models.room import Room as RoomModel

class DjangoRoomRepository(RoomRepository):
    def get(self, obj_id: int) -> Optional[RoomEntity]:
        obj = RoomModel.objects.filter(id=obj_id).first()
        if not obj:
            return None
        return RoomEntity(id=obj.id, room_type=obj.room_type, capacity=obj.capacity)

    def list(self) -> List[RoomEntity]:
        return [RoomEntity(id=r.id, room_type=r.room_type, capacity=r.capacity) for r in RoomModel.objects.all()]

    def create(self, entity: RoomEntity) -> RoomEntity:
        obj = RoomModel.objects.create(room_type=entity.room_type, capacity=entity.capacity)
        return RoomEntity(id=obj.id, room_type=obj.room_type, capacity=obj.capacity)

    def update(self, entity: RoomEntity) -> RoomEntity:
        obj = RoomModel.objects.get(id=entity.id)
        obj.room_type, obj.capacity = entity.room_type, entity.capacity
        obj.save()
        return RoomEntity(id=obj.id, room_type=obj.room_type, capacity=obj.capacity)

    def delete(self, obj_id: int) -> None:
        RoomModel.objects.filter(id=obj_id).delete()