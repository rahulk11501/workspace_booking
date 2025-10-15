# core/tests/factories/team_factory.py
import factory
from core.models.team import Team
from core.tests.factories.user_factory import UserFactory
from random import randint

class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team
        skip_postgeneration_save = True  # avoids deprecation warning

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
            for _ in range(randint(2, 5)):
                self.members.add(UserFactory())

        # explicitly save the instance to persist members
        self.save()
