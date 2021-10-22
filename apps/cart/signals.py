from typing import List

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from apps.cart.models import Cart, CartItem
from apps.orders.models import OrderItem


@receiver(post_save, sender=get_user_model())
def create_cart_for_user(sender, instance, created, **kwargs):
   if created:
      Cart.objects.create(user=instance)


@receiver(post_save, sender=OrderItem)
def delete_cart_item(sender, instance, created, **kwargs):
   if created:
      cart_items: List[CartItem] = CartItem.objects.filter(cart__user__id=instance.order.user.id)
      for item in cart_items:
         item.delete()