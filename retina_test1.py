import cv2 as cv
import numpy as np
'''Code To read an Image and display'''
img = cv.imread('images/Patient3.jpg')
# cv.imshow('Actual Image',img)


#Cut Image
cut_image =img[412:667, 833:1088]
# cv.imshow("Cut Image",cut_image)
# img_resize=cv.resize(img,(1280,720))
img_gray=cv.cvtColor(cut_image,cv.COLOR_BGR2LAB)
l,a,b=cv.split(img_gray)
# cv.imshow('Scaled Image', b)

# blank=np.zeros(img.shape,dtype='uint8')
# cv.imshow('Blank',blank)
# canny = cv.Canny(b, 125,175)
blur = cv.GaussianBlur(b, (5, 5),cv.BORDER_DEFAULT)
ret,thresh= cv.threshold(blur,125,255, cv.THRESH_BINARY)
contours, hierarchies= cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_TC89_L1)

# calculate moments of binary image
M = cv.moments(thresh)

# calculate x,y coordinate of center
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

# put text and highlight the center
cv.circle(cut_image, (cX, cY), 3, (255, 255, 255), -1)
cv.putText(cut_image, "Origin", (cX - 25, cY - 25),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# display the image
# cv.imshow("center Image", cut_image)

cv.drawContours(blur,contours,-1, (255,255,0), 1)
# cv.imshow('Scaled Image', blur)

cv.drawContours(cut_image,contours,-1, (0,255,0), 2)
# cv.imshow('Scaled Original Image', cut_image)

for i in contours:
   M = cv.moments(i)
   if M['m00'] != 0:
      cx = int(M['m10']/M['m00'])
      cy = int(M['m01']/M['m00'])
      cv.drawContours(cut_image, [i], -1, (0, 255, 0), 2)
      cv.circle(cut_image, (cx, cy), 2, (255, 255, 255), -1)
      cv.putText(cut_image, "center", (cx - 20, cy - 20),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
   # print(f"x: {cx} y: {cy}")
   
cv.imshow("image.png", cut_image)

cv.waitKey(0)

