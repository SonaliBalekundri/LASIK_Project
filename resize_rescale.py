import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # THIS METHOD WILL WORK FOR IMAGES, VIDEOS & LIVE VIDEOS   
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# def changeRes(width,height):
#     # THIS METHOD WILL WORK ONLY FOR LIVE VIDEOS
#     capture.set(3,width)
#     capture.set(4,height)


# RESIZING & RESCALING IMAGES
img=cv.imread('retina7.jpg')
resized_img=rescaleFrame(img)
cv.imshow('eye', img)
cv.imshow('eye Resized', resized_img)
cv.waitKey(0)


# RESIZING & RESCALING VIDEOS

# capture = cv.VideoCapture('videos/centnary.mp4')
# while True:
#     isTrue,frame=capture.read()
#     frame_resized = rescaleFrame(frame)
#     cv.imshow('Video',frame)
#     cv.imshow('Video Resized',frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows
