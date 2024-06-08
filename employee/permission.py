from rest_framework.permissions import BasePermission

from employee.models import EmployeePosition


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.position == 'CUS'


class HasPosition(BasePermission):
    def has_permission(self, request, view):
        return request.user.position in map(lambda obj: obj[0], EmployeePosition.choices)
