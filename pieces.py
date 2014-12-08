from checkers import *

class CheckerPiece(object):
	"""
		checkerPiece that determines has an attribut if it is white or B and returns all possible moves
	"""

	def __init__(self, color, position, number):
		self.color = color
		self.name = color + number
		self._position = position
		self.isKing = False
		self._possibleMoves = []

	def position(self):
		return self._position

	def isKing(self):
		if self.color == "B":
			if self.position[0] == 8:
				return True
		else:
			if self.position[0] == 1:
				return True
		return False

	def possibleMoves(self, brd):
		moves = []
		x,y = self.position()
		if self.color == 'B':
			moves.append((x+1,y-1))
			moves.append((x+1,y+1))
			moves.append((x+2,y-2))
			moves.append((x+2,y+2))
			if self.isKing:
				moves.append((x-1,y-1))
				moves.append((x-1,y+1))
				moves.append((x-2,y+2))
				moves.append((x-2,y-2))
		else:
			moves.append((x-1,y-1))
			moves.append((x-1,y+1))
			moves.append((x-2,y-2))
			moves.append((x-2,y+2))
			if self.isKing:
				moves.append((x+1,y-1))
				moves.append((x+1,y+1))
				moves.append((x+2,y+2))
				moves.append((x+2,y-2))

		return moves

	def validateMoves(self, brd):
		posMoves = self.possibleMoves(brd)
		print posMoves
		validMoves = []

		x,y = self.position()

		for move in posMoves:
			mx, my = move
			if mx>0 and my>0 and mx<9 and my<9:
				print "fuck"
				if mx - x == 2:
					print "you"
					jx = mx-1
					if my - y == 2:
						jy = my-1
					elif my-y == -2:
						jy = my+1
					print (jx,jy)
					if brd[(jx,jy)] == 0:
						pass
					elif brd[(jx,jy)].color == self.color:
						pass
					else:
						validMoves.append(move)
				elif mx - x == -2:
					print "you"
					jx = mx+1
					if my - y == 2:
						jy = my-1
					elif my-y == -2:
						jy = my+1
					print (jx,jy)
					if brd[(jx,jy)] == 0:
						pass
					elif brd[(jx,jy)].color == self.color:
						pass
					else:
						validMoves.append(move)
				elif brd[move] == 0:
					validMoves.append(move)
		print validMoves
		return validMoves

