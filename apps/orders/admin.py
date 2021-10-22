from django.contrib import admin

from apps.orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
   list_display = ['id', 'user', 'created_date']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
   list_display = ['id', 'product', 'amount', 'partial_price']