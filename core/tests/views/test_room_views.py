import pytest
from rest_framework.test import APIClient
from core.tests.factories.room_factory import RoomFactory

@pytest.mark.django_db
class TestRoomViews:
    def setup_method(self):
        self.client = APIClient()
        self.url = "/api/v1/rooms/"

    @pytest.mark.parametrize(
        "room_type,capacity,expect_status",
        [
            ("PRIVATE", 1, 201),    # valid
            ("PRIVATE", 2, 422),    # invalid for PRIVATE
            ("CONFERENCE", 3, 201), # valid min
            ("CONFERENCE", 2, 422), # invalid for CONFERENCE
            ("SHARED", 4, 201),     # valid max
            ("SHARED", 5, 422),     # invalid for SHARED
            ("SHARED", 0, 422),     # invalid capacity
        ],
    )
    def test_create_room_validations(self, room_type, capacity, expect_status):
        data = {"room_type": room_type, "capacity": capacity}
        res = self.client.post(self.url, data, format="json")
        assert res.status_code == expect_status

    def test_list_rooms(self):
        RoomFactory.create_batch(4)
        res = self.client.get(self.url)
        assert res.status_code == 200
        assert len(res.data) == 4

    def test_retrieve_room(self):
        room = RoomFactory.create()
        res = self.client.get(f"{self.url}{room.id}/")
        assert res.status_code == 200
        assert res.data["room_type"] == room.room_type
