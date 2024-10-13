from abc import ABC, abstractmethod
from common.color import Color
from common.pair import Pair

class Piece(ABC):
    def __init__(self, color: Color, position: Pair):
        self.color = color
        self.position = position
        self.is_dead = False

    @abstractmethod
    def get_valid_moves(self, board):
        pass

    def move(self, new_position: Pair):
        self.position = new_position

    @abstractmethod
    def can_attack(self, board, position: Pair) -> bool:
        pass

    @property
    @abstractmethod
    def symbol(self) -> str:
        pass