# Piece class

from typing import Tuple

class Piece:
    def __init__(self, row: int,
                 col: int, role: str,
                 color: Tuple[int,int,int]) -> None:
        self.row   = row
        self.col   = col
        self.role  = role
        self.color = color
    
    def __repr__(self) -> str:
        return self.role[:1]

    def get_pos(self) -> Tuple[int,int]:
        return (self.row, self.col)

    def set_pos(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def get_color(self) -> Tuple[int, int, int]:
        return self.color
