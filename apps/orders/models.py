from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from apps.products.models import Product


class Order(models.Model):
   user: get_user_model() = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
   created_date: datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

   class Meta:
      verbose_name = _('Order')
      verbose_name_plural = _('Orders')

   def __str__(self) -> str:
      return f'{self.user.username}: order n° {self.id}'


class OrderItem(models.Model):
   product: Product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
   amount: int = models.PositiveSmallIntegerField()
   price: float = models.DecimalField(max_digits=8, decimal_places=2)
   order: Order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='order_items')

   class Meta:
      verbose_name = _('Order Item')
      verbose_name_plural = _('Order Items')

   @property
   def partial_price(self):
      return self.price * self.amount

   def __str__(self) -> str:
      return f'{self.product.name} at {self.amount}'
