from board import Board

class TicTacToaBoard(Board):
    def __init__(self, size: int):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]

    def place_mark(self, row: int, col: int, symbol: str) -> bool:
        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == " ":
            self.board[row][col] = symbol
            return True
        return False

    def is_full(self) -> bool:
        return all(self.board[i][j] != " " for i in range(self.size) for j in range(self.size))

    def check_for_win(self, symbol: str, row: int, col: int) -> bool:
        row_win = all(self.board[row][i] == symbol for i in range(self.size))
        col_win = all(self.board[i][col] == symbol for i in range(self.size))
        main_diag_win = all(self.board[i][i] == symbol for i in range(self.size))
        other_diag_win = all(self.board[i][self.size - 1 - i] == symbol for i in range(self.size))
        return any([row_win, col_win, main_diag_win, other_diag_win])

    def display(self) -> None:
        print("-------------")
        for i in range(self.size):
            print("|", end="")
            for j in range(self.size):
                print(self.board[i][j] + "|", end="")
            print("\n-------------")
