from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import pagination, status, viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend

from apps.users.serializers.user_serializers import UserSerializer, UpdateUserSerializer
from core.permissions.owner_permission import IsOwnerOrAdmin
from apps.users.filters import IsOwnerFilter


class UserViewSet(viewsets.ModelViewSet):
   model = get_user_model()
   serializer_class = UserSerializer
   lookup_field = 'pk'
   permission_classes = (IsOwnerOrAdmin, )
   filter_backends = (filters.SearchFilter, DjangoFilterBackend)
   filterset_class = IsOwnerFilter
   search_fields = ('username', )
   pagination_class = pagination.PageNumberPagination

   def get_queryset(self):
      return self.model.objects.all()

   def get_serializer_class(self):
      if self.action == 'create':
         return self.serializer_class
      elif self.action == 'update':
         return UpdateUserSerializer
      return self.serializer_class

   def destroy(self, request, *args, **kwargs):
      user = self.get_object()
      user.is_active = False
      user.save()
      return Response({'message': 'User deleted'}, status=status.HTTP_200_OK)
