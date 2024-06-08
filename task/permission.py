from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission

from task.models import Task, TaskStatus


class IsExecutorOwner(BasePermission):
    def has_permission(self, request, view):
        try:
            return Task.objects.get(pk=request.data.get('task_id')).executor == request.user
        except ObjectDoesNotExist:
            return False


class IsNotRealizedTask(BasePermission):
    def has_permission(self, request, view):
        try:
            return Task.objects.get(pk=request.data.get('task_id')).status != TaskStatus.realized
        except ObjectDoesNotExist:
            return False
