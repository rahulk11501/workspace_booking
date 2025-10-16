# core/tests/factories/room_factory.py
import factory
from core.models.room import Room
from faker import Faker

fake = Faker()

class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    room_type = factory.LazyFunction(lambda: fake.random_element(["PRIVATE", "CONFERENCE", "SHARED"]))

    @factory.lazy_attribute
    def capacity(self):
        if self.room_type == "PRIVATE":
            return 1
        elif self.room_type == "CONFERENCE":
            # Random between 3 and 8 members for conferences
            return fake.random_int(min=3, max=8)
        elif self.room_type == "SHARED":
            # Shared desks max 4 users
            return fake.random_int(min=1, max=4)
        return 1  # fallback
