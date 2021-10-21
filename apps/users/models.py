from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from simple_history.models import HistoricalRecords

from core.models import BaseModel

# Create your models here.


class CustomUserManager(BaseUserManager):
   def _create_user(self, username, email, password, **kwargs):
      if not email:
         raise ValueError('Email address is required')
      user = self.model(username=username, email=self.normalize_email(email), **kwargs)
      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_user(self, username, email, password=None):
      return self._create_user(username, email, password)

   def create_superuser(self, username, email, password=None):
      return self._create_user(username, email, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin, BaseModel):

   username = models.CharField(max_length=15, unique=True)
   email = models.EmailField(max_length=50, unique=True)
   first_name = models.CharField(max_length=30, blank=True)
   last_name = models.CharField(max_length=30, blank=True)
   image = models.ImageField(upload_to='profile/', null=True)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   is_superuser = models.BooleanField(default=False)
   history = HistoricalRecords()
   objects = CustomUserManager()

   USERNAME_FIELD = 'username'

   REQUIRED_FIELDS = ['email']

   def __str__(self) -> str:
      return f'{self.username}'

   class Meta:
      verbose_name = 'User'
      verbose_name_plural = 'Users'