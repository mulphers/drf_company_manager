from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from employee.permission import IsCustomer, IsExecutor
from task.permission import (IsExecutorOwner, IsNotRealizedTask,
                             IsTaskWithoutExecutor)
from task.serializers import TaskSerializers
from task.services import (assign_task, close_task, create_task, get_all_task,
                           get_assigned_task, set_customer_to_task,
                           update_task)


class CreateTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsCustomer,
    )
    serializer_class = TaskSerializers

    def post(self, request):
        data = set_customer_to_task(
            data=request.data.copy(),
            user=request.user
        )

        return create_task(serializer=self.serializer_class(data=data))


class GetTaskView(ListAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = TaskSerializers

    def get_queryset(self):
        return get_all_task(user=self.request.user)


class AssignTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsExecutor,
        IsTaskWithoutExecutor
    )
    serializer_class = TaskSerializers

    def post(self, request):
        return assign_task(
            task_id=request.data.get('task_id'),
            user=request.user,
            serializer_class=self.serializer_class
        )


class GetAssignedTaskView(ListAPIView):
    permission_classes = (
        IsAuthenticated,
        IsExecutor,
    )
    serializer_class = TaskSerializers

    def get_queryset(self):
        return get_assigned_task(user=self.request.user)


class UpdateTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsExecutor,
        IsExecutorOwner,
        IsNotRealizedTask,
    )
    serializer_class = TaskSerializers

    def post(self, request):
        return update_task(
            task_id=request.data['task_id'],
            report=request.data.get('report'),
            serializer_class=self.serializer_class
        )


class CloseTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsExecutor,
        IsExecutorOwner,
    )
    serializer_class = TaskSerializers

    def post(self, request):
        return close_task(
            task_id=request.data.get('task_id'),
            serializer_class=self.serializer_class
        )
