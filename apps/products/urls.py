from rest_framework.routers import DefaultRouter

from .views.product_category_views import *
from .views.product_views import *
from .views.measure_unit_views import *

app_name = 'products'

router = DefaultRouter()

router.register(r'measure_units', MeasureViewSet, basename='measure_units')
router.register(r'categories', ProductCategoryViewSet, basename='categories')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls