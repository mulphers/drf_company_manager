from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from employee.models import Employee


class EmployeeSerializers(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        return super().create(validated_data)
