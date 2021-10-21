from rest_framework import serializers

from apps.cart.models import CartItem
from apps.products.serializers.product_serializers import ProductSerializer
from apps.users.serializers.user_serializers import UserSerializer


class CartItemSerilizer(serializers.ModelSerializer):
   class Meta:
      model = CartItem
      exclude = ['cart']
      extra_kwargs = {
          'amount': {
              'read_only': True,
          }
      }

   def to_representation(self, instance):
      data = super().to_representation(instance)
      data['product'] = ProductSerializer(instance.product).data
      data['partial_price'] = instance.partial_price
      return data


class CartItemUpdateSerializer(CartItemSerilizer):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.Meta.extra_kwargs = {
          'product': {
              'read_only': True,
          }
      }
