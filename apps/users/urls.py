from django.urls.conf import path
from rest_framework.routers import DefaultRouter

from apps.users.views.registration import ActivationAccount, RegistrationView

from .views.user_views import *

app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

reqgister_urls = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('account-acvtivation/<slug:uid64>/<slug:token>/',
         ActivationAccount.as_view(),
         name='account_activation')
]

urlpatterns = router.urls + reqgister_urls