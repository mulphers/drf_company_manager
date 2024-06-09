from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response

from task.models import Task, TaskStatus


def _find_task(task_id):
    try:
        return Task.objects.get(pk=task_id)
    except ObjectDoesNotExist:
        return None


def set_customer_to_task(data, user):
    data['customer'] = user.id

    return data


def create_task(serializer):
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_task(task_id, report, serializer_class):
    task = _find_task(task_id=task_id)

    if task is None:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    if report:
        task.report = report

    task.save()

    return Response(serializer_class(task).data, status=status.HTTP_200_OK)


def close_task(task_id, serializer_class):
    task = _find_task(task_id=task_id)

    if task is None:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    if not task.report:
        return Response(
            {"error": "When closing a task, it must contain a report"},
            status=status.HTTP_400_BAD_REQUEST
        )

    task.status = TaskStatus.realized
    task.closed_ad = timezone.now()

    task.save()

    return Response(serializer_class(task).data, status=status.HTTP_200_OK)


def assign_task(task_id, user, serializer_class):
    task = _find_task(task_id=task_id)

    if task is None:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    task.executor = user
    task.status = TaskStatus.in_process
    task.save()

    return Response(serializer_class(task).data, status=status.HTTP_200_OK)


def get_all_task(user):
    if user.access_to_all_tasks:
        return Task.objects.all()

    elif user.position == 'CUS':
        return Task.objects.filter(customer=user)

    elif user.position == 'EXC':
        return Task.objects.filter(executor=None)

    return []


def get_assigned_task(user):
    return Task.objects.filter(executor=user)
