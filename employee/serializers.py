from rest_framework.serializers import ModelSerializer

from employee.models import Employee


class EmployeeSerializers(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
