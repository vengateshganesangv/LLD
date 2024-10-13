from abc import ABC, abstractmethod
from entity.order_line_entity import OrderLine
from entity.shop_order import ShopOrder
from dto.payment_repsonse_dto import PaymentResponseDTO
from manager.abstract_cart_manager import AbstractCartManager

class AbstractOrderManager(ABC):
    @abstractmethod
    def place_order(self, cart_manager: AbstractCartManager, payment_response: PaymentResponseDTO, transaction_id: int) -> ShopOrder:
        pass

    @abstractmethod
    def get_order_refund_value(self, order_id: int) -> int:
        pass

    @abstractmethod
    def get_order_items(self, order_id: int) -> list[OrderLine]:
        pass