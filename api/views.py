from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from task.serializers import CreateTaskSerializers


class CreateTaskView(APIView):
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = CreateTaskSerializers

    def post(self, request):
        data = request.data.copy()
        data['customer'] = request.user.id

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
