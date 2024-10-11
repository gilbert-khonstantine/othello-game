from board import OthelloBoard
from player import Player

class OthelloGame:
    round_number = 0
    def __init__(self, board: OthelloBoard, player_x: Player, player_y: Player):
        self.board = board
        self.player_x = player_x
        self.player_y = player_y

    def is_finished(self) -> bool:
        return self.board.is_full()
    
    def start_game(self):
        while not self.is_finished():
            OthelloGame.round_number += 1
            print(self.board)
            player_label = Player.player_turn(OthelloGame.round_number)
            player = self.player_x if player_label == 'X' else self.player_y
            player_input = str(input("Player "+ player_label + "'s turn, enter your move (e.g. D4, A1):"))
            while not player.valid_move(player_input):
                print("Invalid move, please try again!")
                player_input = str(input("Player "+ player_label + "'s turn, enter your move (e.g. D4, A1):"))
            self.board = player.apply_move(player_input)