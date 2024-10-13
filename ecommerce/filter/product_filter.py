from abc import ABC, abstractmethod

from data.product import Product

class ProductFilter(ABC):
    @abstractmethod
    def filter(self, products) -> list[Product]: 
        pass
