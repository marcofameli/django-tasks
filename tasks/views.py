from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services.task_service import TaskService
from .utils.task_utils import format_task_response
from .serializers import TaskSerializer

class TaskListCreateView(APIView):
    def get(self, request):
        tasks = TaskService.get_all_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = TaskService.create_task(serializer.validated_data)
            return Response(format_task_response(task), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskRetrieveUpdateDestroyView(APIView):
    def get(self, request, task_id):
        task = TaskService.get_task_by_id(task_id)
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, task_id):
        task = TaskService.get_task_by_id(task_id)
        if task:
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                updated_task = TaskService.update_task(task, serializer.validated_data)
                return Response(format_task_response(updated_task))
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, task_id):
        task = TaskService.get_task_by_id(task_id)
        if task:
            TaskService.delete_task(task)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)