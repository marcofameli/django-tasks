def format_task_response(task):
    return {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'created_at': task.created_at,
        'updated_at': task.updated_at,
    }