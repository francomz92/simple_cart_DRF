from django.contrib.auth import get_user_model
from rest_framework import status

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from apps.cart.models import CartItem

from apps.products.models import Product, MeasureUnit, ProductCategory


def get_cart_creation_url(user):
   return reverse('cart:cart', args=[user.id])


def set_atributes_needed():
   category = ProductCategory.objects.create(name='Bebidas')
   measure_unit = MeasureUnit.objects.create(description='Litros')
   return category, measure_unit


def set_default_products(obj):
   obj.category, obj.measure_unit = set_atributes_needed()
   product1 = Product.objects.create(name='Coca',
                                     description='Una description',
                                     category=obj.category,
                                     measure_unit=obj.measure_unit,
                                     price=180)
   product2 = Product.objects.create(name='Sprite',
                                     description='Otra description',
                                     category=obj.category,
                                     measure_unit=obj.measure_unit,
                                     price=170)
   return product1, product2


class CartItemAuthorizedTest(APITestCase):
   ''' Tests for cart creation by authenticated user '''
   def setUp(self) -> None:
      self.product1, self.product2 = set_default_products(self)

      self.user = get_user_model().objects.create(username='root', email='root@example.com')

      self.client.force_login(self.user)

      return super().setUp()

   def test_create_cart_item_by_owner_customer(self):
      ''' Test cart item creation by owner customer '''
      url = get_cart_creation_url(self.user)
      data = {
          'product': self.product1.id,
          'amount': 3,
      }

      # When
      res = self.client.post(url, data=data, format='json')
      cart_item = CartItem.objects.filter(cart__user=self.user, product=data['product']).first()
      # Then
      self.assertEqual(res.status_code, status.HTTP_201_CREATED)
      self.assertIsNotNone(res.data)
      self.assertEqual(res.data['id'], cart_item.id)

   def test_create_cart_item_by_not_owner_customer(self):
      ''' Test cart item creation by not owner customer '''
      new_user = get_user_model().objects.create_user(username='test',
                                                      email='test@example.com',
                                                      password='password333')
      url = get_cart_creation_url(new_user)
      data = [
          {
              'product': self.product1.id,
              'amount': 4
          },
      ]
      # When
      res = self.client.post(url, data=data, format='json')
      # Then
      self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class CartItemUnauthorizedTest(APITestCase):
   ''' Test for cart creation by unauthorized user '''
   def setUp(self) -> None:
      self.product1, self.product2 = set_default_products(self)
      self.user = get_user_model().objects.create(username='root', email='root@example.com')
      return super().setUp()

   def test_create_cart_item_by_owner_customer(self):
      ''' Test cart item creation by owner customer '''
      url = get_cart_creation_url(self.user)
      data = [
          {
              'product': self.product1.id,
              'amount': 3,
          },
      ]
      # When
      res = self.client.post(url, data=data, format='json')
      # Then
      self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)