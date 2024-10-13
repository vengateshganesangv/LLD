from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def execute_payment(self) -> bool:
        pass

    @abstractmethod
    def get_amount(self) -> float:
        pass
