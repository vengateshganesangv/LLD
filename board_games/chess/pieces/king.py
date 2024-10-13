from common.piece import Piece
from common.color import Color
from common.pair import Pair
from common.move import Move

class King(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for dir_x, dir_y in directions:
            new_x, new_y = self.position.x + dir_x, self.position.y + dir_y
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                new_pos = Pair(new_x, new_y)
                piece = board.get_cell(new_pos).get_piece()
                if piece is None or piece.color != self.color:
                    moves.append(Move(self.position, new_pos))
        
        return moves

    def can_attack(self, board, position: Pair) -> bool:
        dx, dy = abs(self.position.x - position.x), abs(self.position.y - position.y)
        return dx <= 1 and dy <= 1

    @property
    def symbol(self) -> str:
        return 'K' if self.color == Color.WHITE else 'k'