from common.piece import Piece
from common.color import Color
from common.pair import Pair
from common.move import Move

class Bishop(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for dir_x, dir_y in directions:
            for i in range(1, 8):
                new_x, new_y = self.position.x + i*dir_x, self.position.y + i*dir_y
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    new_pos = Pair(new_x, new_y)
                    piece = board.get_cell(new_pos).get_piece()
                    if piece is None:
                        moves.append(Move(self.position, new_pos))
                    elif piece.color != self.color:
                        moves.append(Move(self.position, new_pos))
                        break
                    else:
                        break
                else:
                    break
        
        return moves

    def can_attack(self, board, position: Pair) -> bool:
        dx, dy = abs(self.position.x - position.x), abs(self.position.y - position.y)
        return dx == dy

    @property
    def symbol(self) -> str:
        return 'B' if self.color == Color.WHITE else 'b'