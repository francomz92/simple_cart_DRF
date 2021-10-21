from django.db import models
from django.core.validators import FileExtensionValidator

from simple_history.models import HistoricalRecords

from core.models import BaseModel


class MeasureUnit(BaseModel):

   description = models.CharField(max_length=50, unique=True)
   historical = HistoricalRecords()

   @property
   def _history_user(self):
      return self.changed_by

   @_history_user.setter
   def _history_user(self, value):
      self.changed_by = value

   def __str__(self) -> str:
      return self.description

   class Meta:
      verbose_name = "Measure Unit"
      verbose_name_plural = "Measure Units"


class ProductCategory(BaseModel):

   name = models.CharField(max_length=30, unique=True)
   historical = HistoricalRecords()

   @property
   def _history_user(self):
      return self.changed_by

   @_history_user.setter
   def _history_user(self, value):
      self.changed_by = value

   def __str__(self) -> str:
      return self.name

   class Meta:
      verbose_name = "Category"
      verbose_name_plural = "Categories"


class Product(BaseModel):

   name = models.CharField(max_length=25, unique=True)
   description = models.TextField(max_length=255)
   category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
   measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)
   image = models.ImageField(upload_to='products/',
                             blank=True,
                             null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
   price = models.PositiveSmallIntegerField()
   historical = HistoricalRecords()

   @property
   def _history_user(self):
      return self.changed_by

   @_history_user.setter
   def _history_user(self, value):
      self.changed_by = value

   def __str__(self) -> str:
      return self.name

   class Meta:
      verbose_name = "Product"
      verbose_name_plural = "Products"