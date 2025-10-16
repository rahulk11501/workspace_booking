import pytest
from rest_framework.test import APIClient
from core.tests.factories.user_factory import UserFactory

@pytest.mark.django_db
class TestUserViews:
    def setup_method(self):
        self.client = APIClient()
        self.url = "/api/v1/users/"

    @pytest.mark.parametrize(
        "age,gender,expect_status",
        [
            (25, "Male", 201),
            (32, "Female", 201),
            (-5, "Male", 422),
            (40, "Unknown", 422),
        ],
    )
    def test_create_user_validations(self, age, gender, expect_status):
        payload = {"name": "John Doe", "age": age, "gender": gender}
        res = self.client.post(self.url, payload, format="json")
        assert res.status_code == expect_status

    def test_list_users(self):
        UserFactory.create_batch(5)
        res = self.client.get(self.url)
        assert res.status_code == 200
        assert len(res.data) == 5

    def test_retrieve_update_delete_user(self):
        user = UserFactory.create()
        detail_url = f"{self.url}{user.id}/"

        res = self.client.get(detail_url)
        assert res.status_code == 200

        update_data = {"name": "Updated", "age": user.age, "gender": user.gender}
        res = self.client.put(detail_url, update_data, format="json")
        assert res.status_code == 200
        assert res.data["name"] == "Updated"

        res = self.client.delete(detail_url)
        assert res.status_code == 204
