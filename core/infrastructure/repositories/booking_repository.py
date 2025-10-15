from typing import List, Optional
from core.domain.entities.booking_entity import BookingEntity
from core.domain.entities.user_entity import UserEntity
from core.domain.entities.team_entity import TeamEntity
from core.domain.entities.room_entity import RoomEntity
from core.domain.repositories.booking_repository import BookingRepository
from core.models.booking import Booking as BookingModel

class DjangoBookingRepository(BookingRepository):
    def get(self, obj_id: int) -> Optional[BookingEntity]:
        obj = BookingModel.objects.filter(id=obj_id).first()
        if not obj:
            return None
        user = UserEntity(id=obj.user.id, name=obj.user.name, age=obj.user.age, gender=obj.user.gender) if obj.user else None
        team = TeamEntity(id=obj.team.id, name=obj.team.name, members=[]) if obj.team else None
        room = RoomEntity(id=obj.room.id, room_type=obj.room.room_type, capacity=obj.room.capacity)
        return BookingEntity(
            id=obj.id,
            room=room,
            user=user,
            team=team,
            slot_start=obj.slot_start,
            slot_end=obj.slot_end,
            created_at=obj.created_at
        )

    def list(self) -> List[BookingEntity]:
        return [self.get(b.id) for b in BookingModel.objects.all()]

    def create(self, entity: BookingEntity) -> BookingEntity:
        obj = BookingModel.objects.create(
            room_id=entity.room.id,
            user_id=entity.user.id if entity.user else None,
            team_id=entity.team.id if entity.team else None,
            slot_start=entity.slot_start,
            slot_end=entity.slot_end
        )
        return self.get(obj.id)

    def update(self, entity: BookingEntity) -> BookingEntity:
        obj = BookingModel.objects.get(id=entity.id)
        obj.room_id = entity.room.id
        obj.user_id = entity.user.id if entity.user else None
        obj.team_id = entity.team.id if entity.team else None
        obj.slot_start = entity.slot_start
        obj.slot_end = entity.slot_end
        obj.save()
        return self.get(obj.id)

    def delete(self, obj_id: int) -> None:
        BookingModel.objects.filter(id=obj_id).delete()
