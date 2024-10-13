from abc import ABC, abstractmethod

class Publisher(ABC):
    @abstractmethod
    def add_subscriber(self, subscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber):
        pass

    @abstractmethod
    def notify_all(self, message):
        pass