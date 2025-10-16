# core/tests/schemas/test_room_schema.py
import pytest
from core.domain.schemas.room_schema import RoomSchema
from core.tests.factories.room_factory import RoomFactory

@pytest.mark.django_db
def test_room_schema_validation():
    room = RoomFactory()
    schema = RoomSchema.model_validate(room)
    assert schema.room_type == room.room_type
    assert schema.capacity == room.capacity
