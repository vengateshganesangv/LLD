from abc import ABC, abstractmethod
from common.color import Color
from common.move import Move
from common.strategy import Strategy

class Player(ABC):
    def __init__(self, name: str, color: Color, strategy: Strategy):
        self.name = name
        self.color = color
        self.strategy = strategy

    @abstractmethod
    def make_move(self, board) -> Move:
        pass