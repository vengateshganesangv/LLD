from abc import ABC, abstractmethod

from dto.product_info_query_dto import ProductInfoQueryDTO

class State(ABC):
    @abstractmethod
    def init(self):
        pass
    @abstractmethod
    def show_product_details(self):
        pass
    @abstractmethod
    def read_product_details(self,transaction_id, productDetails: list[ProductInfoQueryDTO]):
        pass
    @abstractmethod
    def show_cart(self):
        pass
    @abstractmethod
    def place_order(self, payment_info, payment_mode):
        pass
    @abstractmethod
    def cancel_transaction(self, transaction_id):
        pass
    @abstractmethod
    def cash_dispensing(self):
        pass
    @abstractmethod
    def product_dispensing(self):
        pass
    @abstractmethod
    def get_state(self):
        pass
