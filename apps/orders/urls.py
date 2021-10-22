from django.urls import path

from apps.orders.views.order_views import *
from apps.orders.views.order_item_views import *

app_name = 'orders'

urlpatterns = [
    path('users/<pk>/orders/', OrdersView.as_view(), name='orders'),
    path('users/<pk>/orders/<int:order_id>/', OrderRetrieveView.as_view(), name='orders_id'),
    path('users/<pk>/orders/<int:order_pk>/items/', OrderItemsViews.as_view(), name='order_items'),
]
