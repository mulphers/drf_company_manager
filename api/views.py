from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from task.models import Task
from task.permission import CreateTaskOnlyCustomerPermission
from task.serializers import TaskSerializers


class CreateTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
        CreateTaskOnlyCustomerPermission
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
        return Task.objects.filter(customer=self.request.user)
