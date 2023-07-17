from django.test import TestCase
from app.models import Task


class TaskTestCase(TestCase):

    def test_task_creation(self):
        """Test task creation"""
        task = Task.objects.create(number=1, status='new')
        self.assertEqual(task.number, 1)
        self.assertEqual(task.status, 'new')

    def test_task_update(self):
        """Test task update"""
        task = Task.objects.create(number=1, status='new')
        task.status = 'in_progress'
        task.save()
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.status, 'in_progress')

    def test_task_delete(self):
        """Test task delete"""
        task = Task.objects.create(number=1)
        self.assertEqual(Task.objects.count(), 1)

        task.delete()
        self.assertEqual(Task.objects.count(), 0)