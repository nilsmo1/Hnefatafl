# Main program

from Board import Board
from Piece import Piece
import pygame

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
    # Pygame init and window init
    pygame.init()
    window_size = (800,800)
    window = pygame.display.set_mode(window_size)
    
    board = Board(11)
    board.init_board()
    print_board(board)
    
    Running = True
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False




main()
