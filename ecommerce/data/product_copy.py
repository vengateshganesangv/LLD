from data.product import Product

class ProductCopy:
    def __init__(self, product: Product, product_id: int, is_sold: bool):
        self.product = product
        self.id = product_id
        self.is_sold = is_sold

    def get_product(self) -> Product:
        return self.product

    def get_id(self) -> int:
        return self.id

    def is_sold(self) -> bool:
        return self.is_sold