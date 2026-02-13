import cv2 as cv
import numpy as np
'''Contour -> means the boundaries of objects,
the line or curve that joins the continuous points
along the boundaries of an object.
They are not the same as edges.
Contours are useful tools when you get into shape
analysis and object detection.'''

img=cv.imread('images/retina26.jpg')
cv.imshow('eye', img)

'''Using blank image so that we can draw the 
contours on this blank image.'''
blank=np.zeros(img.shape,dtype='uint8')
# cv.imshow('Blank',blank)

gray_temp=cv.cvtColor(img,cv.COLOR_BGR2LAB)
l,a,gray=cv.split(gray_temp)
# cv.imshow('Gray',gray)

# blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

# canny=cv.Canny(blur,125,175)
# cv.imshow('Canny',canny)

'''Threshold -> it will take gray image & threshold 
value & maximum value. Threshold looks at an image
& tries to binarize that image.
Which means if a particular pixel is below 125,
if the density of that pixel is below 125 then it
is going to be set to zero or blank. If above 125,
it is set to white.'''
ret, thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0) 




