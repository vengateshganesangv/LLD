from collections import deque
from common.game import Game
from chess.chess_board import ChessBoard
from chess.chess_player import ChessPlayer

class Chess(Game):
    def __init__(self, first_player: ChessPlayer, second_player: ChessPlayer):
        board = ChessBoard()
        players = deque([first_player, second_player])
        super().__init__(players, board)
        self.prepare_board()

    def start(self):
        while not self.is_over():
            self.board.display()
            current_player = self.players[0]
            move = current_player.make_move(self.board)
            self.board.apply_move(move)
            if self.is_over():
                print(f"Game over! {current_player.name} is the winner!")
                break
            self.players.rotate(-1)
        self.board.display()

    def is_over(self) -> bool:
        return any(player.is_king_dead() for player in self.players)

    def prepare_board(self):
        for player in self.players:
            player.place_pieces(self.board)

    def is_checkmate(self, player: ChessPlayer) -> bool:
        if not self.is_in_check(player):
            return False
        return all(self.results_in_check(player, move) for move in player.get_all_possible_moves(self.board))

    def is_in_check(self, player: ChessPlayer) -> bool:
        king_position = player.get_king_position(self.board)
        opponent = self.players[1] if player == self.players[0] else self.players[0]
        return any(piece.can_attack(self.board, king_position) for piece in opponent.pieces.values() if not piece.is_dead)

    def results_in_check(self, player: ChessPlayer, move):
        self.board.apply_move(move)
        in_check = self.is_in_check(player)
        self.board.undo_move(move)
        return in_check