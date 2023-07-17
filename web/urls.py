from django.contrib import admin
from django.urls import path, include



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tasks API",
        default_version='v1',
        description="Test assignment project API",
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticatedOrReadOnly],
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('api/docs/json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('api/docs/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('api/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]