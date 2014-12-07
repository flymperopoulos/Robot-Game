class Pawn:

	"""Class for the Pawn Object piece"""

	def __init__(self, position, color, name, state= 'pawn'):
		self.position = position
		self.color = color
		self.name = color +'p'+ str(name)
		self.state = state

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

	"""Class for the Bishop Object piece"""

	def __init__(self, position, color, name):
		self.position = position
		self.color = color
		self.name = color +'B' +str(name)

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

class Rook:

	"""Class for the Rook Object piece"""

	def __init__(self, position, color, name):
		self.position = position
		self.color = color
		self.name = color + 'R'+str(name)

	def possibleMoves(self):
		x,y = self.position

		rookMoves = []

		for i in range(-7,8):
			if 0<x+i<8:
				rookMoves.append((x+i,y))
				rookMoves.append((x,y+i))
		return rookMoves	

	def validateMoves(self):
		rookValidMoves = possibleMoves()

		x,y = self.position

		for r in rookValidMoves:

			if self.board.get(r) == 0:
				rookValidMoves.append(r)
			if self.board.get(r) == 1 and self.board.get(r).color != color:
				validMoves.append(r)

class Knight:

	"""Class for the Knight Object piece"""

	def __init__(self, position, color, name):
		self.position = position
		self.color = color
		self.name = color +'N' +str(name)

	def possibleMoves(self):
		x,y = self.position
		while (x-1)>0:
			moves = [(x+1,y+3),(x-1,y+3),(x-1,y-3),(x+1,y-3)]
		return moves

	def validateMoves(self):
		knightValidMoves = possibleMoves()

		for k in knightValidMoves:

			if self.board.get(k) == 0:
				rookValidMoves.append(k)
			if self.board.get(k) == 1 and self.board.get(k).color != color:
				validMoves.append(k)

class King:

	"""Class for the King Object piece"""

	def __init__(self, position, color, name):
		self.position = position
		self.color = color
		self.name = color + 'K'+str(name)

	def possibleMoves(self):
		x,y = self.position
		moves = [(x,y+1),(x+1,y),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]
		return moves

	def validateMoves(self):
		kingValidMoves = possibleMoves()

		for k in kingValidMoves:
			if self.board.get(k) == 0:
				kingValidMoves.append(k)
			if self.board.get(k) and self.board.get(k).color != color:
				kingValidMoves.append(k)

class Queen:

	"""Class for the Queen Object piece"""

	def __init__(self, position, color, name):
		self.position = position
		self.color = color
		self.name = color + 'Q' + str(name)

	def possibleMoves(self):
		queenMoves = []

		for i in range(-7,8):
			if 0<x+i<8:
				queenMoves.append((x+i,y+i))
				queenMoves.append((x+i,y))
				queenMoves.append((x,y+i))
		return queenMoves

	def validateMoves(self):
		queenValidMoves = possibleMoves()

		x,y = self.position

		# Loops through validMoves 
		for m in queenValidMoves:
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

	def initialBoard(self):
		for i in range(1,9):
			for j in range(1,9):
				self.board[(i,j)] = 0

		for j in range(1,9):
			self.board[(2,j)] = Pawn((2,j),'W',j)
			self.board[(7,j)] = Pawn((7,j),'B',j)

		self.board[(1,1)] = Rook((1,1),'W',1)
		self.board[(1,8)] = Rook((1,8),'W',8)
		self.board[(8,1)] = Rook((8,1),'B',1)
		self.board[(8,8)] = Rook((8,8),'B',8)

		self.board[(1,2)] = Knight((1,2),'W',2)
		self.board[(1,7)] = Knight((1,7),'W',7)
		self.board[(8,2)] = Knight((8,2),'B',2)
		self.board[(8,7)] = Knight((8,7),'B',7)

		self.board[(1,3)] = Bishop((1,3),'W',3)
		self.board[(1,6)] = Bishop((1,6),'W',6)
		self.board[(8,3)] = Bishop((8,3),'B',3)
		self.board[(8,6)] = Bishop((8,6),'B',6)

		self.board[(1,5)] = King((1,5),'W',1)
		self.board[(1,4)] = Queen((1,4),'W',1)
		self.board[(8,5)] = King((8,5),'B',1)
		self.board[(8,4)] = Queen((8,4),'B',1)
		return self.board

	def isChess(self):
		return True