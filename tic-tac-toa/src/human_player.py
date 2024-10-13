from player import Player
from board import Board
from move import Move
from tic_tac_toa_move import TicTacToaMove

class HumanPlayer(Player):
    def __init__(self, symbol: str, name: str):
        self.symbol = symbol
        self.name = name

    def get_symbol(self) -> str:
        return self.symbol

    def get_name(self) -> str:
        return self.name

    def make_move(self, board: Board) -> Move:
        row, col = None, None

        while row is None or col is None or not board.place_mark(row, col, self.symbol):
            print(f"{self.name}, enter your move (row and column):")
            try:
                row = int(input("Row: ")) - 1
                col = int(input("Column: ")) - 1
            except ValueError:
                print("Invalid input. Please enter integers for row and column.")

        return TicTacToaMove(row, col)
