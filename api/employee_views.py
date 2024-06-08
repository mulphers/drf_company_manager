from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.serializers import EmployeeSerializers


class GetCurrentUser(APIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = EmployeeSerializers

    def get(self, request):
        return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)
