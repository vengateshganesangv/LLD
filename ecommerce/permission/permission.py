from abc import ABC, abstractmethod

class Permission(ABC):
    @abstractmethod
    def is_permitted(self):
        pass