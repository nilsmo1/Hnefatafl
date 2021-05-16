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
    
    def occupied(self, row: int, col: int) -> bool:
        """
        Sees if a given cell is occupied or empty.
        @ Parameters:
            row: int
            col: int
        @ Return:
            bool
        """
        return self.board[row][col] != None

    def validate_move(self, row: int, col: int, new_row: int, new_col: int) -> bool:
        """
        Validates a move so that illegal moves are ignored.
        @ Parameters:
            row    : int
            col    : int
            new_row: int
            new_col: int
        @ Return:
            bool
        """
        same_row_or_same_col = (row == new_row) ^ (col == new_col)
        return same_row_or_same_col and not self.occupied(new_row, new_col)


    def move(self, row, col, new_row, new_col) -> None:
        """
        Moves a piece on the board
        @ Parameters:
            row    : int
            col    : int
            new_row: int
            new_col: int
        @ Return:
            None
        """
        if self.validate_move(row, col, new_row, new_col):
            tmp_row, tmp_col = row, col
            self.board[new_row][new_col] = self.board[row][col]
            self.board[tmp_row][tmp_col] = None
