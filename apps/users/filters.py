from django.contrib.auth import get_user_model

from django_filters.rest_framework import FilterSet


class IsOwnerFilter(FilterSet):
   class Meta:
      model = get_user_model()
      fields = {
          'username': ['icontains'],
          'email': ['icontains'],
      }
