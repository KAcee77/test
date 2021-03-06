import django_filters
from company.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    department_id = django_filters.CharFilter(lookup_expr='exact', required=False)
    last_name = django_filters.CharFilter(lookup_expr='iexact', required=False)

    class Meta:
        model = Employee
        fields = [
            'department_id',
            'last_name',
        ]
       