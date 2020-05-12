from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Workout
        fields = ('id', 'created_at', 'owner', 'day', 'workout', 'workout_routine')