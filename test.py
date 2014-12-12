from chess import *
from checkers import *
import sys
# from picameracode import *
import random
# from minmax import *
#import tictactoe

# def printBoardttt(brd):
#   """displays board"""
#   brdList = []
#   for i in range(1,4):
#       for j in range(1,4):
#           if brd[(i,j)] == 0:
#               brdList.append(' ')
#           else:
#               brdList.append(brd[(i,j)].name)
def utility (board):
    score = 0
    for i in range(1,9):
        for j in range(1,9):
            if board[(i,j)].color == white:
                score += PIECE
                if board[(i,j)].isKing:
                    score += KING
                if i == 1 or i == 8:
                    score += EDGE 
                if j == 1 or j == 8:
                    score -= EDGE
            elif board[(i,j)].color == black:
                score -= PIECE
                if board[(i,j)].isKing:
                    score -= KING
                if i == 1 or i == 8: 
                    score-= EDGE
                if j == 1 or j == 8:
                    score -= EDGE
    score += random.randint(0,10)
    return score


def grab_pieces(board,player):
    pieces = []
    for i in range(1,9):
        for j in range(1,9):
            if board[(i,j)] != 0 and board[(i,j)].color == player:
                pieces.append(board[(i,j)])
    return pieces



def min_value (game, board,value,move,player):
    # fix me 
    d_moves = {}
    if done(game,board,player) != False:
        value[-1] = utility(board)
        # value.append(0)
        return value
    pieces = grab_pieces(board,player)
    for piece in pieces:
        moves = piece.validateMoves(board)
        d_moves[piece] = moves
    for key in d_moves:
        for i in d_moves[key]:
            move = [key, i[0], i[1]]
            new_board = makeMove(game, board, move)#fix this
            # print_board(board)
            player = otherPlayer(player)
            value[-1] = min(value[-1],max_value(game, new_board,value,move,player))
            print 'Final'
            print value,move
            
    return value, move

def max_value (game, board,value,move,player):
    d_moves = {}
    if done(game,board,player) != False:
        value[-1] = utility(board)
        # value.append(0)
        return value
    pieces = grab_pieces(board,player)
    for piece in pieces:
        moves = piece.validateMoves(board)
        d_moves[piece] = moves
    for key in d_moves:
        for i in d_moves[key]:
            move = [key, i[0], i[1]]
            new_board = makeMove(game, board, move)# fix this
            # print_board(board)
            player = otherPlayer(player)
            value[-1] = max(value[-1],min_value(game, new_board,value,move,player))
            print 'Final'
            print value
    return value, move


def best_move (game, board,player):
    # fix me
    move = [0]
    value = [0]
    v,move = min_value(game, board,value,move,player)
    print move
    return board, move

def printBoard(brd):
    """displays board"""
    brdList = []
    for j in range(1,9):
        for i in range(1,9):
            if brd[(i,j)] == 0:
                brdList.append(' . ')
            else:
                if len(brd[(i,j)].name) == 3:
                    brdList.append(brd[(i,j)].name)
                else:
                    brdList.append(brd[(i,j)].name + ' ')
    # print brdList[0:8] 
    # print brdList[8:16]
    # print brdList[16:24]
    # print brdList[24:32]
    # print brdList[32:40]
    # print brdList[40:48]
    # print brdList[48:56]
    # print brdList[56:64]
    for i in range(0,8):
        print '  ',brdList[i*8],brdList[i*8+1],brdList[i*8+2],brdList[i*8+3],brdList[i*8+4],brdList[i*8+5],brdList[i*8+6],brdList[i*8+7]
    return brdList

def done(game, brd, player):
    """Return True if game is won or if game is unwinnable. Print some statement based on the condition."""
    if hasWin(game, brd, player):
        return True
    elif game.end():
        return True
    else:
        return False

def hasWin(game,brd,player):
    if game.hasWin(brd, player):
        return True
    else:
        return False

def otherPlayer(player):
    """switch between players"""
    if player == 'W':
        player = 'B'
    else:
        player = 'W'
    return player

def validateMove(game, brd, move):
    """detects if a move is legal"""
    return True

def readPlayerInput_test(game, brd, player):
    move = []
    while True:
        print "You are " + player
        usrInput = raw_input("Piece newX newY or Q-- ")
        if usrInput.upper() == 'Q':
            sys.exit(0)
        lis = usrInput.split()
        if len(lis) == 3:
            if lis[0][0] == player:
                for i in brd:
                    if brd[i] != 0:
                        if brd[i].name == lis[0]:
                            move.append(brd[i])
                            move.append(int(lis[1]))
                            move.append(int(lis[2]))
                            print "I have your move"
                            return brd,move
            else:
                print "Piece does not match player color"
                    # else: 
                        # print "Could not find " + lis[0] +' '+ lis[1]+' ' + lis[2]
        else:
            print "Invalid length. Try again."
        
    return
def humanMove(game, brd, player):
    #needs a little work
    d = brd
    while d == brd:
        d = getState(brd)
    return d, None
def computerMove(game, brd, player):
    moves = []
    pieces = grab_pieces(brd,player)
    for piece in pieces:
        m = piece.validateMoves()
        for move in m:
            moves.append(move)
    move = random.choice(moves)
    return board, move

def makeMove(game, brd, move):
    """Makes a legal move based on current game rules"""
    if move == None:
        return brd
    else: 
        piece = move[0]
        x = move[1]
        y = move[2]
        # xp,yp = piece._position
        # validate move needs to be fixed. I can move pieces two spaces away when there is not a piece next to it in checkers.  
        #Double jumps need to be fixed
        print brd[(x,y)]
        print x
        print y
        if (x,y) in piece.validateMoves(brd): 
            brd = game.move(piece,x,y)  

            return brd
        else: 
            print 'invalid move'
            return brd  

def getState(board):
    """detects how the board looks"""
    dic1, dic2 = picam_main()
    d= createBoard(dic1, dic2)
    d2 = compareBoard(board,d)
    return d2

def createBoard(camBrd, colorBrd):
    d = {}
    for keys in cam.keys():
        if keys in colorBrd:
            d[keys] = CheckerPiece("W", keys, "0")
        else:
            d[keys] = CheckerPiece("B", keys, "0")
    return d



def compareBoard(brd, finalCamBoard):
    d = {}
    for pieces in brd.values():
        for camPieces in finalCamBoard.values():
            # adding the "W" (human) pieces. There are only going to be one piece that changed position
            # print pieces.color, pieces.position, pieces.name
            if pieces.color == "W" and camPieces.color == "W" and pieces.position == camPieces.position:
                # print "first if", pieces.color, pieces.position, pieces.name
                d[pieces.position] = CheckerPiece("W", pieces.position, pieces.name[1])
            elif pieces.color == "W" and camPieces.color == "W":
                # print "else", pieces.color, pieces.position, pieces.name
                d[camPieces.position] = CheckerPiece("W", camPieces.position, pieces.name[1])
            # adding the "B" (computer) pieces. In checkers only thing that can happen is pieces being taken away
            if pieces.color == "B" and camPieces.color == "B" and pieces.position == camPieces.position:
                d[pieces.position] = CheckerPiece("B", pieces.position, pieces.name[1])

    return d

def determineGame(strn):
    if strn.lower() == "chess":
        game = Chess()
    elif strn.lower() == "checkers":
        game = Checkers()
    else:
        game = tictactoe()
    return game


def createBoard(game):
    """initializes board"""
    return game.initialBoard()
    

def run(strn,curPlayer,playW, playB):
    game = determineGame('checkers')
    brd = createBoard(game)
    boardView = printBoard(brd)
    previousBrdView = boardView
    
    player = curPlayer
    while not done(game, brd, player):
        if player == 'W':
            brd,move = playW(game, brd, player)
        else:
            brd,move = playB(game, brd, player)
        brd = makeMove(game,brd,move)
        boardView = printBoard(brd)
        if boardView!=previousBrdView:
            previousBrdView = boardView
            player = otherPlayer(player)
            print "Change player"
    if hasWin(game, brd, player):
        print "winner " + player
    else: 
        print "Stalemate"

def main():
    inpt = raw_input("test, Current player(w or b) ")
    usrInput = inpt.split()
    # if len(usrInput) == 4:
    #   if usrInput[2].upper() == "COMPUTER":
    #       playW = computerMove
    #   else:
    #       if usrInput[0].upper() == 'TEST': 
    #           playW = readPlayerInput_test
    #       elif len(usrInput) == 3:
    #           playW = humanMove
    #   if usrInput[2].upper() == "HUMAN":
    #       if usrInput[0].upper() == 'TEST': 
    #           playB = readPlayerInput_test
    #       elif len(usrInput) == 3:
    #           playB = humanMove
    #   else: 
    #       playB = computerMove
    #   run(usrInput[0],usrInput[1].upper(), playW, playB)
    # else:
    #   playW = humanMove
    #   playB = computerMove
    if inpt != '':
        if usrInput[0].upper() == 'TEST':
            if len(usrInput) == 2:
                if usrInput[1].upper() == 'B':
                    playB = readPlayerInput_test
                    playW = computerMove
                elif usrInput[1].upper() == 'TEST':
                    playB = readPlayerInput_test
                    playW = readPlayerInput_test
            else:
                playW = readPlayerInput_test
                playB = computerMove    
        elif usrInput[0].upper() == 'B':
            playB = humanMove
            playW = computerMove
    else:
        playW = humanMove
        playB = computerMove
    run('','w'.upper(), playW, playB)

        
    return True

if __name__ in "__main__":
    main()