from board import OthelloBoard
from typing import List

class Player:
    def __init__(self, board: OthelloBoard):
        self.board = board
        pass
    def possible_moves(self, player_label: str) -> List[str]:
        return []
    
    def apply_move(self, player_input: str) -> OthelloBoard:
        return self.board
    
    def valid_move(self, player_input: str) -> bool:
        return player_input in self.possible_moves(player_input)
    
    def player_turn(round_number: int):
        return 'X' if round_number % 2 ==1 else 'O'

class HumanPlayer(Player):
    def __str__(self):
        return "Human Player"

class MiniMaxPlayer(Player):
    def __str__(self):
        return "Minimax AI Player"