from data.product import Product
from filter.product_filter import ProductFilter


class PayOnDelFilter:
    def __init__(self, is_pay_on_delivery: bool, next_filter: ProductFilter):
        self.is_pay_on_delivery = is_pay_on_delivery
        self.next_filter = next_filter

    def filter(self, products: list[Product]) -> list[Product]:
        filtered_products = self.next_filter.filter(products)
        return [product for product in filtered_products if product.is_pay_on_delivery == self.is_pay_on_delivery]
