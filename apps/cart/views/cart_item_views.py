from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response

from apps.cart.models import Cart, CartItem
from apps.cart.serializers.cart_item_serializers import CartItemSerilizer, CartItemUpdateSerializer
from apps.cart.permissions import IsOwnerCustomer
from apps.users.serializers.user_serializers import UserSerializer


class CartItemCreateView(generics.ListCreateAPIView):
   serializer_class = CartItemSerilizer
   permission_classes = (IsOwnerCustomer, )

   def dispatch(self, request, *args, **kwargs):
      user = get_user_model().objects.filter(id=self.kwargs['pk']).first()
      self.cart = Cart.objects.prefetch_related('cart').filter(user=user).first()
      return super().dispatch(request, *args, **kwargs)

   def get_queryset(self):
      return CartItem.objects.filter(cart=self.cart)

   def get(self, request, *args, **kwargs):
      serializer = self.get_serializer(self.get_queryset(), many=True)
      return Response(
          {
              'details': serializer.data,
              'user': UserSerializer(self.cart.user).data,
          },
          status=status.HTTP_200_OK,
      )

   def post(self, request, *args, **kwargs):
      data, existent_item = self._clean_request_data(request)
      if data:
         return super().create(request, *args, **kwargs)
      return Response(self.get_serializer(existent_item).data, status=status.HTTP_200_OK)

   def perform_create(self, serializer):
      serializer.save(cart=self.cart, amount=1)

   def _clean_request_data(self, request):
      ''' Increase item amount if exists in cart '''
      data = request.data.copy()
      existent_item = self.get_queryset().filter(product=data['product']).first()
      if existent_item is not None and int(data['product']) == existent_item.product.id:
         existent_item.amount += 1
         existent_item.save()
         data = None
      return data, existent_item


class CartItemUpdateView(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = CartItemUpdateSerializer
   permission_classes = (IsOwnerCustomer, )

   def dispatch(self, request, *args, **kwargs):
      user = get_user_model().objects.filter(id=self.kwargs['pk']).first()
      self.cart = Cart.objects.filter(user=user).first()
      return super().dispatch(request, *args, **kwargs)

   def get_object(self):
      return CartItem.objects.filter(id=self.kwargs['item_pk'], cart=self.cart).first()

   def get(self, request, *args, **kwargs):
      if self.get_object():
         return super().retrieve(request, *args, **kwargs)
      return Response({'message': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)

   def put(self, request, *args, **kwargs):
      data = self._clean_request_data(request)
      if data:
         return super().update(request, *args, **kwargs)
      return Response({'message': 'Item eliminated'}, status=status.HTTP_200_OK)

   def _clean_request_data(self, request):
      ''' Delete item if their amount is less than or equal to 0 '''
      if int(request.data['amount']) < 1:
         self.delete(request)
         return None
      return True
