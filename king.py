from tkinter.messagebox import RETRY
from xmlrpc.client import FastUnmarshaller

from piece import Piece

class King(Piece):

    def __init__(self, color):
       
        super().__init__(color)
        self.symbol = 'k'

    def makeMoves(self, input, output, board):

        start = self.convertMoves(input)
        end = self.convertMoves(output)

        startLine = start[1]
        startColumn = start[0]

        endLine = end[1]
        endColumn = end[0]

        game = board.game

        isPossible = False

        if (endLine == startLine - 1) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine - 1) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine - 1) and (endColumn == startColumn):

            isPossible = True

        else:

            isPossible = False



        if isPossible == True:

            if (game[endLine][endColumn] is not None
               and game[endLine][endColumn].color != self.color):

                game[startLine][startColumn] = None
                game[endLine][endColumn] = self

                return True

            elif (game[endLine][endColumn] is None):

                game[startLine][startColumn] = None
                game[endLine][endColumn] = self

                return True

            else:

                return False

        else:

            return False

    def isCheck(self, input, board, color):

        start = self.convertMoves(input)

        startLine = start[1]
        startColumn = start[0]

        position = self.findKing(board, color)
        endLine = position[0]
        endColumn = position[1]

        isPossible = False

        if (endLine == startLine - 1) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine - 1) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine - 1) and (endColumn == startColumn):

            isPossible = True

        else:

            isPossible = False

        return isPossible

    def findKing(self,board,color):

        for row in range(len(board.game)):

            for col in range(len(board.game[row])):

                if board.game[row][col] is not None:

                    if (board.game[row][col].color == color
                       and board.game[row][col].symbol == 'k'):

                            return [row,col]