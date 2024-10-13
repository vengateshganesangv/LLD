from common.board import Board
from common.cell import Cell
from common.pair import Pair
from common.move import Move
from common.piece import Piece

class ChessBoard(Board):
    def __init__(self):
        self.cells = [[Cell(Pair(i, j)) for j in range(8)] for i in range(8)]

    def apply_move(self, move: Move):
        source_cell = self.get_cell(move.source)
        dest_cell = self.get_cell(move.destination)
        piece: Piece = source_cell.get_piece()
        dest_cell.set_piece(piece)
        source_cell.set_piece(None)
        if piece:
            piece.move(move.destination)

    def display(self):
        for row in self.cells:
            for cell in row:
                piece = cell.get_piece()
                print(f"{piece.symbol if piece else '.'}", end=" ")
            print()
        print()

    def get_cell(self, position: Pair) -> Cell:
        return self.cells[position.x][position.y]

    def undo_move(self, move: Move):
        source_cell = self.get_cell(move.source)
        dest_cell = self.get_cell(move.destination)
        piece: Piece = dest_cell.get_piece()
        source_cell.set_piece(piece)
        dest_cell.set_piece(None)
        if piece:
            piece.move(move.source)