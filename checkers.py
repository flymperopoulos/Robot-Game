import checkerPiece

class checkers:
    """
    	checkers Class
    """
    def __init__(self):
        self.board = {}
    
    def initialBoard(self):
        for i in range(1,9):
            for j in range(1,9):
                if (i == 1 or i == 3) and (j == 1 or j == 3 or j == 5 or j == 7):
                    self.board[(i,j)] = checkerPiece("B", (i,j))
                if i == 2 and (j == 2 or j == 4 or j == 6 or j == 8):
                    self.board[(i,j)] = checkerPiece("B", (i,j))
                if (i == 6 or i == 8) and (j == 2 or j == 4 or j == 6 or j == 8):
                    self.board[(i,j)] = checkerPiece("W", (i,j))
                if i == 7 and (j == 1 or j == 3 or j == 5 or j == 7):
                    self.board[(i,j)] = checkerPiece("W", (i,j))
                else:
                    self.board[(i,j)] = 0

    	

    def isCheckers(self):
    	return True

    def hasWin(self, player, board):
        if player == "B":
            for pieces in board.keys():
                if self.board.get(pieces).color == "W":
                    return False
                else:
                    return True
        else:
            for pieces in self.board.keys():
                if self.board.get(pieces).color == "B":
                    return False
                else:
                    return True