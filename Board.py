# Board class

from Colors import BLACK, LIGHT_GRAY, OFFWHITE, WHITE, YELLOW, BLOCKER
from Piece import Piece
from typing import List, Union, Tuple

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
        self.king_move_flag = False

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

        RAW_TEST_BOARD_TEMPLATE = list("""
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .""".replace(" ","").split("\n")[1:])
        
        board = [list(row.strip()) for row in RAW]
        
        for i,row in enumerate(board):
            for j,pos in enumerate(row):
                if   pos == "B": board[i][j] = Piece(i,j,"BLACK", BLACK)
                elif pos == "W": board[i][j] = Piece(i,j,"WHITE", WHITE)
                elif pos == "K": board[i][j] = Piece(i,j,"KING" , YELLOW)
                else           : board[i][j] = None

        self.board = board


    def king_has_moved(self) -> bool:
        """
        If the king has moved, a blocking piece should be put in the middle
        because no piece is supposed to be able to that spot.
        @ Parameters:
            None
        @ Return:
            Bool
        """
        row = col = self.size//2
        if self.king_move_flag != False:
            return False
        if self.board[row][col] == None:
            print(f"self.board[row][col] == None")
            self.king_move_flag = True
            return True
        elif self.board[row][col].get_role() == "BLOCKER":
            print("return blockerstatus")
            return False
        

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
   
    def in_bounds(self, row: int, col: int) -> bool:
        """
        Checks if a position is on the board or not.
        @ Parameters:
            row: int
            col: int
        @ Return:
            bool
        """
        return 0 <= row < self.size and 0 <= col < self.size

    
    def clear_path(self, row: int, col: int, new_row: int, new_col: int) -> bool:
        """
        Determines if the move is valid or not,
        depending on if there are any blocking pieces in the way.
        @ Parameters:
            row    : int
            col    : int
            new_row: int
            new_col: int
        @ Return:
            bool
        """
        if row != new_row:
            min_row, max_row = min(row,new_row), max(row,new_row)
            for row_index in range(min_row+1, max_row):
                if self.board[row_index][col] != None:
                    return False
        if col != new_col:
            min_col, max_col = min(col,new_col), max(col,new_col)
            for col_index in range(min_col+1, max_col):
                if self.board[row][col_index] != None:
                    return False
        return True

    
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
        invalid_positions = [(self.size-1, 0), (0, self.size-1),
                             (0,0),(self.size-1, self.size-1)]
        same_row_or_same_col = (row == new_row) ^ (col == new_col)
        if self.board[row][col] != None:
            if self.board[row][col].get_role() == "KING":
                return (same_row_or_same_col and not 
                        self.occupied(new_row, new_col) and 
                        self.in_bounds(new_row, new_col) and
                        self.clear_path(row, col, new_row, new_col))
            
        return (same_row_or_same_col and not 
                self.occupied(new_row, new_col) and 
                self.in_bounds(new_row, new_col) and
                self.clear_path(row, col, new_row, new_col) and
                (new_row,new_col) not in invalid_positions)


    def move(self, row: int, col: int, new_row: int, new_col: int) -> None:
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


    def capture(self, row: int, col: int, role: str) -> None:
        """
        Checks if piece is captured after a move.
        @ Parameters:
            row : int
            col : int
            role: str
        @ Return:
            None
        """
        for row_offset, col_offset in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_row, new_col = row+row_offset, col+col_offset
            if not self.in_bounds(new_row, new_col):
                continue
            piece = lambda r,c: self.board[r][c] if self.in_bounds(r,c) else None
            if piece(new_row, new_col) != None: 
                if piece(new_row, new_col).get_role() not in [role,"KING", "BLOCKER"]:
                    if piece(new_row+row_offset, new_col+col_offset) != None:
                        if (piece(new_row+row_offset, new_col+col_offset).get_role() == "KING" and 
                            role == "WHITE"):
                            print(f"{role} captured an opponent at: row: {new_row}, col: {new_col}")
                            self.board[new_row][new_col] = None
                        elif piece(new_row+row_offset, new_col+col_offset).get_role() == role:
                            print(f"{role} captured an opponent at: row: {new_row}, col: {new_col}")
                            self.board[new_row][new_col] = None


    def place_blocking_piece(self) -> None:
        """
        Puts a blocking piece in the middle of the board (used after calling 'king_has_moved'.
        @ Parameters:
            None
        @ Return:
            None
        """
        row = col = self.size//2
        self.board[row][col] = Piece(row, col, "BLOCKER", BLOCKER)
        print("sucessfull placement of blocker!\n\n")


    def game_over(self) -> Tuple[int, int, int]:
        """
        Checks if the board is in a state where one of the teams has won.
        Returns a color depending on which team won.
        @ Parameters:
            None
        @ Return:
            Tuple[int, int, int]
        """
        corners = [(self.size-1, 0), (0, self.size-1), (0,0)]
        for row, col in corners:
            pos = self.board[row][col]
            if pos != None:
                if pos.get_role() == "KING":
                    return WHITE
        # TODO: make win-conditions for BLACK team

        
