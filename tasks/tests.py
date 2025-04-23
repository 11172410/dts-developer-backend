from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

# Create your tests here.


class TaskListViewTests(APITestCase):
    def setUp(self):
        Task.objects.create(
            title="test title",
            description="test",
            status=False,
            due_date="2025-05-01",
            due_time="12:00",
        )

    def test_retrieve_list_of_tasks(self):
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
