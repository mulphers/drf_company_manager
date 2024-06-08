from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.models import Employee
from employee.serializers import EmployeeSerializers


class CreateEmployeeView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class GetCurrentUser(APIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = EmployeeSerializers

    def get(self, request):
        return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)
