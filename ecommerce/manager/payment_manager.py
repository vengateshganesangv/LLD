from abc import ABC, abstractmethod

class PaymentManager(ABC):

    @abstractmethod
    def execute_payment(self):
        pass
