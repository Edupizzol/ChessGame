from piece import Piece

class Pawn(Piece):

    def __init__(self,color):
            
        super().__init__(color)
        self.symbol = 'p'
        self.has_moved = False

    #@override
    def makeMoves(self,input,output,board):

        start = self.convertMoves(input)
        end = self.convertMoves(output)

        startLine = start[1]
        startColumn = start[0]

        endLine = end[1]
        endColumn = end[0]

        game = board.game

        size = len(board.game)

        if not (0 <= endLine < size and 0 <= endColumn < size):
            return False

        if self.color == 'white':

            if (startColumn == endColumn 
            and (startLine - 2) == endLine
            and self.has_moved == False  
            and game[startLine - 1][startColumn] is None
            and game[endLine][endColumn] is None):
                
                game[endLine][endColumn] = self
                game[startLine][startColumn] = None
                self.has_moved = True

                return True 

            elif (startColumn == endColumn
                and (startLine - 1) == endLine
                and game[endLine][endColumn] is None):
                
                    game[endLine][endColumn] = self
                    game[startLine][startColumn] = None
                    self.has_moved = True

                    return True
            
            elif ((startColumn - 1 == endColumn or startColumn + 1 == endColumn)
                and endLine == startLine - 1
                and game[endLine][endColumn] is not None
                and game[endLine][endColumn].color != self.color):

                    game[endLine][endColumn] = self
                    game[startLine][startColumn] = None
                    self.has_moved = True

                    return True
        
            else:
                
                #movimento inválido
                return False

        elif self.color == 'black':

            if (startColumn == endColumn 
            and (startLine + 2) == endLine
            and self.has_moved == False 
            and game[startLine + 1][startColumn] is None
            and game[endLine][endColumn] is None):
                
                game[endLine][endColumn] = self
                game[startLine][startColumn] = None
                self.has_moved = True

                return True 

            elif (startColumn == endColumn
                and (startLine + 1) == endLine
                and game[endLine][endColumn] is None):
                
                    game[endLine][endColumn] = self
                    game[startLine][startColumn] = None
                    self.has_moved = True

                    return True
            
            elif ((startColumn + 1 == endColumn or startColumn - 1 == endColumn)
                and endLine == startLine + 1
                and game[endLine][endColumn] is not None
                and game[endLine][endColumn].color != self.color):

                    game[endLine][endColumn] = self
                    game[startLine][startColumn] = None
                    self.has_moved = True

                    return True
        
            else:
                
                #movimento inválido
                return False

        