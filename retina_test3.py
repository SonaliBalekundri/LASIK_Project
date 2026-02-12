import cv2 as cv
import numpy as np
'''Code To read an Image and display'''
img = cv.imread('Patient2.jpg')
cv.imshow('Actual Image',img)


#Cut Image
cut_image =img[412:667, 833:1088]
cv.imshow("Cut Image",cut_image)

img_gray=cv.cvtColor(cut_image,cv.COLOR_BGR2LAB)
l,a,b=cv.split(img_gray)
cv.imshow('Scaled Image', b)

#create a window
cv.namedWindow('Scaling')
cv.resizeWindow('Scaling', 700, 45)

#create a track bar
def trackbar(x):
    reti = cv.getTrackbarPos('Retina','Scaling')
    ret,thresh= cv.threshold(b,125,255, cv.THRESH_BINARY)
    contours, hierarchies= cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_TC89_L1)
    cv.drawContours(b,contours,-1, (255,255,0), 1)
    cv.imshow('Scaled Image', b)
    cv.drawContours(cut_image,contours,-1, (0,255,0), 1)
    cv.imshow('Scaled Original Image', cut_image)
    print(reti)
    return reti
cv.createTrackbar('Retina','Scaling', 65, 200,trackbar)


cv.waitKey(0)