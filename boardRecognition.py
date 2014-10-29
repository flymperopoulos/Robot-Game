import cv2
import numpy as py
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
# height, width = img.shape[:2]
# print height,width
# edges = cv2.Canny(img,100,200)
# moment = cv2.moments(edges)

# if moment['m00'] != 0:
#     bx,by = int(moment['m10']/moment['m00']), int(moment['m01']/moment['m00'])
#     cv2.circle(edges,(bx,by),30,255,-1)
#     print bx,by

# cv2.imshow('edges', edges)
# cv2.imshow('stuff', img)

im = cv2.imread('Checkers.png',0)
height, width = im.shape[:2]
# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(im,100,200)
print height, width
gridH = height/8
gridW = width/8
print height - gridH/2
ret,thresh = cv2.threshold(edges,127,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
print len(contours)
pieces = {}
for cnt in contours:
	m = cv2.moments(cnt)
	# ellipse = cv2.fitEllipse(cnt)
	# cv2.ellipse(im,ellipse,(0,255,0),2)
	if m['m00']!= 0:
		x,y = int(m['m10']/m['m00']), int(m['m01']/m['m00'])
		# print x,y
		if pieces.has_key((x,y)):
			pieces[(x,y)] = pieces[(x,y)]+1
		else:
			pieces[(x,y)] = 1
		# cv2.circle(edges,(x,y),3,(255,255,0),1)
		cv2.circle(im,(x,y),3,(0,255,0),2)
p = []
print pieces
for val in pieces:
	if pieces[val] > 1:
		p.append(val)
		cv2.circle(edges,val,3,(255,255,0),1)
		# cv2.circle(im,val,3,(0,255,0),2)
print p

# one = pieces
# for tup in pieces:
# 	for tup1 in one:

# print rpieces


		
cv2.drawContours(im, contours, -1, (0,255,0), 1)
cv2.imshow('stuff', im)
cv2.imshow('edge', edges)

cv2.waitKey(0)
