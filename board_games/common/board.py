from abc import ABC, abstractmethod
from common.move import Move
from common.pair import Pair
from common.cell import Cell

class Board(ABC):
    @abstractmethod
    def apply_move(self, move: Move):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_cell(self, position: Pair) -> Cell:
        pass