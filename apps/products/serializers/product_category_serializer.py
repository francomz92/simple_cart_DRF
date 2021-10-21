from rest_framework import serializers

from apps.products.models import ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = ProductCategory
      exclude = [
          'state',
          'created_date',
          'modified_date',
          'deleted_date',
      ]
