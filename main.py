from BoardInitialize import Board
from pawn import Pawn
from queen import Queen
from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King

def main():
    board = Board()

    # Try to move the white rook at bottom-left
    print("\nAttempting move: a1 → h8")

    bishop = board.game[7][2] # white rook at a1
    queen = Queen("white")
    b2bishop = Bishop("black")
    board.game[7][0] = queen
    board.game[6][1] = None
    board.game[0][7] = None
    board.game[1][6] =  None

    print("Initial Board:")
    board.displayBoard()

    move_result= queen.makeMoves("a1","h8", board)

    if move_result is False:
        print("Move blocked!")
    else:
        print("Move successful!")

    board.displayBoard()

main()

