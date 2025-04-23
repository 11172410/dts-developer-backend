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
        """Tests if a list of all tasks can be retrieved"""
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_task(self):
        """Tests if new task can be created"""
        response = self.client.post(
            "/tasks/",
            {
                "title": "test task",
                "description": "test",
                "due_date": "2025-05-01",
                "due_time": "12:00",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_task_without_description(self):
        """Tests if a new task can be created without a description as description is set as optional."""

        response = self.client.post(
            "/tasks/",
            {
                "title": "test task",
                "due_date": "2025-05-01",
                "due_time": "12:00",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["description"], "")

    def test_create_task_with_missing_required_fields(self):
        """Tests that a task will not be created if a required field is missing."""

        response = self.client.post(
            "/tasks/",
            {
                "due_date": "2025-05-01",
                "due_time": "12:00",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_task_set_in_the_past(self):
        """Tests that a task will not be created if user tries to set task in the past"""

        response = self.client.post(
            "/tasks/",
            {
                "title": "test task",
                "due_date": "2025-04-20",
                "due_time": "12:00",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TaskDetailViewTests(APITestCase):
    def setUp(self):
        Task.objects.create(
            title="test title",
            description="test",
            status=False,
            due_date="2025-05-01",
            due_time="12:00",
        )

    def test_retrieve_task_by_id(self):
        """Tests if a single task can be retrieved by id."""

        response = self.client.get("/tasks/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_non_existent_task(self):
        """Tests that a non-existent task will not be retrieved."""

        response = self.client.get("/tasks/2/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_task(self):
        """Tests if a task can be updated."""

        response = self.client.patch("/tasks/1/", {"title":"new title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_non_existent_task(self):
        """Tests updating a non-existent task."""

        response = self.client.patch("/tasks/2/", {"title":"test title"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_delete_task(self):
        """Tests that a task can be deleted successfully"""

        response = self.client.delete("/tasks/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_non_existent_task(self):
        """Tests that a non-existent task cannot be deleted."""

        response = self.client.delete("/tasks/2/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)