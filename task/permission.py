from rest_framework.permissions import BasePermission

from task.models import Task


class IsExecutorOwner(BasePermission):
    def has_permission(self, request, view):
        return Task.objects.get(pk=request.data.get('task_id')).executor == request.user
