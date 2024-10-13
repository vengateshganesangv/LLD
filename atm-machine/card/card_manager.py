from abc import ABC, abstractmethod

class CardManager(ABC):
    @abstractmethod
    def validate_card(self, card_details):
        pass

    @abstractmethod
    def validate_withdrawal(self, amount, trans_id):
        pass

    @abstractmethod
    def execute_withdrawal(self, trans_id):
        pass