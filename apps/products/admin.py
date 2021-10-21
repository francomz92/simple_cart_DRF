from django.contrib import admin
from apps.products.models import MeasureUnit, Product, ProductCategory


@admin.register(MeasureUnit)
class MeasureUnitAdmin(admin.ModelAdmin):
   list_display = ['id', 'description', 'state', 'modified_date']
   list_display_links = ['id', 'description']
   search_fields = ['description']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'modified_date']
   list_display_links = ['id', 'name']
   search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'description', 'category', 'state', 'image', 'modified_date']
   filter_fields = ['category']
   search_fields = ['name', 'description']
   list_display_links = ['id', 'name']
   autocomplete_fields = ['category', 'measure_unit']
   ordering = ['id']
   list_editable = ['state']