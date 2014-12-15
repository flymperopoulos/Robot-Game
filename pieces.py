from checkers import *

class CheckerPiece(object):
    """
        checkerPiece that determines has an attribut if it is white or B and returns all possible moves
    """
    

    def __init__(self, color, position, number):
        self.color = color
        self.number = number
        self.name = color + number
        self._position = position
        self._isKing = False
        self._possibleMoves = []
        self.DIR =  {'ul':(-1,-1),
            'ur':(1,-1),
            'dl':(-1,1),
            'dr':(1,1)}

    def position(self):
        return self._position

    def isKing(self):
        return self._isKing

    def possibleMoves(self, brd):
        print self._position
        if self._position == 0:
            return None
        else:
            x,y = self._position
            moves = []
            jumps = []
            moves,jumps = self.jump2(brd,x,y,moves,jumps)
            print moves
            for key in self.DIR:
                nx = x+self.DIR[key][0]
                ny = y + self.DIR[key][1]
                print (nx, ny)
                if nx>0 and ny>0 and nx<9 and ny<9:
                    if brd[(nx,ny)] == 0: 
                        moves.append((nx,ny))
            return moves, jumps

    def jump(self, brd, x, y, moves,jumps):
        
        for key in self.DIR:
            nx = x+self.DIR[key][0]
            ny = y + self.DIR[key][1]
            if nx>0 and ny>0 and nx<9 and ny<9:
                if (nx,ny) in jumps:
                    pass
                elif brd[(nx,ny)] != 0:
                    if brd[(nx,ny)] != self.color:
                        if  nx+self.DIR[key][0]>0 and ny+self.DIR[key][1]>0 and nx+self.DIR[key][0]<9 and ny+self.DIR[key][1]<9:
                            if brd[nx+self.DIR[key][0],ny+self.DIR[key][1]] in moves:
                                pass
                            else:
                                if brd[nx+self.DIR[key][0],ny+self.DIR[key][1]] == 0: 
                                    moves,jumps = self.jump(brd,nx+self.DIR[key][0],ny+ self.DIR[key][1],moves,jumps)
                                    moves.append((nx+self.DIR[key][0],ny+ self.DIR[key][1]))
                                    jumps.append((nx,ny))
        return moves, jumps
        
    def jump2(self, brd,x,y, moves,jumps):
        for key in self.DIR:
            nx = x+self.DIR[key][0]
            ny = y + self.DIR[key][1]
            if nx>0 and ny>0 and nx<9 and ny<9:
                if (nx,ny) in jumps:
                    pass
                elif brd[(nx,ny)] != 0:
                    if brd[(nx,ny).color] != self.color:
                        if nx+self.DIR[key][0]>0 and ny+self.DIR[key][1]>0 and nx+self.DIR[key][0]<9 and ny+self.DIR[key][1]<9:
                            if brd[nx+self.DIR[key][0],ny+self.DIR[key][1]] == 0: 
                                moves.append((nx+self.DIR[key][0],ny+ self.DIR[key][1]))
                                jumps.append((nx,ny))
                                for key in self.DIR:
                                    nnx = nx+self.DIR[key][0]
                                    nny = ny + self.DIR[key][1]
                                    if nnx>0 and nny>0 and nnx<9 and nny<9:
                                        if (nnx,nny) in jumps:
                                            pass
                                        elif brd[(nnx,nny)] != 0:
                                            if brd[(nnx,nny)] != self.color:
                                                if nnx+self.DIR[key][0]>0 and nny+self.DIR[key][1]>0 and nnx+self.DIR[key][0]<9 and nny+self.DIR[key][1]<9:
                                                    if brd[nnx+self.DIR[key][0],nny+self.DIR[key][1]] == 0: 
                                                        moves.append((nnx+self.DIR[key][0],nny+ self.DIR[key][1]))
                                                        jumps.append((nnx,nny))
                                                        for key in self.DIR:
                                                            nnnx = nnx+self.DIR[key][0]
                                                            nnny = nny + self.DIR[key][1]
                                                            if nnnx>0 and nnny>0 and nnnx<9 and nnny<9:
                                                                if (nnnx,nnny) in jumps:
                                                                    pass
                                                                elif brd[(nnnx,nnny)] != 0:
                                                                    if brd[(nnnx,nnny)] != self.color:
                                                                        if nnnx+self.DIR[key][0]>0 and nnny+self.DIR[key][1]>0 and nnnx+self.DIR[key][0]<9 and nnny+self.DIR[key][1]<9:
                                                                            if brd[nnnx+self.DIR[key][0],nnny+self.DIR[key][1]] == 0: 
                                                                                moves.append((nnnx+self.DIR[key][0],nnny+ self.DIR[key][1]))
                                                                                jumps.append((nnnx,nnny))
        return moves, jumps    


    def validateMoves(self, brd):
        posMoves, jumps = self.possibleMoves(brd)
        validMoves = []
        js = []
        if posMoves != None:
            x,y = self.position()
            if not self._isKing:
                if self.color == 'B':
                    print "BLACK", posMoves
                    for i in range(len(posMoves)):
                        mx, my = posMoves[i]
                        if mx-x >0:
                            validMoves.append(posMoves[i])
                            if mx-x>1:
                                js.append(jumps[i])
                else:
                    print "WHITE", posMoves
                    for i in range(len(posMoves)):
                        print posMoves[i]
                        print (x,y)
                        mx, my = posMoves[i]
                        if mx-x <0:
                            print posMoves[i]
                            validMoves.append(posMoves[i])
                            if mx-x<-1:
                                js.append(jumps[i])
            else:
                print "KING", posMoves
                validMoves = posMoves
                js = jumps
        else:
            return []
        print "validMoves", validMoves

        return validMoves, js

