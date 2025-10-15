from django.core.management.base import BaseCommand
from core.models.user import User
from core.models.team import Team
from core.models.room import Room
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed initial data for users, teams, rooms, and bookings"

    def handle(self, *args, **options):
        # --- Users ---
        users = []
        for _ in range(20):
            user = User.objects.create(
                name=fake.name(),
                age=random.randint(5, 60),
                gender=random.choice(['Male', 'Female', 'Other'])
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f"Created {len(users)} users."))

        # --- Teams ---
        teams = []
        for i in range(5):
            team = Team.objects.create(name=f"Team {i+1}")
            members = random.sample(users, k=random.randint(3, 5))
            team.members.set(members)
            teams.append(team)
        self.stdout.write(self.style.SUCCESS(f"Created {len(teams)} teams."))

        # --- Rooms ---
        # Private Rooms
        for i in range(8):
            Room.objects.create(room_type="Private", capacity=1)
        # Conference Rooms
        for i in range(4):
            Room.objects.create(room_type="Conference", capacity=10)
        # Shared Desks
        for i in range(3):
            Room.objects.create(room_type="Shared", capacity=4)
        self.stdout.write(self.style.SUCCESS("Created all rooms."))

        # --- Optional: Bookings ---
        # You can create some initial bookings if desired
        # for example, assign first user to first private room at 9 AM
        self.stdout.write(self.style.SUCCESS("Seed data completed successfully."))
