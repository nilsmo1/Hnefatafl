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
    
    board = Board(11)
    board.init_board()
    print_board(board)
    Running = True
    # Press Q or the close the window to exit
    while Running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key  == pygame.K_q
                ): Running = False
        window.fill(WHITE)
        display_board(window, window_size, board)        
        pygame.display.update()


if __name__ == "__main__":
    main()

