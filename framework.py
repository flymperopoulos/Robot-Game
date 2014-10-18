import chess
import checkers
import tictactoe

def done(brd):
	#Return True if game is won or if game is unwinnable. Print some statement based on the condition.
	return True

def otherPlayer(player):
	#switch between players 
	return True

def validateMove(brd, move):
	#detects if a move is legal
	return True

def move(brd):
	#Makes a legal move based on current game rules
	return True

def getState():
	#detects how the board looks
	return True

def createBoard(game):
	# initializes board
	if game = "chess":
		return chess.initalboard()
	elif game = "checkers":
		return checkers.initalboard()
	else:
		return tictactoe.initalboard()
	return True

def run():
	return True

def main():
	game, brd = getState()
	# create the initial board
	createBoard(game, brd)

	while not done(brd):

	return True

if __name__ in "__main__":
	main()