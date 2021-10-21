from django.db import models


class BaseModel(models.Model):

   id = models.AutoField(primary_key=True)
   state = models.BooleanField(default=True)
   created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
   modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)
   deleted_date = models.DateTimeField(auto_now=True, auto_now_add=False)

   def __str__(self) -> str:
      pass

   class Meta:
      abstract = True