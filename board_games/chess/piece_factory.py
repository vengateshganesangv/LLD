from common.color import Color
from common.pair import Pair
from chess.pieces.pawn import Pawn
from chess.pieces.rook import Rook
from chess.pieces.knight import Knight
from chess.pieces.bishop import Bishop
from chess.pieces.queen import Queen
from chess.pieces.king import King
from common.piece import Piece

class PieceFactory:
    @staticmethod
    def create_all_pieces(color: Color) -> dict[str, Piece]:
        row = 0 if color == Color.WHITE else 7
        pieces = {}
        
        # Pawns
        pawn_row = 1 if color == Color.WHITE else 6
        for i in range(8):
            pieces[f'P{i+1}'] = Pawn(color, Pair(pawn_row, i))
        
        # Rooks
        pieces['R1'] = Rook(color, Pair(row, 0))
        pieces['R2'] = Rook(color, Pair(row, 7))
        
        # Knights
        pieces['N1'] = Knight(color, Pair(row, 1))
        pieces['N2'] = Knight(color, Pair(row, 6))
        
        # Bishops
        pieces['B1'] = Bishop(color, Pair(row, 2))
        pieces['B2'] = Bishop(color, Pair(row, 5))
        
        # Queen
        pieces['Q'] = Queen(color, Pair(row, 3))
        
        # King
        pieces['K'] = King(color, Pair(row, 4))
        
        return pieces