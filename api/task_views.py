from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.permission import HasPosition, IsCustomer, IsExecutor
from task.models import Task, TaskStatus
from task.permission import IsExecutorOwner, IsNotRealizedTask
from task.serializers import TaskSerializers


class CreateTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsCustomer,
    )
    serializer_class = TaskSerializers

    def post(self, request):
        data = request.data.copy()
        data['customer'] = request.user.id

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTaskView(ListAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = TaskSerializers

    def get_queryset(self):
        if self.request.user.access_to_all_tasks:
            return Task.objects.all()

        elif self.request.user.position == 'CUS':
            return Task.objects.filter(customer=self.request.user)

        elif self.request.user.position == 'EXC':
            return Task.objects.filter(executor=None)

        return []


class AssignTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsExecutor,
    )
    serializer_class = TaskSerializers

    def post(self, request):
        # TODO: Transfer business logic to another module

        try:
            task = Task.objects.get(pk=request.data['task_id'])
        except ObjectDoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        if task.executor is not None:
            return Response({"error": "Task is already assigned"}, status=status.HTTP_400_BAD_REQUEST)

        task.executor = request.user
        task.status = TaskStatus.in_process
        task.save()

        return Response(self.serializer_class(task).data, status=status.HTTP_200_OK)


class GetAssignedTaskView(ListAPIView):
    permission_classes = (
        IsAuthenticated,
        IsExecutor,
    )
    serializer_class = TaskSerializers

    def get_queryset(self):
        return Task.objects.filter(executor=self.request.user)


class UpdateTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsExecutor,
        IsExecutorOwner,
        IsNotRealizedTask,
    )
    serializer_class = TaskSerializers

    def post(self, request):
        # TODO: Transfer business logic to another module

        try:
            task = Task.objects.get(pk=request.data['task_id'])
        except ObjectDoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        if report := request.data.get('report'):
            task.report = report

        task.save()

        return Response(self.serializer_class(task).data, status=status.HTTP_200_OK)


class CloseTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsExecutor,
        IsExecutorOwner,
    )
    serializer_class = TaskSerializers

    def post(self, request):
        # TODO: Transfer business logic to another module

        try:
            task = Task.objects.get(pk=request.data['task_id'])
        except ObjectDoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        if not task.report:
            return Response(
                {"error": "When closing a task, it must contain a report"},
                status=status.HTTP_400_BAD_REQUEST
            )

        task.status = 'REL'
        task.closed_ad = timezone.now()

        task.save()

        return Response(self.serializer_class(task).data, status=status.HTTP_200_OK)
