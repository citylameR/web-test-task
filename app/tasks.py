import time

from rq import get_current_job

from app.models import Task


def process_task(task_id):
    job = get_current_job()

    task = Task.objects.get(id=task_id)
    task.status = 'in_progress'
    task.save()

    # имитация выполнения задачи
    time.sleep(5)

    task.status = 'completed'
    task.save()

    return {'task_id': task.id, 'status': task.status}


def clean_old_tasks():
    old_tasks = Task.objects.filter(status='completed')
    old_tasks.delete()
