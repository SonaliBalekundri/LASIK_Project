import cv2 as cv
import matplotlib.pyplot as plt

# READING IMAGE
img=cv.imread('images/retina26.jpg')
cv.imshow('eye', img)


'''By default OpenCV reads images in BGR form.'''

'''COLOR SPACES -> spaces of colors, a system of
representing an array of colors.
Eg: RGB ( the color model of three-color image 
displays using red, green, and blue light), 
Grayscale (a range of grey shades from white to 
black, as used in a monochrome display or printout.), 
HSV (for hue, saturation, value; also known as HSB, 
for hue, saturation, brightness), 
LAB (L*: Lightness, a*: Red/Green Value, b*: Blue/Yellow Value), 
LUV (where L stands for luminance, whereas U and V represent 
chromaticity values of color images), 
HSL (for hue, saturation, lightness), etc'''

'''BGR to Grayscale'''
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)
# cv.imshow('HSV',hsv)

'''BGR to LAB'''
lab1=cv.cvtColor(img,cv.COLOR_LBGR2LAB)
l,a,b=cv.split(lab1)
cv.imshow('LAB1',lab1)
cv.imshow('LAB5',b)

# lab2=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow('LAB2',lab2)

# lab3=cv.cvtColor(img,cv.COLOR_LBGR2Lab)
# cv.imshow('LAB3',lab3)

# lab4=cv.cvtColor(img,cv.COLOR_BGR2Lab)
# cv.imshow('LAB3',lab4)

'''BGR to LUV'''
luv1=cv.cvtColor(img,cv.COLOR_LBGR2LUV)
cv.imshow('LUV1',luv1)

# luv2=cv.cvtColor(img,cv.COLOR_BGR2LUV)
# cv.imshow('LUV2',luv2)

'''BGR to RGB'''
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()


'''BGR to HSL'''
# hsl=cv.cvtColor(img,cv.COLOR_BGR2HLS)
# cv.imshow('HSL',hsl)




cv.waitKey(0) 

