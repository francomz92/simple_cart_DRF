from rest_framework import pagination, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.products.models import MeasureUnit
from apps.products.serializers.secondary_serializers import MeasureUnitSerializer


class MeasureViewSet( viewsets.ModelViewSet):
   '''
      This class manages custom methods allowed to superusers.
      Objects -> MeasureUnit
   '''
   model = MeasureUnit
   serializer_class = MeasureUnitSerializer
   permission_classes = (IsAdminUser, )
   pagination_class = pagination.PageNumberPagination

   def get_queryset(self):
      if self.request.user.is_superuser:
         return self.model.objects.all()
      return Response({'message': 'You are not allowed to view this.'}, status=status.HTTP_403_FORBIDDEN)
