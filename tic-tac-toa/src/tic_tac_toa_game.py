from tic_tac_toa_board import TicTacToaBoard
from human_player import HumanPlayer

class TicTacToeGame:
    def __init__(self, board_size: int):
        self.board_size = board_size
        self.board = TicTacToaBoard(board_size)
        self.player1 = HumanPlayer("X", "Vengat")
        self.player2 = HumanPlayer("O", "Vengi")
        self.current_player = self.player1
        self.game_won = False

    def play_game(self) -> None:
        self.board.display()

        while not self.board.is_full() and not self.game_won:
            move = self.current_player.make_move(self.board)
            self.board.display()

            row, col = move.row, move.col

            if self.board.check_for_win(self.current_player.symbol, row, col):
                print(f"{self.current_player.name} wins!")
                self.game_won = True

            self.current_player = self.player2 if self.current_player == self.player1 else self.player1

        if not self.game_won:
            print("It's a tie!")


game = TicTacToeGame(4)
game.play_game()
