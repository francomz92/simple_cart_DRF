from django.contrib import admin

from apps.cart.models import Cart, CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
   list_display = ['id', 'cart', 'product', 'amount', 'partial_price']
   list_display_links = None
   ordering = ['-id']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
   list_display = ['id', 'user']
   ordering = ['id']