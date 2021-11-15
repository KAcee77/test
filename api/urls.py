from django.urls import include, path
from rest_framework import routers

from .company.views import DepartmentViewSet, EmployeeViewSet

router = routers.DefaultRouter()

router.register(r'employers', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
