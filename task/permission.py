from rest_framework.permissions import BasePermission


class CreateTaskOnlyCustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.position == 'CUS'
