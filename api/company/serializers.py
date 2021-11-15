from django.db.models import Sum
from rest_framework import serializers

from company.models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'photo',
            'position',
            'salary',
            'age',
            'department'
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField('get_employee_count')
    salary_sum = serializers.SerializerMethodField('get_salary_sum')

    def get_employee_count(self, department):
        return len(Employee.objects.filter(department_id=department.id))

    def get_salary_sum(self, department):
        return Employee.objects.filter(department_id=department.id).aggregate(Sum('salary'))['salary__sum']

    class Meta:
        model = Department
        fields = [
            'name',
            'employee_count',
            'salary_sum'
        ]
