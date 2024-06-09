from rest_framework.permissions import BasePermission

from employee.models import EmployeePosition


class IsExecutor(BasePermission):
    def has_permission(self, request, view):
        return request.user.position == 'EXC'


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.position == 'CUS'
