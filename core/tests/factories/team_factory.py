# core/tests/factories/team_factory.py
import factory
from core.models.team import Team
from core.tests.factories.user_factory import UserFactory

class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.Faker("company")

    @factory.post_generation
    def members(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for user in extracted:
                self.members.add(user)
        else:
            # add 2–5 random users if none passed
            from random import randint
            for _ in range(randint(2, 5)):
                self.members.add(UserFactory())
