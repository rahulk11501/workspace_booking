import pytest
from core.tests.factories.user_factory import UserFactory

@pytest.mark.django_db
def test_user_creation():
    user = UserFactory()
    assert user.id is not None
    assert user.name