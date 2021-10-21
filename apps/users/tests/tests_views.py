from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

from rest_framework.test import APIClient
from rest_framework import status


class UserAdminAuthenticatedViewsTest(TestCase):
   ''' Test for a user that is admin'''
   def setUp(self):
      user = get_user_model().objects.create_superuser(username='root',
                                                       email='root@email.com',
                                                       password='root')
      self.USERS_URL = reverse('users:users-list')
      self.USER_ID_URL = reverse('users:users-detail', args=[user.id])
      self.client = APIClient()
      self.client.force_login(user)

   def test_get_users(self):
      ''' Get list of all users '''
      # When
      response = self.client.get(self.USERS_URL)
      # Then
      self.assertEqual(response.status_code, status.HTTP_200_OK)

   def test_post_users(self):
      ''' Create a user '''
      # Given
      data = {
          'username': 'test2',
          'email': 'test2@example.com',
          'password': 'password',
      }
      # When
      response = self.client.post(self.USERS_URL, data)
      # Then
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   def test_get_one_user(self):
      ''' Get one user '''
      # When
      response = self.client.get(self.USER_ID_URL)
      # Then
      self.assertEqual(response.status_code, status.HTTP_200_OK)

   def test_put_one_user(self):
      ''' Update one user '''
      # Given
      data = {
          'username': 'root',
          'email': 'root@email.com',
          'first_name': 'Pepito',
          'password': 'root',
      }
      # When
      response = self.client.put(self.USER_ID_URL, data)
      # Then
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(response.data.get('first_name'), 'Pepito')

   def test_delete_one_user(self):
      ''' Delete one user '''
      # When
      response = self.client.delete(self.USER_ID_URL)
      # Then
      self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserNotAdminViewTest(TestCase):
   ''' Test for a user that is not admin '''
   def setUp(self):
      user = get_user_model().objects.create_user(username='root', email='root@email.com', password='root')
      self.USERS_URL = reverse('users:users-list')
      self.USER_id_URL = reverse('users:users-detail', args=[user.id])
      self.client = APIClient()
      self.client.force_login(user)

   def test_get_users(self):
      ''' Get list of all users '''
      # When
      response = self.client.get(self.USERS_URL)
      # Then
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

   def test_post_users(self):
      ''' Create a user '''
      # Given
      data = {
          'username': 'test2',
          'email': 'test2@example.com',
          'password': 'password',
      }
      # When
      response = self.client.post(self.USERS_URL, data)
      # Then
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

   def test_get_self_user(self):
      ''' Get self user '''
      # When
      response = self.client.get(self.USER_id_URL)
      # Then
      self.assertEqual(response.status_code, status.HTTP_200_OK)

   def test_get_another_user(self):
      ''' Get another user '''
      new_user = get_user_model().objects.create_user(username='testX',
                                                      email='testX@example.com',
                                                      password='passwordX')
      # When
      url = reverse('users:users-detail', args=[new_user.id])
      response = self.client.get(url)
      # Then
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

   def test_put_self_user(self):
      ''' Update self user '''
      # Given
      data = {
          'username': 'root2',
          'email': 'root@email.com',
          'first_name': 'Pepe',
          'password': 'root',
      }
      # When
      response = self.client.put(self.USER_id_URL, data)
      # Then
      self.assertEqual(response.status_code, status.HTTP_200_OK)

   def test_put_another_user(self):
      ''' Update another user '''
      # Given
      data = {
          'username': 'root2',
          'email': 'root@email.com',
          'first_name': 'Pepe',
          'password': 'root',
      }
      new_user = get_user_model().objects.create_user(username='testX',
                                                      email='testX@example.com',
                                                      password='passwordX')
      # When
      url = reverse('users:users-detail', args=[new_user.id])
      response = self.client.put(url, data)
      # Then
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

   def test_delete_self_user(self):
      ''' Delete self user '''
      # When
      response = self.client.delete(self.USER_id_URL)
      # Then
      self.assertEqual(response.status_code, status.HTTP_200_OK)

   def test_delete_another_user(self):
      ''' Delete another user '''
      new_user = get_user_model().objects.create_user(username='testX',
                                                      email='testX@example.com',
                                                      password='passwordX')
      url = reverse('users:users-detail', args=[new_user.id])
      # When
      response = self.client.delete(url)
      # Then
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)