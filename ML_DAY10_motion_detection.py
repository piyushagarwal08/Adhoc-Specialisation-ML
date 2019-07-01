#!/usr/bin/python3
import math
import cv2

#starting camera
capture = cv2.VideoCapture(0)

# take 1
image1 = capture.read()[1]

# take 2
image2 = capture.read()[1]

# take 3
image3 = capture.read()[1]

# to make motion detection more perfect (gray color ignores light,sun,dust etc)
gray1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)  # converting into gray

gray2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)  # converting into gray

gray3=cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY)  # converting into gray

# Now creating image differentiator 
def img_diff(x,y,z):
    # difference between x and y or gray1 and gray2
    d1 = cv2.absdiff(x,y)
    # difference between y and z or gray2 and gray3
    d2 = cv2.absdiff(y,z)
    # difference between d1 and d2 
    d3 = cv2.bitwise_and(d1,d2)
    return d3

# now apply function
while capture.isOpened():
    status,frame = capture.read()
    motion= img_diff(gray1,gray2,gray3)
    # replacing image frame
    gray1 = gray2
    gray2 = gray3
    gray3 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # passing live image 2 gray 3
    cv2.imshow('live',frame)
    cv2.imshow('motion image',motion)
    if  cv2.waitKey(10) == 13:
        break
cv2.destroyAllWindows()
capture.release()
