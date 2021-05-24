# Main program

from Board import Board
from Colors import BLACK, WHITE, RED, HIGHLIGHT, BACKGROUND
from Piece import Piece
import pygame
from typing import Tuple

def display_turn(window: pygame.Surface, 
                 window_size: Tuple[int, int],
                 turn: str) -> None:
    """
    Function that displays the current players turn so 
    that it is easier to distinguish who's turn it is.
    @ Parameters: 
        window     : pygame.Surface
        window_size: Tuple[int, int]
        turn       : str
    @ Return:
        None
    """
    window_width, _ = window_size
    font = pygame.font.SysFont("Comic Sans MS", 50)
    text = font.render(turn, False, BLACK)
    window.blit(text, (window_width/2-60,30))


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
                                   piece_radius, 10)


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
    board_background_color = BACKGROUND
    board_background_surface = pygame.Surface((board_width, board_width), pygame.SRCALPHA)
    board_background_surface.fill(board_background_color)
    window.blit(board_background_surface, (margin,margin))
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
    print()
    for row in board.get_state():
        row = '\t'+' '.join([str(pos) if pos != None else " " for pos in row])
        print(row)
    print()

def coords_in_bounds(window_size: Tuple[int, int], coord_x: int, coord_y: int) -> bool:
    """
    Checks if the given coordinates are on the board.
    @ Parameters:
        window_size: Tuple[int, int]
        coord_x    : int
        coord_y    : int
    @ Return:
        bool
    """
    margin = 100
    window_width, window_height = window_size
    in_bounds_x = margin < coord_x < window_width-margin
    in_bounds_y = margin < coord_y < window_height-margin
    return in_bounds_x and in_bounds_y


def row_col_to_coordinates(board: Board, 
                           window_size: Tuple[int, int],
                           row: int, col: int) -> Tuple[int, int, int]:
    """
    Converts a row and a column to a tuple of coordinates and a position size
    to highlight the selected piece.
    @ Parameters:
        board      : Board
        window_size: Tuple[int, int, int]
        row        : int
        col        : int
    @ Return:
        Tuple[int, int]
    """
    margin = 100
    window_width, window_height = window_size
    board_rows = board.get_size()
    position_width = (window_width-2*margin)/board_rows
    coord_y = margin + position_width*row
    coord_x = margin + position_width*col
    return (coord_x+1, coord_y+1, position_width)


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
    row = (coord_y - margin) / position_width
    col = (coord_x - margin) / position_width
    return (int(row), int(col))

def move(window: pygame.Surface,
         window_size: Tuple[int, int],
         board: Board,
         player: str) -> Board:
         
    """
    Lets the player select a tile and then another tile to move a piece.
    @ Parameters:
        window     : pygame.Surface
        window_size: Tuple[int, int]
        board      : Board
        player     : str
    @ Return:
        Board
    """
    done_selecting = False
    fully_done = False
    current_board_state = board.get_state()
    while not fully_done:
        while not done_selecting:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key  == pygame.K_q
                ): quit()
                window.fill(WHITE)
                display_turn(window, window_size, player)
                display_board(window, window_size, board)
                pygame.display.update()
                if pygame.mouse.get_pressed()[0]:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if not coords_in_bounds(window_size, mouse_x, mouse_y):
                        print(f"Mouse coordinates are not on the board!")
                        continue
                    
                    row, col = row_col_from_coordinates(board, window_size, mouse_x, mouse_y)
                    if not board.occupied(row, col):
                        print(f"Cannot select empty slot!")
                        continue
                    elif current_board_state[row][col].get_role() == "KING" and player != "BLACK":
                        pass
                    elif current_board_state[row][col].get_role() != player:
                        print(f"{player} has the turn!")
                        continue
                    print(f"First  : row: {row}, col: {col}")
                    coord_x, coord_y, position_width = row_col_to_coordinates(board, window_size, row, col)
                    highlighter = pygame.Surface((position_width, position_width))
                    highlighter.fill(HIGHLIGHT)
                    window.blit(highlighter,(coord_x, coord_y))
                    display_board(window, window_size, board)
                    pygame.display.update()
                    done_selecting = True

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key  == pygame.K_q
                ): quit()

            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if not coords_in_bounds(window_size, mouse_x, mouse_y):
                    print("Mouse coordinates are not on the board!")
                    continue
                new_row, new_col = row_col_from_coordinates(board, window_size, mouse_x, mouse_y)
                if not board.validate_move(row, col, new_row, new_col):
                    print(f"ILLEGAL MOVE: {row, col} -> {new_row,new_col}, try again!")
                    continue
                print(f"Second : row: {new_row}, col: {new_col}")
                fully_done = True
            elif pygame.mouse.get_pressed()[2]:
                done_selecting = False
    board.move(row, col, new_row, new_col)
    board.capture(new_row, new_col, player)
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
    pygame.font.init() 

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
        player = ("BLACK"*((1+turn) % 2)) or ("WHITE"*(turn % 2))
        window.fill(WHITE)
        board = move(window, window_size, board, player)
        if board.king_has_moved():
            board.place_blocking_piece()
        window.fill(WHITE)
        display_board(window, window_size, board)
        pygame.display.update()
        if board.game_over() != None:
            print(f"{player} WINS")
            quit()
        turn+=1

if __name__ == "__main__":
    main()
