from django.db import models
from django.contrib.auth import get_user_model

from apps.products.models import Product


class Cart(models.Model):
   ''' Cart model '''
   user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE, related_name='cart_user')

   class Meta:
      verbose_name = 'cart'
      verbose_name_plural = 'carts'

   def __str__(self) -> str:
      return f'{self.user.username} cart'


class CartItem(models.Model):
   ''' Purchase details model '''
   cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='cart')
   product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='purchase_details')
   amount = models.PositiveSmallIntegerField()
   created_date = models.DateTimeField(auto_now_add=True, editable=False)

   @property
   def partial_price(self):
      return self.product.price * self.amount

   class Meta:
      verbose_name = 'purchase_detail'
      verbose_name_plural = 'purchase_details'

   def __str__(self) -> str:
      return f'PurchaseDetail id: {self.id}'
