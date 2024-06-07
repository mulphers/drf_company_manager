from django.db import models

from base.models import ModelWithTime
from employee.models import Employee


class Task(ModelWithTime):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    customer = models.ForeignKey(
        to=Employee,
        on_delete=models.DO_NOTHING,
        null=True,
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
