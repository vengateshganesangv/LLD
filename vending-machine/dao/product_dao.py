from dao.abstract_dao import AbstractDAO
from db.db import PRODUCT_TABLE
from entity.product_entity import Product

class ProductDAO(AbstractDAO):
    def create(self, product: Product):
        PRODUCT_TABLE[product.id] = product
        return True

    def read(self, id):
        return PRODUCT_TABLE.get(id)

    def update(self, product: Product):
        if product.id in PRODUCT_TABLE:
            PRODUCT_TABLE[product.id] = product
            return True
        return False

    def delete(self, id):
        if id in PRODUCT_TABLE:
            del PRODUCT_TABLE[id]
            return True
        return False

    def get_all(self):
        return list(PRODUCT_TABLE.values())