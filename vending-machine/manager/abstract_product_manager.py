# manager/abstract_product_manager.py
from abc import ABC, abstractmethod
from dto.product_info_query_dto import ProductInfoQueryDTO
from entity.product_entity import Product

class AbstractProductManager(ABC):
    @abstractmethod
    def get_product_list(self) -> list[Product]:
        pass

    @abstractmethod
    def get_product_amount(self, product_info: ProductInfoQueryDTO) -> float:
        pass