from common.strategy import Strategy
from common.move import Move
from common.pair import Pair

class HumanChessStrategy(Strategy):
    def make_move(self, player, board) -> Move:
        while True:
            try:
                start_row = int(input(f"{player.name}, enter start row (0-7): "))
                start_col = int(input(f"{player.name}, enter start column (0-7): "))
                end_row = int(input(f"{player.name}, enter end row (0-7): "))
                end_col = int(input(f"{player.name}, enter end column (0-7): "))
                
                start_pos = Pair(start_row, start_col)
                end_pos = Pair(end_row, end_col)
                
                move = Move(start_pos, end_pos)
                
                if self._is_valid_move(player, move, board):
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 7.")

    def _algebraic_to_pair(self, algebraic: str) -> Pair:
        col = ord(algebraic[0].lower()) - ord('a')
        row = 8 - int(algebraic[1])
        return Pair(row, col)

    def _is_valid_move(self, player, move: Move, board) -> bool:
        piece = board.get_cell(move.source).get_piece()
        return piece in player.pieces.values() and move in piece.get_valid_moves(board)