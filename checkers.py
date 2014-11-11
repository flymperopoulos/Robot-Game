from checkerPiece import *

class Checkers(object):
    """
    	checkers Class
    """
    def __init__(self):
        self.board = {}
    
    def initialBoard(self):
        b = 0
        w = 0
        for i in range(1,9):
            for j in range(1,9):
                if (i == 1 or i == 3) and (j == 1 or j == 3 or j == 5 or j == 7):
                    self.board[(i,j)] = CheckerPiece("B", (i,j), str(b))
                    b+=1
                elif i == 2 and (j == 2 or j == 4 or j == 6 or j == 8):
                    self.board[(i,j)] = CheckerPiece("B", (i,j), str(b))
                    b+=1
                elif (i == 6 or i == 8) and (j == 2 or j == 4 or j == 6 or j == 8):
                    self.board[(i,j)] = CheckerPiece("W", (i,j), str(w))
                    w+=1
                elif i == 7 and (j == 1 or j == 3 or j == 5 or j == 7):
                    self.board[(i,j)] = CheckerPiece("W", (i,j),str(w))
                    w+=1
                else:
                    self.board[(i,j)] = 0

        return self.board

    def isCheckers(self):
    	return True

    def hasWin(self, player, board):
        if player == "B":
            for pieces in self.board.keys():
                if self.board[pieces] != 0:
                    if self.board[pieces].color == "W":
                        return False
            return True
        else:
            for pieces in self.board.keys():
                if self.board[pieces] != 0:
                    if self.board[pieces].color == "B":
                        return False
            return True

    def end(self):
        return False

    def move(self, piece, x, y):
        # sameMove = False
        # while not sameMove:
        pos = piece.position
        piece.position = (x,y)
        self.board[pos] = 0
        self.board[(x,y)] = piece
        piece_taken = 0
        if pos[1] - y == 2:
            if pos[0] - x == 2:
                piece_taken = self.board[(x+1,y+1)]
                self.board[(x+1,y+1)] = 0
            else:
                piece_taken = self.board[(x-1,y+1)]
                self.board[(x-1,y+1)] = 0
        elif pos[1] - y == -2:
            if pos[0] -x == 2:
                piece_taken = self.board[(x+1,y-1)]
                self.board[(x+1,y-1)] = 0
            else:
                piece_taken = self.board[(x-1,y-1)]
                self.board[(x-1,y-1)] = 0
        if piece_taken != 0:
            piece_taken.position = 0 
            # moves2 = piece.validateMoves()
                
        return self.board
