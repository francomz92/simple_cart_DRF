from rest_framework import pagination, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.products.models import ProductCategory
from apps.products.serializers.product_category_serializer import ProductCategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
   '''
      This class manages custom methods allowed to superusers.
      Objects -> ProductCategory
   '''
   model = ProductCategory
   serializer_class = ProductCategorySerializer
   permission_classes = (IsAdminUser, )
   pagination_class = pagination.PageNumberPagination

   def get_queryset(self):
      if self.request.user.is_superuser:
         return self.model.objects.all()
      return Response({'message': 'You are not allowed to view this.'}, status=status.HTTP_403_FORBIDDEN)