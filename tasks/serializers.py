from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    # Give human-readable date format for task
    due_date = serializers.DateField(format="%Y-%m-%d")
    # Give human-readable time format for task
    due_time = serializers.TimeField(format="%H:%M")

    # Ensure task title is always capitalised regardless of human input
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["title"] = rep["title"].capitalize()
        return rep

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "due_date", "due_time"]
