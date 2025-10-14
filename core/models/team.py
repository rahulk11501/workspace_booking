# core/models/team.py
from django.db import models
from .user import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="teams")

    model_config = {
        "from_attributes": True
    }

    def __str__(self):
        return f"{self.name} ({self.members.count()} members)"
