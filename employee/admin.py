from django.contrib import admin

from employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email', 'phone_number', 'position']
