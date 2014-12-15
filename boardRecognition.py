import cv2
import numpy as np
# from matplotlib import pyplot as plt

# cam = cv2.VideoCapture(0)
# while(True):


# 	ret, frame = cam.read()
# 	cv2.imshow('video', frame)


# 	if cv2.waitKey(1) & 0xFF == ord(' '):
# 		break

# cv2.imwrite("res/vidMovedCheckers.png", frame) 
# cam.release()
# cv2.destroyAllWindows()

# img = cv2.imread('circle.jpg',0)
# edges = cv2.Canny(img,100,200)

# im = cv2.imread('res/boardStateTwo.jpg')
# im = cv2.imread('res/boardStateOne.jpg') 
im = cv2.imread('res/boardStateTest.jpg')
# im = cv2.imread('res/red.jpg')
# print im

height, width = im.shape[:2]
print height, width
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

# hsv bounds for red blue and green
 
lower_red = np.uint8([0, 155, 0])
upper_red = np.uint8([10, 255, 255])

lower_blue = np.uint8([100, 50, 50])
upper_blue = np.uint8([140, 255, 255])
lower_green = np.uint8([40, 110, 110])
upper_green = np.uint8([70, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
output = cv2.bitwise_and(im, im, mask = mask)
# print len(np.where(mask != 0)[0])
# print len(np.where(mask != 0)[0])

"""
 contour of the red color
"""
# ret,thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# i = 0
# color = []   # center points of the colors
# for cnt in contours:
# 	m = cv2.moments(cnt)

# 	if m['m00'] > 20:
# 		x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
# 		i= i+1
# 		color.append((x,y))
# 		cv2.circle(mask,(x,y),3,(0,255,0),2)
# # print i
# color = list(set(color))


def checkColorArea():
	pass

# cv2.imshow("im", im)
# cv2.imshow("red", mask)

"""
	finding the contour
"""
edges = cv2.Canny(imgray,100,200)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cornerX, cornerY = 0 ,0
centerX, centerY = 0 ,0
c = 0
big = 0
mom = 0
pieces = []
triangle = []
print len(contours)
for cnt in contours:
	m = cv2.moments(cnt)

	# print cnt, len(cnt)
	print m['m00']
	if m['m00'] > big:
		big = m['m00']
		c = cnt
		mom = m
		# cv2.circle(imgray,(c[0][0][0],c[0][0][1]),10,(0,255,0),2)


	if m['m00'] >100000 and m['m00'] <220000:
		centerX, centerY = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
		# print cnt[0], cnt[0][0][0], cnt[0][0][1]
		cornerX, cornerY = cnt[0][0][0], cnt[0][0][1]

		cv2.circle(imgray,(cornerX, cornerY),10,(0,255,0),2)
		cv2.circle(imgray,(centerX, centerY),10,(0,255,0),2)
		
	if m['m00'] < 850 and m['m00'] > 500:
		x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
		triangle.append((x,y))
		pieces.append((x,y))
		cv2.circle(imgray,(x,y),3,(0,255,0),2)

	if m['m00'] < 1300 and m['m00'] > 1000:
		x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
		pieces.append((x,y))
		cv2.circle(imgray,(x,y),3,(0,255,0),5)

pieces = list(set(pieces))
triangle = list(set(triangle))

# print big, c, mom

img = im
cv2.imshow('im', im)
cv2.drawContours(img, contours, -1, (0,0,0), 2)
cv2.imshow('stuff', imgray)
cv2.imshow('img', img)



gridW = (centerX - cornerX)*2/8
gridH = (centerY - cornerY)*2/8
print gridW, gridH
print centerX, centerY
print cornerX, cornerY
print pieces

d = {}
xtemp=0
ytemp =0 
for p in pieces:
	xtemp = (p[0]-cornerX)/gridW +1
	ytemp = (p[1]-cornerY)/gridH +1
	if xtemp < 9 and ytemp < 9  and xtemp >0  and ytemp > 0:
		d[xtemp, ytemp] = 1
print d, len(d)

dc = {}
xtemp=0
ytemp =0 
for p in triangle:
	xtemp = (p[0]-cornerX)/gridW +1
	ytemp = (p[1]-cornerY)/gridH +1
	if (xtemp, ytemp) in d:
		dc[xtemp, ytemp] = "R"
print dc, len(dc)

cv2.waitKey(0)