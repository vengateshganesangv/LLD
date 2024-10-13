from abc import ABC, abstractmethod

class AbstractEvictionPolicy(ABC):
    @abstractmethod
    def update(self, key):
        pass

    @abstractmethod
    def evict(self):
        pass