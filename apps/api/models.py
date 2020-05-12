from django.db import models
from multiselectfield import MultiSelectField
from apps.authentication.models import User


class Workout(models.Model):
    WorkoutCategory = [
        ('shoulders', 'shoulders'),
        ('arms', 'arms'),
        ('back', 'back'),
        ('chest', 'chest'),
        ('abs', 'abs'),
        ('legs', 'legs')
    ]

    Day = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday')
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=Day)
    workout = MultiSelectField(choices=WorkoutCategory)
    workout_routine = models.TextField()

    def __str__(self):
        return str(self.owner)
