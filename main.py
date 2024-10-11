from game import OthelloGame
from board import OthelloBoard
from player import HumanPlayer

if __name__=='__main__':
    board = OthelloBoard()
    player_x = HumanPlayer(board)
    player_y = HumanPlayer(board)
    game = OthelloGame(board, player_x, player_y)
    game.start_game()