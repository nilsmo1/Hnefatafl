# Main program

from Board import Board
from Piece import Piece
from Colors import BLACK, WHITE
import pygame

def display_board(window: pygame.Surface, board: Board) -> None:
    pass 

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
        display_board(window, board)        
        pygame.display.update()


if __name__ == "__main__":
    main()

