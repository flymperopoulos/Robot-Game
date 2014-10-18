class Pawn:
	def __init__(self, position, color, name, state, change):
		self.position = position
		self.color = color
		self.name = 'p'
		self.state = state
		self.change = change

	def possibleMoves(self):
		x,y = self.position
		moves = [(x,y+1),(x,y+2),(x+1,y+1),(x-1,y+1)]
		return moves

	def alternatePiece(self):
		pass

	def validateMoves(self):
		moves = possibleMoves()
		x,y = self.position
		validMoves = []

		# Checks edge case for column 1 moves
		# Moves diagonally right
		if x == 1 and self.board[(2,y+1)].color != self.color:
			validMoves.append(moves[2])

		# Moves straight up option
		if self.board[1,y+1].color == color:
			validMoves.append(moves[0])

		# Checks edge case for column 8 moves
		# Moves diagonally left
		if x == 8 and self.board[(7,y+1)].color != self.color:
			validMoves.append(moves[3])

		# Checks non-edge cases
		# Move diagonally to the right
		if x != 1 and x != 8 and self.board[(x+1,y+1)].color != self.color:
			validMoves.append(moves[2])
		# Move diagonally to the left
		if x != 1 and x != 8 and self.board[(x-1,y+1)].color != self.color:
			validMoves.append(moves[3])

		# Checks initial state, where pawn can move two steps forward
		if self.state == 0:
			validateMoves.append(moves[1])

class Bishop():
	def __init__(self, position, color, name, state, negativeDirection):
		self.position = position
		self.color = color
		self.name = 'b'
		self.negativeDirection = negativeDirection

	def possibleMoves(self):
		x,y = self.position
		bishMoves = []  

		for i in range(-7,8):
			if 0<x+i<8:
				bishMoves.append((x+i,y+i))
		return bishMoves

	def validateMoves(self):
		validMoves = possibleMoves()

		x,y = self.position

		# Loops through validMoves 
		for m in validMoves:
			# Checks the value of all the dictonary keys and if it is 0, then nothing is there, so it can move
			if self.board.get(m) == 0:
				validMoves.append(m)
			# However, it can also move, if something is there, if it is an enemy
			if self.board.get(m) == 1 and self.board.get(m).color != color:
				validMoves.append(m)


class Chess(object):

	"""Class for the Chess Object"""

	def __init__(self, setupType = 0):
		self.board = {}

	def initiateBoard(self):
		for i in range(1,9):
			for j in range(1,9):
				self.board[(i,j)] = 0

	def isChess(self):
		return True