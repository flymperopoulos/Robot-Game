import cv2
import numpy as np
import picamera
import time

def getState():
	"""takes the picture from the PiCamera and saves it to the desktop"""
	camera = picamera.PiCamera()
	time.sleep(1) 
	camera.capture('/home/pi/Robot-Game/res/boardStateTest.jpg')
	camera.close()

def getImage(filename):
	"""returns the img"""
	return cv2.imread(filename)

def getContour(img):
	"""returns the contour of the board"""
	# grayscaled image
	imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	# finding the contour list
	ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	return contours

def getColor(img):
	"""returns the color contour of the board"""

	#color ranges for each color
	lower_red = np.uint8([0, 155, 0])
	upper_red = np.uint8([10, 255, 255])
	lower_blue = np.uint8([100,150,0])
	upper_blue = np.uint8([140,255,255])
	lower_green = np.uint8([40, 110, 110])
	upper_green = np.uint8([70, 255, 255])

	# finding the contour for the list
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_red, upper_red)
	ret,thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	return contours

def getColorList(contours):
	"""returns the list of the coordinate points where the human's pieces are"""
	color = []   # center points of the colors
	for cnt in contours:
		m = cv2.moments(cnt)

		if m['m00'] > 700 and m['m00'] >500:
			x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
			color.append((x,y))

	color = list(set(color))

	return color

def getTriangleList(contours):
	"""returns the list of the coordinate points where the red pieces are"""
	i = 0
	color = []   # center points of the colors
	for cnt in contours:
		m = cv2.moments(cnt)

		if m['m00'] < 850 and m['m00'] > 500:
			x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
			i= i+1
			color.append((x,y))

	color = list(set(color))

	return color


def getBoardList(contours):
	"""returns the list of coordinate points where all of the pieces are and the center and corner points"""
	centerX = 0
	centerY = 0
	cornerX = 0
	cornerY = 0
	
	c = 0
	big = 0
	mom = 0
	pieces = [] 
	for cnt in contours:
	
		m = cv2.moments(cnt)
		# finding the board and setting center and corner coordinates
		if m['m00'] >100000 and m['m00'] <220000:
			centerX, centerY = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
			cornerX, cornerY = cnt[0][0][0], cnt[0][0][1]
		#adding black pieces 
		if m['m00'] < 1300 and m['m00'] > 1000:
			x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
			pieces.append((x,y))
		#adding triangle pieces
		if m['m00'] < 850 and m['m00'] > 500:		
			x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
			pieces.append((x,y))

	pieces = list(set(pieces))

	return pieces, centerX, centerY, cornerX, cornerY

def imageToBoard(brdList, centerX, centerY, cornerX, cornerY):
	"""returns dictionary of the board state"""
	brdDict = {}
	xtemp=0
	ytemp =0 
	# finding out the height and width of each square
	gridW = (centerX - cornerX)*2/8
	gridH = (centerY - cornerY)*2/8
	for p in brdList:
		xtemp = (p[0]-cornerX)/gridW +1
		ytemp = (p[1]-cornerY)/gridH +1
		if xtemp < 9 and ytemp < 9  and xtemp >0  and ytemp > 0:
			# checking if each pieces are within the board
			brdDict[xtemp, ytemp] = 1

	return brdDict
	
def imageToBoardColor(brdDict, clrList, centerX, centerY, cornerX, cornerY):
	"""returns the list of coordinate points where red pieces are"""
	clrDict = {}
	xtemp = 0
	ytemp = 0
	gridW = (centerX - cornerX)*2/8
	gridH = (centerY - cornerY)*2/8 
	for p in clrList:
		xtemp = (p[0]-cornerX)/gridW +1
		ytemp = (p[1]-cornerY)/gridH +1
		if (xtemp, ytemp) in brdDict:
			# finding out the red pieces
			clrDict[xtemp, ytemp] = "R"
	return clrDict

def grab_pieces(board,player):
    """finds all of the pieces on the board"""
    pieces = []
    for i in range(1,9):
        for j in range(1,9):
            if board[(i,j)] != 0 and board[(i,j)].color == player:
                pieces.append(board[(i,j)])
    return pieces

def picam_main(brd):
	"""Main method that runs everything"""
	try:
		getState()
		img = getImage('/home/pi/Robot-Game/res/boardStateTest.jpg')
		brdCountour = getContour(img)
		# generating the lists from the picture
		brdList, centerX, centerY, cornerX, cornerY = getBoardList(brdCountour)
		clrList = getTriangleList(brdCountour)
		# generating the dictionary from the lists
		brdDict = imageToBoard(brdList, centerX, centerY, cornerX, cornerY)
		clrDict = imageToBoardColor(brdDict, clrList ,centerX, centerY, cornerX, cornerY)

		print brdList
		print clrList
		print brdDict, len(brdDict)
		print clrDict, len(clrDict)
		w_pieces = grab_pieces(brd,'W')
		b_pieces = grab_pieces(brd,'B')

		# returning None if the board is not ready
		if len(clrDict) == len(w_pieces):
			pn = len(w_pieces) + len(b_pieces)
			if  pn == len(brdDict):
				return brdDict, clrDict
		else:
			return None
	except:
		return None

def pic():
	getState()
	
if __name__ in "__main__":
	#picam_main()
	pic()
