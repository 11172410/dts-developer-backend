from datetime import date
from rest_framework import serializers
from .models import Task


class TaskListSerializer(serializers.ModelSerializer):

    status = serializers.ReadOnlyField()
    # Give human-readable date format for task
    due_date = serializers.DateField(format="%Y-%m-%d")
    # Give human-readable time format for task
    due_time = serializers.TimeField(format="%H:%M")

    # Ensure task title is always capitalised regardless of human input
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["title"] = rep["title"].capitalize()
        return rep

    def validate_due_date(self, value):
        """
        Prevents tasks from being set in the past by comparing
        the value of the task with the current date.
        """
        today = date.today()
        if value < today:
            raise serializers.ValidationError(
                "Tasks cannot be set in the past.")
        return value

    class Meta:
        model = Task
        fields = ["id", "title", "description",
                  "status", "due_date", "due_time"]


class TaskDetailSerializer(serializers.ModelSerializer):
    # Give human-readable date format for task
    due_date = serializers.DateField(format="%Y-%m-%d")
    # Give human-readable time format for task
    due_time = serializers.TimeField(format="%H:%M")

    class Meta:
        model = Task
        fields = ["id", "title", "description",
                  "status", "due_date", "due_time"]
