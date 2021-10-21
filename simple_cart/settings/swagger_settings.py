from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Ecommerce API',
        default_version='v0.1',
        description='Silmpe Ecommerce API created by Franco',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='mi@email.com'),
        license=openapi.License(name='OpenAPI License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none',
}