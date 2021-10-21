from rest_framework import serializers

from apps.products.models import MeasureUnit


class MeasureUnitSerializer(serializers.ModelSerializer):
   class Meta:
      model = MeasureUnit
      exclude = [
          'state',
          'created_date',
          'modified_date',
          'deleted_date',
      ]
