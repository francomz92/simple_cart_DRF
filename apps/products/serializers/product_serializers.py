from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in self.fields.values():
         if 'null' in field.default_error_messages:
            field.default_error_messages['null'] = 'Este campo es obligatorio'
         if 'blank' in field.default_error_messages:
            field.default_error_messages['blank'] = 'Este campo es obligatorio'
         if 'required' in field.default_error_messages:
            field.default_error_messages['required'] = 'Este campo es obligatorio'

   class Meta:
      model = Product
      exclude = [
          'state',
          'created_date',
          'modified_date',
          'deleted_date',
      ]

   def to_representation(self, instance):
      data = super().to_representation(instance)
      if data['image'] is None: data['image'] = ''
      data['category'] = instance.category.name
      data['measure_unit'] = instance.measure_unit.description
      return data