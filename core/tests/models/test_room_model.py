# core/tests/models/test_room_model.py
import pytest
from core.tests.factories.room_factory import RoomFactory

@pytest.mark.django_db
def test_room_creation():
    room = RoomFactory()
    assert room.id is not None
    assert room.room_type in ["PRIVATE", "CONFERENCE", "SHARED"]
    assert room.capacity > 0
