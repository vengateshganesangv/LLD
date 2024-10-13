from manager.AbstractProductManager import AbstractProductManager
from entity.Product import Product
from data.ProductInfoQuery import ProductInfoQuery
from db.db import PRODUCT_TABLE

class InMemoryProductManager(AbstractProductManager):
    def getProductList(self) -> list[Product]:
        return list(PRODUCT_TABLE.items()) 
    def getProductAmount(self, product: ProductInfoQuery) -> float:
        amount = PRODUCT_TABLE[product.id].price
        total_amount = amount * product.quantity
        return total_amount
        