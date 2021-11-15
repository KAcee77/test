from django_filters import rest_framework as filters
from project.paginations import CustomPageNumberPagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from company.models import Department, Employee

from .filters import EmployeeFilter
from .serializers import DepartmentSerializer, EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """ # Request_params: "last_name", "deprtment_id" """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EmployeeFilter
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination



class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = None
    http_method_names = ['get']
