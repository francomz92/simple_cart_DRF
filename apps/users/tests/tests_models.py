from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


class UserTest(TestCase):
   ''' User model tests '''
   model = get_user_model()

   def setUp(self):
      self.username = 'franco'
      self.email = 'franco@email.com'
      self.password = 'franco'

   def test_create_user(self):
      ''' Hapy path to create a user '''
      # When
      user = self.model.objects.create(username=self.username, email=self.email, password=self.password)
      # Then
      self.assertIsNotNone(user)
      self.assertEqual(user.username, 'franco')

   def test_create_superuser(self):
      ''' Hapy path to create a superuser '''
      # When
      user = self.model.objects.create_superuser(username=self.username,
                                                 email=self.email,
                                                 password=self.password)
      # Then
      self.assertIsNotNone(user)
      self.assertTrue(user.is_superuser)

   def test_unique_username(self):
      ''' Test unique username '''
      # Given
      self.model.objects.create(username=self.username, email=self.email, password=self.password)
      # Then
      with self.assertRaises(IntegrityError):
         self.model.objects.create(username=self.username, email='other@email.com', password=self.password)

   def test_unique_email(self):
      ''' Test unique email '''
      # Given
      self.model.objects.create(username=self.username, email=self.email, password=self.password)
      # Then
      with self.assertRaises(IntegrityError):
         self.model.objects.create(username='toto', email=self.email, password=self.password)
