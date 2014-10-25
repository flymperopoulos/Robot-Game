from chess import *
from checkers import *
import sys
#import tictactoe

def printBoardttt(brd):
	"""displays board"""
	brdList = []
	for i in range(1,4):
		for j in range(1,4):
			if brd[(i,j)] == 0:
				brdList.append(' ')
			else:
				brdList.append(brd[(i,j)].name)

def printBoard(brd):
	"""displays board"""
	brdList = []
	for i in range(1,9):
		for j in range(1,9):
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
	print

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

def readPlayerInput(brd, player):
	move = []
	while True:
		usrInput = raw_input("Piece newX newY or Q-- ")
		if usrInput.upper() == 'Q':
			sys.exit(0)
		lis = usrInput.split()
		if len(lis) == 3:
			for i in brd:
				if brd[i] != 0:
					if brd[i].name == lis[0]:
						move.append(brd[i])
						move.append(int(lis[1]))
						move.append(int(lis[2]))
						print "I have your move"
						return move
					# else: 
						# print "Could not find " + lis[0] +' '+ lis[1]+' ' + lis[2]
		else:
			print "Invalid length. Try again."
		
	return

def computerMove():
	return

def makeMove(game, brd, move):
	"""Makes a legal move based on current game rules"""
	if move == None:
		return
	else: 
		piece = move[0]
		x = move[1]
		y = move[2]
		xp,yp = piece.position
		if piece.validateMoves(brd):
			brd[(xp,yp)] = 0
			brd[(x,y)] = piece	
			return brd
		else: 
			print 'invalid move'
			return brd	

def getState():
	"""detects how the board looks"""
	return True, True

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
	game = determineGame(strn)
	brd = createBoard(game)
	
	printBoard(brd)
	
	player = curPlayer
	while not done(game, brd, player):
		if player == 'W':
			move = playW(brd, player)
		else:
			move = playB(brd, player)
		brd = makeMove(game,brd,move)
		printBoard(brd)
		player = otherPlayer(player)
	if hasWin(game, brd, player):
		print "winner " + player
	else: 
		print "Stalemate"

def main():
	game, brd = getState()
	inpt = raw_input("Game, Current player(w or b), Human or Computer, Human or Computer-- ")
	usrInput = inpt.split()
	if len(usrInput) == 4:
		if usrInput[2].upper() == "HUMAN":
			playW = readPlayerInput
		else: 
			playW = computerMove
		if usrInput[2].upper() == "HUMAN":
			playB = readPlayerInput
		else: 
			playB = computerMove
		run(usrInput[0],usrInput[1].upper(), playW, playB)
	else:
		print "Try again."


	


	return True

if __name__ in "__main__":
	main()