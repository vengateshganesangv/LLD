from data.product import Product
from filter.product_filter import ProductFilter

class IdleFilter(ProductFilter):
    def filter(self, products: list[Product]) -> list[Product]:
        return products