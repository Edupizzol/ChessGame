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

            elif (game[endLine][endColumn] is None):

                game[startLine][startColumn] = None
                game[endLine][endColumn] = self

            else:

                return False

        else:

            return False