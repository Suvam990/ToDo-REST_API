from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task

class TaskListCreateView(APIView):
    def get(self, request):
        tasks_q = Task.objects.all()

        if tasks_q.exists():
            serializer = TaskSerializer(tasks_q, many=True)
            return Response({"message": "Tasks retrieved successfully", "data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "No tasks found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task created successfully", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({"message": "Task creation failed", "errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    
class TaskDetailView(APIView):
    # GET task by title
    def get(self, request, title):
        task = Task.objects.filter(title=title)
        
        if task.exists():
            serializer = TaskSerializer(task, many=True)
            return Response({"message": "Task(s) retrieved successfully", "data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "No task found with the provided title"}, status=status.HTTP_404_NOT_FOUND)

    # DELETE task by title
    def delete(self, request, title):
        task = Task.objects.filter(title=title)
        
        if task.exists():
            task.delete()
            return Response({"message": "Task(s) deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "No task found with the provided title to delete"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, title):
        task_qs = Task.objects.filter(title=title)

        if task_qs.exists():
            task = task_qs.first()  # Get the first matching task
            serializer = TaskSerializer(task, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Task updated successfully", "data": serializer.data},
                                status=status.HTTP_200_OK)
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "No task found with the provided title to update"},
                        status=status.HTTP_404_NOT_FOUND)
