from abc import ABC, abstractmethod
#Interface
class Board(ABC):
    @abstractmethod
    def place_mark(self, row: int, col: int, symbol: str) -> bool:
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    @abstractmethod
    def check_for_win(self, symbol: str, row: int, col: int) -> bool:
        pass

    @abstractmethod
    def display(self) -> None:
        pass
