# core/tests/models/test_booking_model.py
import pytest
from core.tests.factories.booking_factory import BookingFactory

@pytest.mark.django_db
def test_booking_creation():
    booking = BookingFactory()
    assert booking.id is not None
    assert booking.room
    assert booking.user or booking.team
    assert booking.slot_end > booking.slot_start
