from chess import *
from checkers import *
import sys
from picameracode import *
import random
# from minmax import *
#import tictactoe
import serial
import cv2
import time
#Global Variables 
# STEPS_PER_INCH = 3200
PIECE = 100
KING = 300
EDGE = 10

def send_tuple(tup,tup2):
    print "Sending Tuple"
    x = tup[0]
    y = tup[1]
    x2 = tup2[0]
    y2 = tup2[1]
    with serial.Serial('/dev/ttyACM0',9600) as ser:
        if ser.isOpen():
                ser.write('X'+str(x)+'Y'+str(y)+'X'+ str(x2)+'Y'+str(y2))
                print "Serial is Open"
    print "Done Sending"


def utility (board):
    """Evaluation function for the board"""
    score = 0
    for i in range(1,9):
        for j in range(1,9):
            if board[(i,j)] != 0:
                if board[(i,j)].color == 'white':
                    score += PIECE
                    if board[(i,j)].isKing:
                        score += KING
                        if i == 1 or i == 8:
                            score += EDGE 
                    if j == 1 or j == 8:
                        score += EDGE
                elif board[(i,j)].color == 'black':
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
    """finds all of the pieces on the board"""
    pieces = []
    for i in range(1,9):
        for j in range(1,9):
            if board[(i,j)] != 0 and board[(i,j)].color == player:
                pieces.append(board[(i,j)])
    return pieces



def min_value(game,board,player,tree,depth):
    """Minimizes the Max value"""
    d = {}
    scores = []
    brd_lst = printBoard(board)
    brd_str = ''
    depth += 1
    for i in brd_lst:
        brd_str += i
    if depth > 10:
        return utility(board)
    if done(game,board,player):
        return utility(board)
    for piece in grab_pieces(board,player):
        moves,jumps = piece.validateMoves(board)
        for move in moves:
            if brd_str in tree:
                v = tree[brd_str]
            else:  
                m = [piece,move[0],move[1]]
                new_board = makeMove(game,board,m)
                v = max_value(game,new_board,otherPlayer(player),tree, depth)
                tree[brd_str] = v
            scores.append(v)
    value = min(scores)
    return value

def max_value(game,board,player,tree,depth):
    """Maximizes the minimum vlaue"""
    d = {}
    scores = []
    brd_lst = printBoard(board)
    brd_str = ''
    depth += 1
    for i in brd_lst:
        brd_str += i
    if depth>10:
        return utility(board)
    if done(game,board,player):
        return utility(board)
    for piece in grab_pieces(board,player):
        moves,jumps = piece.validateMoves(board)
        for move in moves:
            if brd_str in tree:
                v = tree[brd_str]
            else:  
                m = [piece,move[0],move[1]]
                new_board = makeMove(game,board,m)
                v = min_value(game,new_board,otherPlayer(player),tree, depth)
                tree[brd_str] = v
            scores.append(v)
    value = max(scores)
    return value

def best_move(game,board,player):
    """Calls the minimax algorithm to determine best move"""
    new_game = Checkers()
    board_buf = board
    new_game.board = board_buf
    print board_buf
    tree = {}
    m = {}
    for piece in grab_pieces(board_buf,player):
        depth = 0
        moves,jumps = piece.validateMoves(board_buf)
        for move in moves:
            if player.upper() == 'W':
                value = min_value(new_game,board_buf,player,tree, depth)
            else:
                value = max_value(new_game,board_buf,player,tree, depth)
            m[value] = [piece,move[0],move[1]]
    if player.upper() == 'W':
        key = max(m)
        move = m[key]
    else:
        key = min(m)
        move = m[key] 
    print move
    return move

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
    """Check if player has win"""
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
    """keyboard input for human player"""
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
    brd_list = printBoard(brd)
    d_list = brd_list
    while d_list == brd_list:
        d = get_State(brd)
        print "checking board"
        if d != None:
            d_list = printBoard(d)
        time.sleep(2)
    return d, None

def computerMove(game, brd, player):
    move =  best_move(game,brd,player)
    piece = move[0]
    x1,y1 = piece.position()
    x2 = move[1]
    y2 = move[2]
    send_tuple((x1,y1),(x2,y2))
    return brd, move

def makeMove(game, brd, move):
    """Makes a legal move based on current game rules"""
    # new_brd = dict(brd)
    new_game = Checkers()
    # new_game.board = new_brd
    new_brd = new_game.make_buf(brd)
    if move == None:
        return new_brd
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
        ms, js = piece.validateMoves(new_brd)
        if (x,y) in ms: 
            new_brd = new_game.move(piece,x,y,js)  
            return new_brd
        else: 
            print 'invalid move'
            return new_brd  

def get_State(board):
    """detects how the board looks"""
    out = picam_main(board)
    if out == None:
        print "bull"
        return None
    dic1, dic2 = out
    d= createBoard(dic1, dic2)
    d2 = compareBoard(board,d)
    print d2
    return d2

def createBoard(camBrd, colorBrd):
    """Uses Cam data to create Board"""
    d = {}
    for keys in camBrd.keys():
        if keys in colorBrd:
            d[keys] = CheckerPiece("W", keys, "0")
        else:
            d[keys] = CheckerPiece("B", keys, "0")
    return d



def compareBoard(brd, finalCamBoard):
    d = {}
    for i in range(1,9):
        for j in range(1,9):
             d[(i,j)] = 0
    for pieces in brd.values():
        for camPieces in finalCamBoard.values():
            # adding the "W" (human) pieces. There are only going to be one piece that changed position
            # print pieces.color, pieces.position, pieces.name
            if pieces != 0:
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

# def determineGame(strn):
#     if strn.lower() == "chess":
#         game = Chess()
#     elif strn.lower() == "checkers":
#         game = Checkers()
#     else:
#         game = tictactoe()
#     return game


def createInitialBoard(game):
    """initializes board"""
    return game.initialBoard()
    

def run(strn,curPlayer,playW, playB):
    """Gameplay Loop"""
    game = Checkers()
    brd = createInitialBoard(game)
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
    # inpt = raw_input("test, Current player(w or b) ")
    # usrInput = inpt.split()
    # OLD VERSION
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
    inpt = sys.argv
    usrInput = inpt[1:]
    if usrInput != []:
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
