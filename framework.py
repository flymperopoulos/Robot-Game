import chess
import checkers
import tictactoe

def printBoardttt(brd):
	"""displays board"""
	brdList = []
	for i in range(1,4):
		for j in range(1,4):
			if board[(i,j)] == 0:
				brdList.append(' ')
			else:
				brdList.append(board[(i,j)].name)

def printBoard(brd):
	"""displays board"""
	brdList = []
	for i in range(1,9):
		for j in range(1,9):
			if board[(i,j)] == 0:
				brdList.append(' ')
			else:
				brdList.append(board[(i,j)].name)

def done(game, brd):
	"""Return True if game is won or if game is unwinnable. Print some statement based on the condition."""
	if hasWin(game, brd):
		return True
	elif game.end():
		return True
	else:
		return False

def hasWin(game,brd):
	if game.hasWin():
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
	if move in game.validateMoves():
		return True
	else: 
		print "Not a valid move"
		return False

def readPlayerInput(brd):
	while True:
		usrInput = raw_input("Piece newX newY or Q")
		if usrInput.uppercase == 'Q':
			sys.exit(0)
		lis = usrInput.split()
		if len(move) == 5:
			for i in board
				if board[i] != 0:
					if (lis[1],lis[2]) in board[i].possibleMoves and board[i].name == lis[0]:
						move[0] = board[i]
						move[1] = int(move[1])
						move[2] = int(move[2])
						return move
				else: 
					print "not a piece "
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
	if game.lowercase() == "chess":
		return chess.initalboard()
	elif game.lowercase() == "checkers":
		return checkers.initalboard()
	else:
		return tictactoe.initalboard()
	return True

def run(game,curPlayer,playW, playB):
	brd = createBoard(game)

	printBoard(brd)
	
	player = curPlayer
	while not done(brd):
		if player = 'W':
			move = playW(brd)
		else:
			move = playB(brd)
		makeMove(game,brd,move)
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
	if usrInput[2].uppercase() == "HUMAN":
		playW = readPlayerInput()
	else: 
		playW = computerMove()
	if usrInput[2].uppercase() == "HUMAN":
		playB = readPlayerInput()
	else: 
		playB = computerMove()

	run(usrInput[0],usrInput[1].uppercase(), playW, playB)


	return True

if __name__ in "__main__":
	main()