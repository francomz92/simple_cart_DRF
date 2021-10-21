from django.contrib import admin
from django.urls import path, include, re_path

from django.conf.urls.static import static
from django.conf import settings

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views.authentication import LogIn, LogOut

from .settings.swagger_settings import schema_view

swagger_urls = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

drf_urls = [
    path('admin/', admin.site.urls),
    #  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #  path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', LogIn.as_view(), name='login'),
    path('api/logout/', LogOut.as_view(), name='logout'),
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.products.urls')),
    path('api/', include('apps.cart.urls')),
]

urlpatterns = swagger_urls + drf_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)