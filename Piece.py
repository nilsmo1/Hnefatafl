# Piece class

from typing import Tuple

class Piece:
    def __init__(self, row: int,
                 col: int, role: str,
                 color: Tuple[int, int, int]) -> None:
        """
        Initializes a piece with a specified position, role and color.
        @ Parameters:
            row  : int
            col  : int
            role : str
            color: Tuple[int, int, int]
        @ Return:
            None
        """
        self.row   = row
        self.col   = col
        self.role  = role
        self.color = color
    
    def __repr__(self) -> str:
        """
        Representation of a piece is just the first character in the name of the role.
        @ Parameters:
            None
        @ Return:
            str
        """
        return self.role[:1]

    def get_pos(self) -> Tuple[int, int]:
        """
        Returns the position of a piece on the board
        @ Parameters:
            None
        @ Return:
            Tuple[int, int]
        """
        return (self.row, self.col)

    def set_pos(self, row: int, col: int) -> None:
        """
        Sets the positions of a piece on the board.
        @ Parameters:
            row: int
            col: int
        @ Return:
            None
        """
        self.row = row
        self.col = col

    def get_color(self) -> Tuple[int, int, int]:
        """
        Returns the color of a piece
        @ Parameters:
            None
        @ Return:
            Tuple[int, int, int]
        """
        return self.color

    def get_role(self) -> str:
        """
        Returns the role of a piece.
        @ Parameters:
            None
        @ Return:
            str
        """
        return self.role
