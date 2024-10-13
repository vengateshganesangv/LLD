from chess.chess_game import Chess
from chess.chess_player import ChessPlayer
from common.color import Color
from chess.strategies.human_chess_strategy import HumanChessStrategy
from chess.strategies.computer_chess_strategy import ComputerChessStrategy

def main():
    player1 = ChessPlayer("Player 1", Color.WHITE, HumanChessStrategy())
    player2 = ChessPlayer("Player 2", Color.BLACK, ComputerChessStrategy())
    
    chess_game = Chess(player1, player2)
    chess_game.start()

if __name__ == "__main__":
    main()