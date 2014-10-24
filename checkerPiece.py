
class CheckerPiece(object):
	"""
		checkerPiece that determines has an attribut if it is white or black and returns all possible moves
	"""

	def __init__(self, color, position):
		self.color = color
		self.name = color
		self.position = position
		self.isKing = False

	def possibleMoves(self, position):
		moves = []
		kingMoves = []
		if self.color == "black":
			if position[1] == 1:
				moves.append((position[0]+1, 2))
				kingMoves.append((position[0]+1, 2))
			elif position[1] == 8:
				moves.append((position[0]+1, 7))
				kingMoves.append((position[0]+1, 7))
			elif position[0] == 8 and self.isKing == False: 
				return moves
			else:
				moves.append((position[0]+1, position[1]+1))
				moves.append((position[0]+1, position[1]-1))
				kingMoves.append((position[0]+1, position[1]+1))
				kingMoves.append((position[0]+1, position[1]-1))
		else:
			if position[1] == 1:
				moves.append((position[0]-1, 2))
				kingMoves.append((position[0]-1, 2))
			elif position[1] == 8:
				moves.append((position[0]-1, 7))
				kingMoves.append((position[0]-1, 7))
			elif position[0] == 1 and self.isKing == False:
				return moves
			else:
				moves.append((position[0]-1, position[1]+1))
				moves.append((position[0]-1, position[1]-1))
				kingMoves.append((position[0]-1, position[1]+1))
				kingMoves.append((position[0]-1, position[1]-1))
		if self.isKing:
			return kingMoves
		else:
			return moves

	def validateMoves(self, brd):
		"""
			takes in a dictionary of a board and a list of moves and checks if there is a another piece there)
		"""
		realmove = []
		kingRealMove = []
		moves = possibleMoves(self.position)

		if self.isKing:
			for m in moves:
				if brd.get(m) == 0:
					realmove.append(m)
				if brd.get(m).color != self.color and self.color == "black":

					if brd.get((m[0]+2,m[1]+2)) == 0:   #1
						kingRealMove.append((m[0]+2,m[1]+2))
						newMoves = possibleMoves((m[0]+2,m[1]+2))
						for nm in newMoves:
							if brd.get(nm).color != self.color:
					
								if brd.get((nm[0]+2,nm[1]+2)) == 0:   #2
									kingRealMove.append((nm[0]+2,nm[1]+2))
									newMoves1 = possibleMoves((nm[0]+2,nm[1]+2))
									for nm1 in newMoves1:
										if brd.get(nm1).color != self.color:
											if brd.get((nm1[0]+2,nm1[1]+2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]+2))

											if brd.get((nm1[0]+2,nm1[1]-2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]-2))

								if brd.get((nm[0]+2,nm[1]-2)) == 0:		#2
									kingRealMove.append((nm[0]+2,nm[1]-2))
									newMoves1 = possibleMoves((nm[0]+2,nm[1]-2))
									for nm1 in newMoves1:
										if brd.get(nm1).color != self.color:
											if brd.get((nm1[0]+2,nm1[1]+2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]+2))

											if brd.get((nm1[0]+2,nm1[1]-2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]-2))
					
					if brd.get((m[0]+2,m[1]-2)) == 0:     #1
						kingRealMove.append((m[0]+2,m[1]-2))
						newMoves = possibleMoves((m[0]+2,m[1]-2))
						for nm in newMoves:
							if brd.get(nm).color != self.color:
					
								if brd.get((nm[0]+2,nm[1]+2)) == 0:     #2
									kingRealMove.append((nm[0]+2,nm[1]+2))
									newMoves1 = possibleMoves((nm[0]+2,nm[1]+2))
									for nm1 in newMoves1:
										if brd.get(nm1).color != self.color:
											if brd.get((nm1[0]+2,nm1[1]+2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]+2))

											if brd.get((nm1[0]+2,nm1[1]-2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]-2))
					
								if brd.get((nm[0]+2,nm[1]-2)) == 0:    #2
									kingRealMove.append((nm[0]+2,nm[1]-2))
									newMoves1 = possibleMoves((nm[0]+2,nm[1]-2))
									for nm1 in newMoves1:
										if brd.get(nm1).color != self.color:
											if brd.get((nm1[0]+2,nm1[1]+2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]+2))

											if brd.get((nm1[0]+2,nm1[1]-2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]-2))

					if brd.get((m[0]-2,m[1]+2)) == 0:   #1
						kingRealMove.append((m[0]-2,m[1]+2))
						newMoves = possibleMoves((m[0]-2,m[1]+2))
						for nm in newMoves:
							if brd.get(nm).color != self.color:
					
								if brd.get((nm[0]-2,nm[1]+2)) == 0:   #2
									kingRealMove.append((nm[0]-2,nm[1]+2))
									newMoves1 = possibleMoves((nm[0]-2,nm[1]+2))
									for nm1 in newMoves1:
										if brd.get(nm1).color != self.color:
											if brd.get((nm1[0]-2,nm1[1]+2)) == 0:   #3
												kingRealMove.append((nm1[0]-2,nm1[1]+2))

											if brd.get((nm1[0]-2,nm1[1]-2)) == 0:   #3
												kingRealMove.append((nm1[0]-2,nm1[1]-2))

								if brd.get((nm[0]-2,nm[1]-2)) == 0:		#2
									kingRealMove.append((nm[0]-2,nm[1]-2))
									newMoves1 = possibleMoves((nm[0]-2,nm[1]-2))
									for nm1 in newMoves1:
										if brd.get(nm1).color != self.color:
											if brd.get((nm1[0]-2,nm1[1]+2)) == 0:   #3
												kingRealMove.append((nm1[0]-2,nm1[1]+2))

											if brd.get((nm1[0]-2,nm1[1]-2)) == 0:   #3
												kingRealMove.append((nm1[0]-2,nm1[1]-2))
					
					if brd.get((m[0]-2,m[1]-2)) == 0:     #1
						kingRealMove.append((m[0]-2,m[1]-2))
						newMoves = possibleMoves((m[0]-2,m[1]-2))
						for nm in newMoves:
							if brd.get(nm).color != self.color:
					
								if brd.get((nm[0]-2,nm[1]+2)) == 0:     #2
									kingRealMove.append((nm[0]-2,nm[1]+2))
									newMoves1 = possibleMoves((nm[0]-2,nm[1]+2))
									for nm1 in newMoves1:
										if brd.get(nm1).color != self.color:
											if brd.get((nm1[0]-2,nm1[1]+2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]+2))

											if brd.get((nm1[0]-2,nm1[1]-2)) == 0:   #3
												kingRealMove.append((nm1[0]-2,nm1[1]-2))
					
								if brd.get((nm[0]-2,nm[1]-2)) == 0:    #2
									kingRealMove.append((nm[0]-2,nm[1]-2))
									newMoves1 = possibleMoves((nm[0]-2,nm[1]-2))
									for nm1 in newMoves1:
										if brd.get(nm1).color != self.color:
											if brd.get((nm1[0]-2,nm1[1]+2)) == 0:   #3
												kingRealMove.append((nm1[0]+2,nm1[1]+2))

											if brd.get((nm1[0]-2,nm1[1]-2)) == 0:   #3
												kingRealMove.append((nm1[0]-2,nm1[1]-2))
			return kingRealMove




		for m in moves:
			if brd.get(m) == 0:
				realmove.append(m)
			if brd.get(m).color != self.color and self.color == "black":

				if brd.get((m[0]+2,m[1]+2)) == 0:   #1
					realmove.append((m[0]+2,m[1]+2))
					newMoves = possibleMoves((m[0]+2,m[1]+2))
					for nm in newMoves:
						if brd.get(nm).color != self.color:
				
							if brd.get((nm[0]+2,nm[1]+2)) == 0:   #2
								realmove.append((nm[0]+2,nm[1]+2))
								newMoves1 = possibleMoves((nm[0]+2,nm[1]+2))
								for nm1 in newMoves1:
									if brd.get(nm1).color != self.color:
										if brd.get((nm1[0]+2,nm1[1]+2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]+2))

										if brd.get((nm1[0]+2,nm1[1]-2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]-2))

							if brd.get((nm[0]+2,nm[1]-2)) == 0:		#2
								realmove.append((nm[0]+2,nm[1]-2))
								newMoves1 = possibleMoves((nm[0]+2,nm[1]-2))
								for nm1 in newMoves1:
									if brd.get(nm1).color != self.color:
										if brd.get((nm1[0]+2,nm1[1]+2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]+2))

										if brd.get((nm1[0]+2,nm1[1]-2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]-2))
				
				if brd.get((m[0]+2,m[1]-2)) == 0:     #1
					realmove.append((m[0]+2,m[1]-2))
					newMoves = possibleMoves((m[0]+2,m[1]-2))
					for nm in newMoves:
						if brd.get(nm).color != self.color:
				
							if brd.get((nm[0]+2,nm[1]+2)) == 0:     #2
								realmove.append((nm[0]+2,nm[1]+2))
								newMoves1 = possibleMoves((nm[0]+2,nm[1]+2))
								for nm1 in newMoves1:
									if brd.get(nm1).color != self.color:
										if brd.get((nm1[0]+2,nm1[1]+2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]+2))

										if brd.get((nm1[0]+2,nm1[1]-2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]-2))
				
							if brd.get((nm[0]+2,nm[1]-2)) == 0:    #2
								realmove.append((nm[0]+2,nm[1]-2))
								newMoves1 = possibleMoves((nm[0]+2,nm[1]-2))
								for nm1 in newMoves1:
									if brd.get(nm1).color != self.color:
										if brd.get((nm1[0]+2,nm1[1]+2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]+2))

										if brd.get((nm1[0]+2,nm1[1]-2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]-2))
			else:
				if brd.get((m[0]-2,m[1]+2)) == 0:   #1
					realmove.append((m[0]-2,m[1]+2))
					newMoves = possibleMoves((m[0]-2,m[1]+2))
					for nm in newMoves:
						if brd.get(nm).color != self.color:
				
							if brd.get((nm[0]-2,nm[1]+2)) == 0:   #2
								realmove.append((nm[0]-2,nm[1]+2))
								newMoves1 = possibleMoves((nm[0]-2,nm[1]+2))
								for nm1 in newMoves1:
									if brd.get(nm1).color != self.color:
										if brd.get((nm1[0]-2,nm1[1]+2)) == 0:   #3
											realmove.append((nm1[0]-2,nm1[1]+2))

										if brd.get((nm1[0]-2,nm1[1]-2)) == 0:   #3
											realmove.append((nm1[0]-2,nm1[1]-2))

							if brd.get((nm[0]-2,nm[1]-2)) == 0:		#2
								realmove.append((nm[0]-2,nm[1]-2))
								newMoves1 = possibleMoves((nm[0]-2,nm[1]-2))
								for nm1 in newMoves1:
									if brd.get(nm1).color != self.color:
										if brd.get((nm1[0]-2,nm1[1]+2)) == 0:   #3
											realmove.append((nm1[0]-2,nm1[1]+2))

										if brd.get((nm1[0]-2,nm1[1]-2)) == 0:   #3
											realmove.append((nm1[0]-2,nm1[1]-2))
				
				if brd.get((m[0]-2,m[1]-2)) == 0:     #1
					realmove.append((m[0]-2,m[1]-2))
					newMoves = possibleMoves((m[0]-2,m[1]-2))
					for nm in newMoves:
						if brd.get(nm).color != self.color:
				
							if brd.get((nm[0]-2,nm[1]+2)) == 0:     #2
								realmove.append((nm[0]-2,nm[1]+2))
								newMoves1 = possibleMoves((nm[0]-2,nm[1]+2))
								for nm1 in newMoves1:
									if brd.get(nm1).color != self.color:
										if brd.get((nm1[0]-2,nm1[1]+2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]+2))

										if brd.get((nm1[0]-2,nm1[1]-2)) == 0:   #3
											realmove.append((nm1[0]-2,nm1[1]-2))
				
							if brd.get((nm[0]-2,nm[1]-2)) == 0:    #2
								realmove.append((nm[0]-2,nm[1]-2))
								newMoves1 = possibleMoves((nm[0]-2,nm[1]-2))
								for nm1 in newMoves1:
									if brd.get(nm1).color != self.color:
										if brd.get((nm1[0]-2,nm1[1]+2)) == 0:   #3
											realmove.append((nm1[0]+2,nm1[1]+2))

										if brd.get((nm1[0]-2,nm1[1]-2)) == 0:   #3
											realmove.append((nm1[0]-2,nm1[1]-2))

		return realmove

	def isKing(self):
		if self.color == "black":
			if self.position[0] == 8:
				return True
		else:
			if self.position[0] == 1:
				return True
		return False
