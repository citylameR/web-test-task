from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return TaskUpdateSerializer
        return TaskSerializer

    @action(detail=True, methods=['post'])
    def process_task(self, request, pk=None):
        """Process the task"""
        task = self.get_object()
        task.status = 'in_progress'
        task.save()

        # run background task
        self.process_task.delay(task.id)

        return Response({'status': 'task processing started'})