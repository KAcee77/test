from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('chg/api/auth/', include('social_django.urls', namespace='social')),
    path('project/api/', include('api.urls')),
    # path('chg/project/', include('company.urls')),
    path('project/api/openapi', get_schema_view(
            title="К школе готов",
            description="API для frontend",
            version="1.0.0"
        ), name='openapi-schema'),
    path('project/api/swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
