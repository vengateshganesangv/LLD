from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_position(self) -> int:
        pass

    @abstractmethod
    def set_position(self, position: int) -> None:
        pass