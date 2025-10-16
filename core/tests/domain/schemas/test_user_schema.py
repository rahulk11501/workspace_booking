import pytest
from core.domain.schemas.user_schema import UserSchema
from core.tests.factories.user_factory import UserFactory

@pytest.mark.parametrize("age,gender,expect_error", [
    (-1, "Male", True),
    (25, "Xe/Xim", True),
    (30, "Female", False),
])
def test_user_schema_validation(age, gender, expect_error):
    user = UserFactory.build(age=age, gender=gender)
    data = {"name": user.name, "age": user.age, "gender": user.gender}
    if expect_error:
        with pytest.raises(ValueError):
            UserSchema.model_validate(data)
    else:
        validated = UserSchema.model_validate(data)
        assert validated.age == data["age"]
        assert validated.gender == data["gender"]
