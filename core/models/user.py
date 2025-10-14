# core/models/user.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)

    model_config = {
        "from_attributes": True
    }
    
    def __str__(self):
        return f"{self.name} ({self.age}, {self.gender})"
