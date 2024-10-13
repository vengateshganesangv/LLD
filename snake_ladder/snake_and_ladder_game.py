from snake_and_ladder_board import SnakeAndLadderBoard
from human_player import HumanPlayer
import random

class SnakeAndLadderGame:
    def __init__(self, board_size: int, num_players: int):
        self.board_size = board_size
        self.board = SnakeAndLadderBoard(board_size)
        self.players = [HumanPlayer(f"Player {i+1}") for i in range(num_players)]
        self.current_player_index = 0
        self.game_over = False

    def play_game(self) -> None:
        while not self.game_over:
            self._display_board()
            current_player = self.players[self.current_player_index]
            print(f"\n{current_player.name}'s turn.")
            input("Press Enter to roll the dice...")

            dice_roll = random.randint(1, 6)
            print(f"{current_player.name} rolled a {dice_roll}")

            new_position = self.board.move_player(current_player.position, dice_roll)
            current_player.position = new_position

            print(f"{current_player.name} moved to position {new_position}")

            if new_position == self.board_size:
                print(f"{current_player.name} wins!")
                self.game_over = True
            else:
                self.current_player_index = (self.current_player_index + 1) % len(self.players)

        self._display_board()

    def _display_board(self):
        player_positions = {player.name: player.position for player in self.players}
        self.board.display(player_positions)

game = SnakeAndLadderGame(100, 2)
game.play_game()