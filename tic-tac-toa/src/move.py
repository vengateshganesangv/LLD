from abc import ABC, abstractmethod

class Move(ABC):
    @abstractmethod
    def get_row(self) -> int:
        pass

    @abstractmethod
    def get_col(self) -> int:
        pass
