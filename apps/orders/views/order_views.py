from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response

from apps.orders.models import Order, OrderItem
from apps.orders.permissions import IsOwner
from apps.orders.serializers.order_item_serializers import OrderItemsSerializer
from apps.orders.serializers.order_serializers import OrdersSerializer


class OrdersView(generics.ListCreateAPIView):
   serializer_class = OrdersSerializer
   permission_classes = (IsOwner, )

   def dispatch(self, request, *args, **kwargs):
      self.user = get_user_model().objects.filter(id=kwargs['pk']).first()
      if self.user is None:
         return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
      return super().dispatch(request, *args, **kwargs)

   def get_queryset(self):
      return Order.objects.prefetch_related('order_items').filter(user=self.user)

   def get(self, request, *args, **kwargs):
      orders = []
      for order in self.get_queryset():
         serializer = self.get_serializer(order)
         data = serializer.data
         data['items'] = OrderItemsSerializer(OrderItem.objects.filter(order=order), many=True).data
         orders.append(data)
      return Response(orders, status=status.HTTP_200_OK)

   def perform_create(self, serializer):
      serializer.save(user=self.user)


class OrderRetrieveView(generics.RetrieveAPIView):
   serializer_class = OrdersSerializer
   permission_classes = (IsOwner, )

   def get_object(self):
      user = get_user_model().objects.filter(id=self.kwargs['pk']).first()
      if user is None:
         return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
      order = Order.objects.prefetch_related('order_items').filter(id=self.kwargs['order_id'],
                                                                   user=user).first()
      if order is None:
         return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
      return order

   def get(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      data = serializer.data
      data['items'] = OrderItemsSerializer(OrderItem.objects.filter(order=instance), many=True).data
      return Response(data, status=status.HTTP_200_OK)
