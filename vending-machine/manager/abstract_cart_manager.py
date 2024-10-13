from abc import ABC, abstractmethod
from dto.cart_info_dto import CartInfoDTO
from dto.product_info_query_dto import ProductInfoQueryDTO
from manager.abstract_product_manager import AbstractProductManager

class AbstractCartManager(ABC):
    @abstractmethod
    def add_to_cart(self, transaction_id: int, product_details: list[ProductInfoQueryDTO], product_manager: AbstractProductManager) -> bool:
        pass

    @abstractmethod
    def get_cart_info(self) -> CartInfoDTO:
        pass