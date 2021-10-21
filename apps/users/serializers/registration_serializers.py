from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class RegistrationSerializer(serializers.ModelSerializer):
   password = serializers.CharField(required=True)
   password_confirmation = serializers.CharField(required=True)

   class Meta:
      model = get_user_model()
      fields = [
          'username',
          'email',
          'password',
          'password_confirmation',
          'first_name',
          'last_name',
          'image',
      ]
      extra_kwargs = {
          'password': {
              'write_only': True,
              'style': {
                  'input_type': 'password',
              }
          },
          'password_confirmation': {
              'write_only': True,
              'style': {
                  'input_type': 'password',
              }
          }
      }

   def validate(self, attrs):
      password_confirmation = attrs.pop('password_confirmation')
      similar = True if attrs['username'] == attrs['password'] or \
                     attrs['username'].replace(attrs['password'], '') != attrs['username'] or \
                     attrs['password'].replace(attrs['username'], '') != attrs['password'] \
               else False
      if similar:
         raise ValidationError('Username and password are similar')
      if attrs['password'] != password_confirmation:
         raise ValidationError('Passwords do not match')
      return attrs
