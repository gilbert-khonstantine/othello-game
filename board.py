from typing import List

class OthelloBoard:
    def __init__(self):
        self.BOARD_SIZE : int = 8
        self.BOARD_COLUMN : List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.BOARD_ROW : List[str] = ['1','2','3','4','5','6','7','8']
        self.state : List[List[str]] = [['_'] * self.BOARD_SIZE] * self.BOARD_SIZE
        pass

    def is_full(self):
        # TODO
        return False

    def __str__(self) -> str:
        board_representation : str = ""
        for col in self.BOARD_COLUMN:
            board_representation += ("  " + col + ("" if col != 'H' else "\n"))
        for idx in range(self.BOARD_SIZE):
            board_representation+=("  ".join(self.BOARD_ROW[idx]) + " ")
            board_representation+=("  ".join(self.state[idx]) + "\n")
        return board_representation