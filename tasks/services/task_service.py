from ..models import Task

class TaskService:
    @staticmethod
    def get_all_tasks():
        return Task.objects.all()

    @staticmethod
    def get_task_by_id(task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None

    @staticmethod
    def create_task(task_data):
        return Task.objects.create(**task_data)

    @staticmethod
    def update_task(task, task_data):
        for key, value in task_data.items():
            setattr(task, key, value)
        task.save()
        return task

    @staticmethod
    def delete_task(task):
        task.delete()