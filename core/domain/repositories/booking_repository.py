from typing import Protocol
from core.domain.entities.booking_entity import BookingEntity
from .base_repository import BaseRepository

class BookingRepository(BaseRepository[BookingEntity], Protocol):
    pass
