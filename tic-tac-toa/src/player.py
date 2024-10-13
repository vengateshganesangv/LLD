from abc import ABC, abstractmethod
from board import Board
from move import Move

class Player(ABC):
    @abstractmethod
    def get_symbol(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def make_move(self, board: Board) -> Move:
        pass
