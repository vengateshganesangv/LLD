from dao.product_dao import ProductDAO
from entity.product_entity import Product
from manager.abstract_product_manager import AbstractProductManager
from dto.product_info_query_dto import ProductInfoQueryDTO

class InMemoryProductManager(AbstractProductManager):
    def __init__(self):
        self.product_dao = ProductDAO()

    def get_product_list(self) -> list[Product]:
        return self.product_dao.get_all()

    def get_product_amount(self, product: ProductInfoQueryDTO) -> float:
        db_product = self.product_dao.read(product.id)
        if db_product:
            return db_product.price * product.quantity
        return 0