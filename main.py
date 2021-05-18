# Main program

from Board import Board
from Piece import Piece
from Colors import BLACK, WHITE, RED
import pygame
from typing import Tuple

def display_pieces(window: pygame.Surface,
                   window_size: Tuple[int, int],
                   board: Board) -> None:
    """
    Displays the pieces in the correct positions on the board.
    @ Params:
        window     : pygame.Surface
        window_size: Tuple[int,int]
        board      : Board
    @ Return:
        None
    """
    piece_radius = 20 
    margin = 100
    window_width, window_height = window_size
    board_width = window_width - 2 * margin
    size = board.get_size()
    current_board_state = board.get_state()
    position_size = int(board_width / size)
    offset = int(position_size / 2) + 2
    increment = lambda row: int(margin + offset + row * position_size)

    for row in range(size):
        for col in range(size):
            elem = current_board_state[row][col]
            if elem is not None:
                pygame.draw.circle(window, elem.get_color(),
                                  (increment(col), increment(row)), 
                                   piece_radius)


def display_board(window     : pygame.Surface,
                  window_size: Tuple[int, int],
                  board      : Board)-> None:
    """
    Displays the board in the pygame window.
    @ Parameters: 
        window     : pygame.Surface
        window_size: Tuple[int, int] 
        board      : Board
    @ Return:
        None
    """
    margin = 100
    window_width, window_height = window_size
    board_width = window_width - 2 * margin
    size = board.get_size()
    increment = lambda row: margin + row * board_width / size
    
    for row in range(size+1):
        pygame.draw.line(
            window, BLACK,
            (margin, increment(row)),
            (window_width - margin, increment(row)),2)

    for col in range(size+1):
        pygame.draw.line(
            window, BLACK,
            (increment(col), margin),
            (increment(col), window_width - margin),2)
    display_pieces(window, window_size, board)


def print_board(board: Board) -> None:
    """
    Prints a given "Board" object to stdout.
    @ Parameters: 
        board: Board
    @ Return:
        None
    """
    for row in board.get_state():
        row = ' '.join([str(pos) if pos != None else " " for pos in row])
        print(row)

def row_col_from_coordinates(board: Board,
                             window_size: Tuple[int, int],
                             coord_x: float, 
                             coord_y: float) -> Tuple[int, int]:
    """
    Returns the row and col of the board depending on given coordinates.
    @ Parameters:
        board      : Board
        window_size: Tuple[int, int] 
        coord_x    : float
        coord_y    : float
    @ Return:
        Tuple[int, int]
    """
    margin = 100
    window_width, _ = window_size
    relevant_board_start = margin
    relevant_board_end   = window_width - margin
    position_width = (window_width-2*margin) / board.get_size()
    row = (coord_y - 100) / position_width
    col = (coord_x - 100) / position_width
    return (int(row), int(col))

def move(window: pygame.Surface,
         window_size: Tuple[int, int],
         board: Board) -> Board:
    """
    Lets the player select a tile and then another tile to move a piece.
    @ Parameters:
        window     : pygame.Surface
        window_size: Tuple[int, int]
        board      : Board
    @ Return:
        Board
    """
    done_selecting = False
    fully_done = False
    while not fully_done:
        while not done_selecting:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key  == pygame.K_q
                ): quit()

                if pygame.mouse.get_pressed()[0]:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    row, col = row_col_from_coordinates(board, window_size, mouse_x, mouse_y)
                    print(f"First (row: {row}, col: {col})")
                    done_selecting = True

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key  == pygame.K_q
                ): quit()

            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                new_row, new_col = row_col_from_coordinates(board, window_size, mouse_x, mouse_y)
                if board.validate_move(row, col, new_row, new_col):
                    print(f"Second: row: {new_row} col: {new_col}")
                    fully_done = True
                else:
                    print(f"ILLEGAL MOVE: {row, col} -> {new_row,new_col}, try again!")
            elif pygame.mouse.get_pressed()[2]:
                done_selecting = False
    board.move(row, col, new_row, new_col)
    return board

        
def main() -> None:
    """
    Main function for Hnefatafl
    @ Parameters:
        None
    @ Return:
        None
    """
    pygame.init()
    window_size = (800,800)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Hnefatafl")
    
    board = Board(11)
    board.init_board()
    print_board(board)
    window.fill(WHITE)
    display_board(window, window_size, board)
    pygame.display.update()
    turn = 1
    Running = True
    # Press Q or the close the window to exit
    while Running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key  == pygame.K_q
                ): quit()
        player = (BLACK*(turn % 2)) or (WHITE*(1+turn % 2))
        if board.game_over():
            print(f"{('BLACK'*(turn % 2)) or ('WHITE'*(1+turn % 2))} WINS")
            quit()
        window.fill(WHITE)
        board = move(window, window_size, board)
        display_board(window, window_size, board)
        pygame.display.update()


if __name__ == "__main__":
    main()
