class Pawn:
	def __init__(self, position, color, name, state, change):
		self.position = position
		self.color = color
		self.name = 'p'
		self.state = state
		self.change = change

	def possibleMoves(self, moves):
		x,y = self.position
		self.moves = [self.position(x,y+1),self.position(x,y+2),self.position(x+1,y+1),self.position(x-1,y+1)]

	def alternatePiece(self):
		pass

	def validateMoves(self):

		x,y = self.position
		# Checks edge case for column 1 moves
		# Moves diagonally right
		if x == 1 and board[(2,y+1)].color != self.color:
			self.moves[2]
		# Moves straight up
		else:
			self.moves[0]

		# Checks edge case for column 8 moves
		# Moves diagonally left
		if x == 8 and board[(7,y+1)].color != self.color:
			self.moves[3]
		# Move straight up
		else:
			self.moves[0]

		# Checks non-edge cases
		# Move diagonally to the right
		if x != 1 and x != 8 and board[(x+1,y+1)].color != self.color:
			self.moves[2]
		# Move diagonally to the left
		else if x != 1 and x != 8 and board[(x-1,y+1)].color != self.color:
			self.moves[3]
		# Move straight up
		else:
			self.moves[0]

		if self.state == 0:
			self.moves[1]



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