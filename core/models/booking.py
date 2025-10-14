# core/models/booking.py
from django.db import models
from .room import Room
from .user import User
from .team import Team

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    slot_start = models.DateTimeField()
    slot_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    model_config = {
        "from_attributes": True
    }

    def __str__(self):
        if self.user:
            return f"{self.user.name} - {self.room.room_type} ({self.slot_start})"
        if self.team:
            return f"{self.team.name} - {self.room.room_type} ({self.slot_start})"
        return f"Booking {self.id} - {self.room.room_type}"
