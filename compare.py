from checkerPiece import *
import cv2

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

dic = {(1,1):CheckerPiece("W", (1,1), "1"), (5,4):CheckerPiece("W", (5,4), "2"), (1,4):CheckerPiece("W", (1,4), "3"),
(2,2):CheckerPiece("B", (2,2), "1"), (3,5):CheckerPiece("B", (3,5), "2")}

dic2 = {(1,1):CheckerPiece("W", (1,1) , "0"), (2,1):CheckerPiece("W", (2,1), "0"), (1,4):CheckerPiece("W", (1,4), "0"),
(2,2):CheckerPiece("B", (2,2), "0"), (3,5):CheckerPiece("B", (3,5), "0")}

d = compareBoard(dic, dic2)

for key, value in d.iteritems():
	print key,value.color, value.position, value.name

# cam = cv2.VideoCapture(0)
# while(True):


# 	ret, frame = cam.read()
# 	cv2.imshow('video', frame)


# 	if cv2.waitKey(1) & 0xFF == ord(' '):
# 		break

# cv2.imwrite("res/red.jpg", frame) 
# cam.release()
# cv2.destroyAllWindows()


# print CheckerPiece("W", (1,1), "2").name