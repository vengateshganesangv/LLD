from abc import ABC, abstractmethod

class Board(ABC):
    @abstractmethod
    def move_player(self, current_position: int, dice_roll: int) -> int:
        pass

    @abstractmethod
    def is_game_over(self, position: int) -> bool:
        pass

    @abstractmethod
    def display(self) -> None:
        pass