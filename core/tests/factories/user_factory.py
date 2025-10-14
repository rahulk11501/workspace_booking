import factory
from faker import Faker
from core.models.user import User

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.LazyFunction(fake.name)
    age = factory.LazyFunction(lambda: fake.random_int(min=18, max=65))
    gender = factory.LazyFunction(lambda: fake.random_element(elements=["Male", "Female"]))
