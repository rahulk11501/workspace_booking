# core/tests/factories/booking_factory.py
import factory
from core.models.booking import Booking
from core.tests.factories.room_factory import RoomFactory
from core.tests.factories.user_factory import UserFactory
from core.tests.factories.team_factory import TeamFactory
from datetime import datetime, timedelta

class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    room = factory.SubFactory(RoomFactory)
    slot_start = factory.LazyFunction(lambda: datetime.now())
    slot_end = factory.LazyAttribute(lambda obj: obj.slot_start + timedelta(hours=1))

    @factory.lazy_attribute
    def user(self):
        if self.room.room_type == "PRIVATE" or self.room.room_type == "SHARED":
            return UserFactory()
        return None

    @factory.lazy_attribute
    def team(self):
        if self.room.room_type == "CONFERENCE":
            return TeamFactory()
        return None
