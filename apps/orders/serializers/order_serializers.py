from rest_framework import serializers

from apps.orders.models import Order
from apps.users.serializers.user_serializers import UserSerializer


class OrdersSerializer(serializers.ModelSerializer):
   class Meta:
      model = Order
      fields = '__all__'
      read_only_fields = ['created_date', 'user']

   def to_representation(self, instance):
      data = super().to_representation(instance)
      data['user'] = UserSerializer(instance.user).data
      return data