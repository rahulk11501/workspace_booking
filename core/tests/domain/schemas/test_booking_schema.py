# core/tests/schemas/test_booking_schema.py
import pytest
from core.domain.schemas.booking_schema import BookingSchema
from core.tests.factories.booking_factory import BookingFactory

@pytest.mark.django_db
def test_booking_schema_validation():
    booking = BookingFactory()
    schema = BookingSchema.model_validate(booking)
    assert schema.room.room_type == booking.room.room_type
    assert schema.room.capacity == booking.room.capacity

    if booking.user:
        assert schema.user.name == booking.user.name
        assert schema.user.age == booking.user.age
        assert schema.user.gender == booking.user.gender
    if booking.team:
        assert schema.team.name == booking.team.name
        assert len(schema.team.members) == booking.team.members.count()
