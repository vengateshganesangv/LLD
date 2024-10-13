from common.pair import Pair

class Cell:
    def __init__(self, position: Pair):
        self.position = position
        self.piece = None

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece