from BoardInitialize import Board
from pawn import Pawn
from queen import Queen
from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King

def main():
    board = Board()
    board.game = [[None for _ in range(8)] for _ in range(8)]

    # Place white king at e4 (coordinates [4][4])
    w_king = King("white")
    board.game[4][4] = w_king

    # Place black king at d5 (adjacent diagonally)
    b_king = King("black")
    board.game[3][3] = b_king

    print("Initial Board:")
    board.displayBoard()

    # Test if black king threatens the white king
    if b_king.isCheck("d5", board, "white"):
        print("✅ Check detected! (Black king threatens White king)")
    else:
        print("❌ No check.")

main()
