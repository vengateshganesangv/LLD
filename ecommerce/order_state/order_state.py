from abc import ABC, abstractmethod

class OrderState(ABC):
    def __init__(self, order):
        self.order = order

    @abstractmethod
    def schedule_pickup(self, pickup_details: dict):
        pass

    @abstractmethod
    def pickup(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass

    def transition_error(self, action: str):
        raise ValueError(f"Cannot {action} order in {self.get_status()} state")