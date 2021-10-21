from rest_framework.urls import path

from .views.cart_item_views import *

app_name = 'cart'

urlpatterns = [
    path('users/<pk>/cart/', CartItemCreateView.as_view(), name='cart'),
    path('users/<pk>/cart/item/<int:item_pk>/', CartItemUpdateView.as_view(), name='cart_update'),
]
