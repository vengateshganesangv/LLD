from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def notify(self, message):
        pass