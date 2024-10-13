from board import Board
import random

class SnakeAndLadderBoard(Board):
    def __init__(self, size: int):
        self.size = size
        self.grid_size = int(size ** 0.5)  # Square root of board size for grid
        self.snakes = self._generate_snakes_and_ladders(5)
        self.ladders = self._generate_snakes_and_ladders(5)
        self.board = self._create_board()

    def _create_board(self):
        board = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        num = self.size
        for i in range(self.grid_size):
            row = board[self.grid_size - 1 - i]
            if i % 2 == 0:
                for j in range(self.grid_size):
                    row[j] = num
                    num -= 1
            else:
                for j in range(self.grid_size - 1, -1, -1):
                    row[j] = num
                    num -= 1
        return board

    def _generate_snakes_and_ladders(self, count: int) -> dict:
        elements = {}
        while len(elements) < count:
            start = random.randint(2, self.size - 1)
            end = random.randint(1, self.size - 1)
            if start != end and start not in elements and end not in elements.values():
                elements[start] = end
        return elements

    def move_player(self, current_position: int, dice_roll: int) -> int:
        new_position = current_position + dice_roll
        if new_position > self.size:
            return current_position

        if new_position in self.snakes:
            print(f"Oops! Snake at {new_position}. Going down to {self.snakes[new_position]}")
            return self.snakes[new_position]
        elif new_position in self.ladders:
            print(f"Yay! Ladder at {new_position}. Going up to {self.ladders[new_position]}")
            return self.ladders[new_position]
        else:
            return new_position

    def is_game_over(self, position: int) -> bool:
        return position == self.size

    def display(self, player_positions: dict) -> None:
        print("\nSnake and Ladder Board:")
        for row in self.board:
            for cell in row:
                cell_str = str(cell).rjust(2)
                if cell in self.snakes:
                    cell_str += "S"
                elif cell in self.ladders:
                    cell_str += "L"
                else:
                    cell_str += " "
                
                for player, pos in player_positions.items():
                    if pos == cell:
                        cell_str += player[0]  # Add first letter of player's name
                
                print(f"[{cell_str.ljust(4)}]", end="")
            print()  # New line after each row
        
        print("\nLegend:")
        print("S: Snake")
        print("L: Ladder")
        for player in player_positions:
            print(f"{player[0]}: {player}")
        
        print("\nSnakes:", self.snakes)
        print("Ladders:", self.ladders)