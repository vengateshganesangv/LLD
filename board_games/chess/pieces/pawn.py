from common.piece import Piece
from common.color import Color
from common.pair import Pair
from common.move import Move

class Pawn(Piece):
    def __init__(self, color: Color, position: Pair):
        super().__init__(color, position)
        self.first_move = True

    def get_valid_moves(self, board):
        moves = []
        direction = 1 if self.color == Color.WHITE else 1
        front = Pair(self.position.x + direction, self.position.y)
        
        if 0 <= front.x < 8 and board.get_cell(front).get_piece() is None:
            moves.append(Move(self.position, front))
            if self.first_move:
                double_front = Pair(self.position.x + 2*direction, self.position.y)
                if board.get_cell(double_front).get_piece() is None:
                    moves.append(Move(self.position, double_front))
        
        # Capture moves
        for offset in [-1, 1]:
            capture = Pair(self.position.x + direction, self.position.y + offset)
            if 0 <= capture.x < 8 and 0 <= capture.y < 8:
                piece = board.get_cell(capture).get_piece()
                if piece and piece.color != self.color:
                    moves.append(Move(self.position, capture))
        
        return moves

    def can_attack(self, board, position: Pair) -> bool:
        direction = -1 if self.color == Color.WHITE else 1
        dx, dy = position.x - self.position.x, position.y - self.position.y
        return dx == direction and abs(dy) == 1

    def move(self, new_position: Pair):
        super().move(new_position)
        self.first_move = False

    @property
    def symbol(self) -> str:
        return 'P' if self.color == Color.WHITE else 'p'