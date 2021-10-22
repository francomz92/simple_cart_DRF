from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response

from apps.orders.models import Order, OrderItem
from apps.orders.permissions import IsOwner
from apps.orders.serializers.order_item_serializers import OrderItemsSerializer


class OrderItemsViews(generics.ListCreateAPIView):
   serializer_class = OrderItemsSerializer
   permission_classes = (IsOwner, )

   def dispatch(self, request, *args, **kwargs):
      user = get_user_model().objects.filter(id=self.kwargs['pk']).first()
      self.order = Order.objects.filter(id=self.kwargs['order_pk'], user=user).first()
      return super().dispatch(request, *args, **kwargs)

   def get_queryset(self):
      return OrderItem.objects.filter(order=self.order)

   def post(self, request, *args, **kwargs):
      order = []
      for detail in request.data['details']:
         serializer = self.get_serializer(
             data={
                 'amount': detail['amount'],
                 'product': detail['product']['id'],
                 'price': detail['product']['price'],
             })
         if serializer.is_valid():
            serializer.save(order=self.order)
            order.append(serializer.data)
      return Response(order, status=status.HTTP_200_OK)
