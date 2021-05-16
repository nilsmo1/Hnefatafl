# Piece class

#from Typing import Tuple

class Piece:
    def __init__(self, row: int, col: int, role: str) -> None:
        self.row  = row
        self.col  = col
        self.role = role
    
    def __repr__(self) -> str:
        return self.role[:1]

    def get_pos(self) -> (int,int):
        return (self.row, self.col)

    def set_pos(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
