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
            # Add 0–3 random users (team can exist without members)
            for _ in range(randint(0, 3)):
                self.members.add(UserFactory())

        self.save()
