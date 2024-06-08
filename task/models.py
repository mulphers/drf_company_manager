from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import ModelWithTime
from employee.models import Employee


class TaskStatus(models.TextChoices):
    waiting_executor = 'WAE', _('Waiting executor')
    in_process = 'INP', _('In process')
    realized = 'REL', _('Realized')


class Task(ModelWithTime):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    status = models.CharField(max_length=3, choices=TaskStatus.choices, default=TaskStatus.waiting_executor)
    customer = models.ForeignKey(
        to=Employee,
        on_delete=models.DO_NOTHING,
        related_name='customer_tasks'
    )
    executor = models.ForeignKey(
        to=Employee,
        on_delete=models.DO_NOTHING,
        null=True,
        default=None,
        related_name='executor_tasks'
    )
    closed_ad = models.DateTimeField(null=True)
    report = models.FileField(upload_to='report', null=True, blank=True)
