from data.product import Product
from filter.product_filter import ProductFilter


class RatingBasedFilter:
    def __init__(self, min_rating, next_filter: ProductFilter):
        self.min_rating = min_rating
        self.next_filter = next_filter

    def filter(self, products: list[Product]) -> list[Product]:
        filtered_products = self.next_filter.filter(products)
        return [product for product in filtered_products if product.rating.get_val() >= self.min_rating.get_val()]
