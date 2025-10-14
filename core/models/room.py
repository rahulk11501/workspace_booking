# core/models/room.py
from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ("PRIVATE", "Private Room"),
        ("CONFERENCE", "Conference Room"),
        ("SHARED", "Shared Desk"),
    ]
    
    room_type = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()

    model_config = {
        "from_attributes": True
    }

    def __str__(self):
        return f"{self.room_type} ({self.capacity})"
