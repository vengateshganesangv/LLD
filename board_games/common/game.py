from abc import ABC, abstractmethod
from collections import deque
from common.board import Board
from common.player import Player

class Game(ABC):
    def __init__(self, players: deque[Player], board: Board):
        self.players = players
        self.board = board

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def is_over(self) -> bool:
        pass

    @abstractmethod
    def prepare_board(self):
        pass