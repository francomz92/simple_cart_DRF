from rest_framework import serializers

from apps.orders.models import OrderItem
from apps.products.serializers.product_serializers import ProductSerializer


class OrderItemsSerializer(serializers.ModelSerializer):
   class Meta:
      model = OrderItem
      exclude = ['order']

   def to_representation(self, instance):
      data = super().to_representation(instance)
      data['product'] = ProductSerializer(instance.product).data
      return data
