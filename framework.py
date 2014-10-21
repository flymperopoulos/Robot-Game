from chess import *
from checkers import *
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
				brdList.append(' ')
			else:
				brdList.append(brd[(i,j)].name)
	print brd[0:8] 
	print brd[9:16]
	print brd[17:24]
	print brd[25:32]
	print brd[33:40]
	print brd[41:48]
	print brd[49:56]
	print brd[57:64]

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

def readPlayerInput(brd):
	while True:
		usrInput = raw_input("Piece newX newY or Q")
		if usrInput.upper() == 'Q':
			sys.exit(0)
		lis = usrInput.split()
		if len(move) == 5:
			for i in brd:
				if brd[i] != 0:
					if (lis[1],lis[2]) in brd[i].possibleMoves() and brd[i].name == lis[0]:
						move[0] = board[i]
						move[1] = int(move[1])
						move[2] = int(move[2])
						return move
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
		if validateMove():
			brd[i] == 0
			brd[(x,y)] == piece			

def getState():
	"""detects how the board looks"""
	return True, True

def createBoard(game):
	"""initializes board"""
	if game.lower() == "chess":
		game = Chess
		return game, Chess.initalboard()
	elif game.lower() == "checkers":
		game = checkers
		checkers.initalboard()
		return game, checkers.board
	else:
		game = tictactoe
		return game, tictactoe.initalboard()

def run(game,curPlayer,playW, playB):
	game, brd = createBoard(game)

	printBoard(brd)
	
	player = curPlayer
	while not done(game, brd, player):
		if player == 'W':
			move = playW(brd, player)
		else:
			move = playB(brd, player)
		brd = makeMove(game,brd,move)
		printBoard(brd)
		player = otherPlayer()
	if hasWin(brd):
		print "winner " + player
	else: 
		print "Stalemate"

def main():
	game, brd = getState()
	inpt = raw_input("Game, Current player(w or b), Human or Computer, Human or Computer.")
	usrInput = inpt.split()
	if usrInput[2].upper() == "HUMAN":
		playW = readPlayerInput
	else: 
		playW = computerMove
	if usrInput[2].upper() == "HUMAN":
		playB = readPlayerInput
	else: 
		playB = computerMove

	run(usrInput[0],usrInput[1].upper(), playW, playB)


	return True

if __name__ in "__main__":
	main()