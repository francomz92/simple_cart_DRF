from django.db.models.query import Prefetch

from rest_framework.response import Response
from rest_framework import viewsets, status, pagination

from apps.products.models import Product
from apps.products.serializers.product_serializers import *
from apps.products.service.product_service import ProductService


class ProductViewSet(viewsets.ModelViewSet):
   '''
      This class manages custom Methods for retrieving information about a product.
      Objects -> Products
   '''
   model = Product
   serializer_class = ProductSerializer
   pagination_class = pagination.PageNumberPagination

   def get_queryset(self):
      '''
         Get the queryset of the products. If the user is super user, return all products, otherwise return only the products that have state set to True.
      '''
      user = self.request.user
      if user.is_active and user.is_staff and user.is_superuser:
         return self.model.objects.all().prefetch_related(Prefetch('category'), Prefetch('measure_unit'))
      return self.model.objects.filter(state=True).prefetch_related(Prefetch('category'),
                                                                    Prefetch('measure_unit'))

   def create(self, request, *args, **kwargs):
      '''
         Create a new product object only if the user is a super user.
      '''
      user = self.request.user
      if user.is_active and user.is_staff and user.is_superuser:
         return super().create(request, *args, **kwargs)
      return Response({'message': 'You are not allowed to create'}, status=status.HTTP_403_FORBIDDEN)

   def update(self, request, *args, **kwargs):
      '''
         Update an existing product object only if the user is a super user.
      '''
      user = self.request.user
      if user.is_active and user.is_staff and user.is_superuser:
         return super().update(request, *args, **kwargs)
      return Response({'message': 'You are not allowed to create'}, status=status.HTTP_403_FORBIDDEN)

   def destroy(self, request, *args, **kwargs):
      '''
         Change the status of an existing product object to False only if the user is a super user.
      '''
      user = self.request.user
      if user.is_active and user.is_staff and user.is_superuser:
         product = self.get_queryset().first()
         if product:
            ProductService.product_disabling(product)
            return Response({'message': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)
         return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
      return Response({'message': 'You are not allowed to delete'}, status=status.HTTP_403_FORBIDDEN)
