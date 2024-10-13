from abc import ABC, abstractmethod

class AbstractDAO(ABC):
    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, id):
        pass
