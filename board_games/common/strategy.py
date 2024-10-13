from abc import ABC, abstractmethod
from common.move import Move

class Strategy(ABC):
    @abstractmethod
    def make_move(self, player, board) -> Move:
        pass