from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def read_card(self, card_details):
        pass

    @abstractmethod
    def cancel_transaction(self, trans_id):
        pass

    @abstractmethod
    def read_withdrawal_details(self, card_details, trans_id, amount):
        pass

    @abstractmethod
    def dispense_cash(self, trans_id):
        pass

    @abstractmethod
    def eject_card(self):
        pass

    @abstractmethod
    def get_state_name(self):
        pass