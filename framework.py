from chess import *
from checkers import *
import sys
from picameracode import *
# from minmax import *
#import tictactoe

# def printBoardttt(brd):
# 	"""displays board"""
# 	brdList = []
# 	for i in range(1,4):
# 		for j in range(1,4):
# 			if brd[(i,j)] == 0:
# 				brdList.append(' ')
# 			else:
# 				brdList.append(brd[(i,j)].name)

def printBoard(brd):
	"""displays board"""
	brdList = []
	for j in range(1,9):
		for i in range(1,9):
			if brd[(i,j)] == 0:
				brdList.append(' . ')
			else:
				if len(brd[(i,j)].name) == 3:
					brdList.append(brd[(i,j)].name)s
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

def readPlayerInput_test(brd, player):
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
							return move
			else:
				print "Piece does not match player color"
					# else: 
						# print "Could not find " + lis[0] +' '+ lis[1]+' ' + lis[2]
		else:
			print "Invalid length. Try again."
		
	return
def humanMove(brd,player):
	#needs a little work
	d = brd
	while d == brd:
		d = getState(brd)
	return d, None
def computerMove():
	return

def makeMove(game, brd, move):
	"""Makes a legal move based on current game rules"""
	if move == None:
		return brd
	else: 
		piece = move[0]
		x = move[1]
		y = move[2]
		xp,yp = piece._position
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
			brd,move = playW(brd, player)
		else:
			brd,move = playB(brd, player)
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
	brd = getState()
	inpt = raw_input("test, Current player(w or b), Human or Computer, Human or Computer-- ")
	usrInput = inpt.split()
	# if len(usrInput) == 4:
	if usrInput[2].upper() == "COMPUTER":
		playW = computerMove
	else:
		if usrInput[0].upper() = 'TEST': 
			playW = readPlayerInput_test
		elif len(usrInput) == 3:
			playW = humanMove
	if usrInput[2].upper() == "HUMAN":
		if usrInput[0].upper() = 'TEST': 
			playB = readPlayerInput_test
		elif len(usrInput) == 3:
			playB = humanMove
	else: 
		playB = computerMove
	run(usrInput[0],usrInput[1].upper(), playW, playB)

		
	return True

if __name__ in "__main__":
	main()