from django.test import TestCase

# TODO: Manual tests for now, will add automated tests later

from core.models.user import User
from core.domain.schemas.user_schema import UserSchema

u = User.objects.create(**dict(name="Rahul", age=28, gender="Male"))
user_schema = UserSchema.model_validate(u)
print(user_schema.model_dump_json())

