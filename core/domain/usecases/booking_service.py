from typing import List, Optional
from core.domain.entities.booking_entity import BookingEntity
from core.domain.repositories.booking_repository import BookingRepository

class BookingService:
    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def get_booking(self, booking_id: int) -> Optional[BookingEntity]:
        return self.repository.get(booking_id)

    def list_bookings(self) -> List[BookingEntity]:
        return self.repository.list()

    def create_booking(self, booking: BookingEntity) -> BookingEntity:
        # Add any business rules here, e.g., overlapping check
        return self.repository.create(booking)

    def update_booking(self, booking: BookingEntity) -> BookingEntity:
        # Add business logic validations if needed
        return self.repository.update(booking)

    def delete_booking(self, booking_id: int) -> None:
        self.repository.delete(booking_id)
