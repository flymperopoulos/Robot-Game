import cv2
import numpy as np
# from matplotlib import pyplot as plt



# cam = cv2.VideoCapture(0)
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cam.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('video',frame)
    
#     if cv2.waitKey(1) & 0xFF == ord(' '):
#         break
    
# # When everything done, release the capture
# cam.release()
# cv2.destroyAllWindows()

# img = cv2.imread('circle.jpg',0)
# edges = cv2.Canny(img,100,200)

# im = cv2.imread('res/Checkers.png')
im = cv2.imread('res/board.jpg')

height, width = im.shape[:2]
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

lower_red = np.uint8([0, 155, 0])
upper_red = np.uint8([10, 255, 255])
lower_blue = np.uint8([100,150,0])
upper_blue = np.uint8([140,255,255])
lower_green = np.uint8([40, 110, 110])
upper_green = np.uint8([70, 255, 255])

# mask = cv2.inRange(im, lower_red, upper_red)
mask = cv2.inRange(hsv, lower_red, upper_red)
output = cv2.bitwise_and(im, im, mask = mask)
# print len(np.where(mask != 0)[0])
print len(np.where(mask != 0)[0])
# print np.where(mask != 0)[0]

ret,thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
i = 0
for cnt in contours:
	m = cv2.moments(cnt)

	if len(cnt) >20: #and len(cnt)< 50:
		if m['m00']!= 0 and  m['m00'] > 20:
			x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
			i= i+1
			cv2.circle(mask,(x,y),3,(0,255,0),2)
# print i

def checkColorArea():
	pass
# print (np.where(mask[np.where(mask != 0)] != 255))

moment = cv2.moments(mask)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
	m = cv2.moments(cnt)

	# print cnt, cnt[0], len(cnt)
	if len(cnt) >20: #and len(cnt)< 50:
		if m['m00']!= 0:
			x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
			cv2.circle(im,(x,y),3,(0,255,0),2)

# cv2.imshow("images", np.hstack([im, output]))

cv2.imshow("im", im)
cv2.imshow("red", mask)

# print height, width
# gridH = height/8
# gridW = width/8
# print height - gridH/2

ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print len(contours)
pieces = [] 
for cnt in contours:
	m = cv2.moments(cnt)

	# print cnt, cnt[0], len(cnt)
	if len(cnt) >20: #and len(cnt)< 50:
		if m['m00']!= 0:
			x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
			pieces.append((x,y))
			cv2.circle(imgray,(x,y),3,(0,255,0),2)
# m1 = cv2.moments(contours[0])
# x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
# print x,y
# cv2.circle(imgray,(x,y),10  ,(0,255,0),2)
# cv2.drawContours(im, contours, -1, (0,255,0), 1)
# cv2.imshow('stuff', imgray)
pieces = list(set(pieces))
# print pieces, len(pieces)

cv2.waitKey(0)