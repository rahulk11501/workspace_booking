import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.tests.factories.user_factory import UserFactory

@pytest.mark.django_db
@pytest.mark.parametrize("num_users", [1, 3, 5])
def test_user_list_api_with_factory(num_users):
    UserFactory.create_batch(num_users)
    client = APIClient()

    response = client.get(reverse("user-list-create"))
    assert response.status_code == 200
    assert len(response.data) >= num_users

@pytest.mark.django_db
def test_user_create_api():
    client = APIClient()
    payload = {"name": "Alice", "age": 25, "gender": "Female"}
    response = client.post(reverse("user-list-create"), payload, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "Alice"
