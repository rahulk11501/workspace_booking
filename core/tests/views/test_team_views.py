import pytest
from rest_framework.test import APIClient
from core.tests.factories.team_factory import TeamFactory
from core.tests.factories.user_factory import UserFactory


@pytest.mark.django_db
class TestTeamViews:
    def setup_method(self):
        self.client = APIClient()
        self.url = "/api/v1/teams/"

    def test_list_teams(self):
        TeamFactory.create_batch(3)
        res = self.client.get(self.url)
        assert res.status_code == 200
        assert len(res.data) == 3

    def test_retrieve_team(self):
        team = TeamFactory.create()
        res = self.client.get(f"{self.url}{team.id}/")
        assert res.status_code == 200
        assert res.data["name"] == team.name
        assert isinstance(res.data["members"], list)

    @pytest.mark.parametrize("num_members", [0, 1, 2, 3])
    def test_create_team_with_various_members(self, num_members):
        users = UserFactory.create_batch(num_members)
        data = {
            "name": "Awesome Team",
            "members": [{"name": u.name, "age": u.age, "gender": u.gender} for u in users],
        }
        res = self.client.post(self.url, data, format="json")
        assert res.status_code == 201
        assert res.data["name"] == "Awesome Team"

    def test_update_team(self):
        team = TeamFactory.create()
        new_users = UserFactory.create_batch(2)
        data = {
            "name": "Updated Team",
            "members": [{"id": u.id, "name": u.name, "age": u.age, "gender": u.gender} for u in new_users],
        }
        res = self.client.put(f"{self.url}{team.id}/", data, format="json")
        assert res.status_code == 200
        assert res.data["name"] == "Updated Team"
        assert len(res.data["members"]) == 2

    def test_delete_team(self):
        team = TeamFactory.create()
        res = self.client.delete(f"{self.url}{team.id}/")
        assert res.status_code == 204
        # Confirm deletion
        res = self.client.get(f"{self.url}{team.id}/")
        assert res.status_code == 404
