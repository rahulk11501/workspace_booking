import pytest
from core.domain.schemas.user_schema import UserSchema
from core.tests.factories.user_factory import UserFactory

@pytest.mark.django_db
def test_user_schema_validation():
    user = UserFactory()
    schema = UserSchema.model_validate(user)
    assert schema.name == user.name
    assert schema.age == user.age
    assert schema.gender == user.gender