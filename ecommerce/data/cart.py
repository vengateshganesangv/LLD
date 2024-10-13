from data.product_copy import ProductCopy

class Cart:
    def __init__(self, cart_id: int):
        self.id = cart_id
        self.products: list[ProductCopy] = []

    def add(self, product_copy: ProductCopy):
        self.products.append(product_copy)

    def remove(self, product_copy: ProductCopy):
        if product_copy not in self.products:
            raise RuntimeError("Product not in cart")
        self.products.remove(product_copy)

    def get_cart_amount(self) -> float:
        return sum(product_copy.get_product().price_in_inr for product_copy in self.products)

    def get_distinct_items_count(self) -> int:
        distinct_ids = {product_copy.get_product().id for product_copy in self.products}
        return len(distinct_ids)

    def get_total_items_count(self) -> int:
        return len(self.products)