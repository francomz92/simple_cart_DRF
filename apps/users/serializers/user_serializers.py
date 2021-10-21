from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth import get_user_model
#
#
''' Lo idoneo es que halla un serializer para cada Request Method ["GET", "POST", "PUT", "DELETE", ...] '''


class BaseUserSerializer(serializers.ModelSerializer):
   def __init__(self, *args, **kwargs):
      super(BaseUserSerializer, self).__init__(*args, **kwargs)
      for field in self.fields.values():
         if 'max_length' in field.default_error_messages:
            field.default_error_messages['max_length'] = 'Máximo permitido {max_length} caracteres.'
         if 'required' in field.default_error_messages:
            field.default_error_messages['required'] = 'Este campo es obligatorio.'
         if 'blank' in field.default_error_messages:
            field.default_error_messages['blank'] = 'Este campo no puede estar en blanco.'
         if 'null' in field.default_error_messages:
            field.default_error_messages['null'] = 'Este campo es obligatorio.'

   class Meta:
      model = get_user_model()
      exclude = [
          'is_active',
          'is_staff',
          'is_superuser',
          'groups',
          'user_permissions',
          'modified_date',
          'deleted_date',
      ]
      read_only_fields = ['id', 'last_login', 'state']
      extra_kwargs = {
          'password': {
              'write_only': True,
              'style': {
                  'input_type': 'password',
              },
          },
      }

   def to_representation(self, instance):
      data = super().to_representation(instance)
      data['image'] = instance.image if instance.image else ''

      return data


class UserSerializer(BaseUserSerializer):

   # Este metodo se invoca cuando se llama a .save() en la vista del POST
   def create(self, validated_data):
      password = validated_data.pop('password')
      user = get_user_model()(**validated_data)
      user.username.lower()
      user.set_password(password)
      user.save()
      return user


class UpdateUserSerializer(BaseUserSerializer):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.Meta.read_only_fields.extend(['username', 'email'])

   # Este metodo se invoca cuando se llama a .save() en la vista del PUT
   def update(self, instance, validated_data):
      # if validated_data.get('password', None) is not None:
      #    updated_user.set_password(validated_data['password'])
      # updated_user.save()
      # return updated_user
      password = validated_data['password'] or None
      if not instance.check_password(password):
         raise ValidationError('Password is incorrect')
      return super().update(instance, validated_data)
