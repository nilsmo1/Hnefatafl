# Board class

from Colors import BLACK, LIGHT_GRAY, OFFWHITE
from Piece import Piece
from typing import List, Union

class Board:
    """ 
    Hnefatafl Board
    """
    def __init__(self, size: int) -> None:
        """
        Initialize a board with desired size.
        @ Parameters: 
            size: int (side length of a square board)
        @ Return:
            None
        """
        self.size  = size
        self.board = []

    def init_board(self) -> None:
        """
        Place pieces on the board in a starting configuration.
        @ Parameters: 
            None
        @ Return:
            None
        """
        RAW = list("""
        . . . B B B B B . . .
        . . . . . B . . . . .
        . . . . . . . . . . .
        B . . . . W . . . . B
        B . . . W W W . . . B
        B B . W W K W W . B B
        B . . . W W W . . . B
        B . . . . W . . . . B
        . . . . . . . . . . .
        . . . . . B . . . . .
        . . . B B B B B . . .""".replace(" ","").split("\n")[1:])
        board = [list(row.strip()) for row in RAW]
        
        for i,row in enumerate(board):
            for j,pos in enumerate(row):
                if   pos == "B": board[i][j] = Piece(i,j,"BLACK", BLACK)
                elif pos == "W": board[i][j] = Piece(i,j,"WHITE", OFFWHITE)
                elif pos == "K": board[i][j] = Piece(i,j,"KING" , LIGHT_GRAY)
                else           : board[i][j] = None

        self.board = board

    def get_state(self) -> List[Union[None, Piece]]:
        """
        Returns the current state of the board.
        @ Parameters:
            None
        @ Return:
            List[Union[None, Piece]]
        """
        return self.board

    def get_size(self) -> int:
        """
        Returns the size of the side length of the board.
        @ Parameters:
            None
        @ Return:
            int
        """
        return self.size
