from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from base.models import ModelWithTime


class EmployeePosition(models.TextChoices):
    executor = 'EXC', _('Executor')
    customer = 'CUS', _('Customer')


class Employee(AbstractUser, ModelWithTime):
    email = models.EmailField(_("email_address"), null=False)
    phone_number = PhoneNumberField()
    position = models.CharField(max_length=3, choices=EmployeePosition.choices, null=True, default=None)
    access_to_all_tasks = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
