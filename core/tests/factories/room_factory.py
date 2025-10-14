# core/tests/factories/room_factory.py
import factory
from core.models.room import Room
from faker import Faker

fake = Faker()

class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    room_type = factory.LazyFunction(lambda: fake.random_element(["PRIVATE", "CONFERENCE", "SHARED"]))
    capacity = factory.LazyAttribute(lambda o: 1 if o.room_type == "PRIVATE" else (4 if o.room_type == "SHARED" else 10))
