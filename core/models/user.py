# core/models/user.py
from django.db import models

class User(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    model_config = {
        "from_attributes": True
    }
    
    def __str__(self):
        return f"{self.name} ({self.age}, {self.gender})"
