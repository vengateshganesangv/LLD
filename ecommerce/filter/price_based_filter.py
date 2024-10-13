from data.product import Product
from filter.product_filter import ProductFilter


class PriceBasedFilter:
    def __init__(self, price_upper_cap: float, next_filter: ProductFilter):
        self.price_upper_cap = price_upper_cap
        self.next_filter = next_filter

    def filter(self, products: list[Product]) -> list[Product]:
        filtered_products = self.next_filter.filter(products)
        return [product for product in filtered_products if product.price_in_inr <= self.price_upper_cap]
