from abc import ABC, abstractmethod
from data.ProductInfoQuery import ProductInfoQuery
from entity.Product import Product

class AbstractProductManager(ABC):
    @abstractmethod
    def getProductList(self) -> list[Product]:
        pass
    def getProductAmount(self, productInfo: ProductInfoQuery) -> float:
        pass
    