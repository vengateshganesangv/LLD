from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def init(self):
        pass
    @abstractmethod
    def show_product_details(self):
        pass
    @abstractmethod
    def read_product_details(self, product_id, qty):
        pass
    @abstractmethod
    def read_amount(self, purchaser_id, amount):
        pass
    @abstractmethod
    def cancel_transaction(self, purchaser_id):
        pass
    def cash_dispensing(self):
        pass
    def product_dispensing(self):
        pass
    def get_state_name(self):
        pass
