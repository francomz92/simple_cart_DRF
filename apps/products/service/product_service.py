from apps.products.models import Product


class ProductService:
   @classmethod
   def product_disabling(cls, product: Product):
      product.state = False
      product.save()