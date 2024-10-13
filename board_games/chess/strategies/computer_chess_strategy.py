import random
from common.strategy import Strategy
from common.move import Move

class ComputerChessStrategy(Strategy):
    def make_move(self, player, board) -> Move:
        all_moves = []
        for piece in player.pieces.values():
            if not piece.is_dead:
                valid_moves = piece.get_valid_moves(board)
                valid_moves = [move for move in valid_moves if self._is_within_board(move)]
                all_moves.extend(valid_moves)
        
        if all_moves:
            return random.choice(all_moves)
        else:
            raise ValueError("No valid moves available")

    def _is_within_board(self, move: Move) -> bool:
        return 0 <= move.source.x <= 7 and 0 <= move.source.y <= 7 and \
               0 <= move.destination.x <= 7 and 0 <= move.destination.y <= 7