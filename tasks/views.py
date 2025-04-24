from rest_framework import generics
from .models import Task
from .serializers import TaskListSerializer, TaskDetailSerializer

# Create your views here.


class TaskList(generics.ListCreateAPIView):
    """
    Generic view for task list, where all tasks are retrieved as a list.
    Tasks can also be created with this API endpoint.
    """

    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view to allow individual tasks to be retrieved,
    updated and deleted by their id.
    """

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
