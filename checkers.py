from pieces import *

class Checkers(object):
    """
    	checkers Class
    """
    def __init__(self):
        self.board = {}
        self.DIR =  {'ul':(-1,-1),
                'ur':(1,-1),
                'dl':(-1,1),
                'dr':(1,1)}
    
    def make_buf(self,brd):
        new_brd = dict(brd)
        for key in brd:
            if brd[key]!=0:
                new_brd[key] = CheckerPiece(brd[key].color,key,brd[key].number)
            else: 
                new_brd[key] = 0
        self.board = new_brd
        return new_brd
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

    def move(self, piece, x, y, jumps):
        pos = piece.position()
        piece._position = (x,y)
        self.board[pos] = 0
        self.board[(x,y)] = piece
        if piece.color == 'B':
            if x == 8:
                piece._isKing = True
        else:
            if x == 1:
                piece._isKing = True
        if abs(pos[0]-x) != 1:
            if jumps != []:
                for tup in jumps:
                    self.board[tup] = 0
                
        return self.board

