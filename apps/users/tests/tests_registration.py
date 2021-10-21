from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

from apps.users.views.registration import activation_token


class UserRegistrationTests(APITestCase):
   ''' Tests for UserRegistration '''

   USER_REGISTRATION_URL = reverse('users:signup')

   def test_new_user_registration(self):
      ''' Tests for new user registration '''
      data = {
          'username': 'pepe123',
          'email': 'pepe123@example.com',
          'password': 'password333',
          'password_confirmation': 'password333'
      }
      # When
      res = self.client.post(self.USER_REGISTRATION_URL, data=data)
      user = get_user_model().objects.filter(username=data['username']).first()
      # Then
      self.assertEqual(res.status_code, status.HTTP_201_CREATED)
      self.assertIsNotNone(res.data)
      self.assertEqual(data['username'], user.username)
      self.assertFalse(user.is_active)

   def test_account_verification(self):
      ''' Tests for account verification '''
      data = {
          'username': 'pepe234',
          'email': 'pepe234@example.com',
          'password': 'password333',
          'password_confirmation': 'password333',
      }
      # When
      res = self.client.post(self.USER_REGISTRATION_URL, data=data)
      # Then
      self.assertEqual(res.status_code, status.HTTP_201_CREATED)
      # Given
      user = get_user_model().objects.filter(username=data['username']).first()
      domain = 'http://localhost:3000'
      uid = urlsafe_base64_encode(force_bytes(user.pk))
      token = activation_token.make_token(user)
      path = reverse('users:account_activation', args=[uid, token])
      link = domain + path
      # When
      res = self.client.get(link)
      user = get_user_model().objects.filter(username=data['username']).first()
      # Then
      self.assertEqual(res.status_code, status.HTTP_200_OK)
      self.assertTrue(user.is_active)