from django.contrib import admin

from .models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ('last_name', 'department__id')

admin.site.register(Department)
