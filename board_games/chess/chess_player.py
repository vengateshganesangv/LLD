from chess.chess_board import ChessBoard
from common.piece import Piece
from common.player import Player
from common.color import Color
from common.pair import Pair
from common.move import Move
from chess.piece_factory import PieceFactory
from common.strategy import Strategy

class ChessPlayer(Player):
    def __init__(self, name: str, color: Color, strategy: Strategy):
        super().__init__(name, color, strategy)
        self.pieces : dict[str, Piece] = PieceFactory.create_all_pieces(color)

    def make_move(self, board):
        return self.strategy.make_move(self, board)

    def is_king_dead(self) -> bool:
        return self.pieces['K'].is_dead

    def get_king_position(self, board: ChessBoard):
        for row in range(8):
            for col in range(8):
                cell = board.get_cell(Pair(row, col))
                if cell.get_piece() == self.pieces['K']:
                    return cell.position
        return None

    def place_pieces(self, board: ChessBoard):
        for piece in self.pieces.values():
            board.get_cell(piece.position).set_piece(piece)

    def get_all_possible_moves(self, board):
        moves = []
        for piece in self.pieces.values():
            if not piece.is_dead:
                moves.extend(piece.get_valid_moves(board))
        return moves