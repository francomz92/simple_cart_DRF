from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from apps.cart.models import Cart


@receiver(post_save, sender=get_user_model())
def create_cart_for_user(sender, instance, created, **kwargs):
   if created:
      Cart.objects.create(user=instance)
