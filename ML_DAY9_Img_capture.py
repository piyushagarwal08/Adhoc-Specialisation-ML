#!/usr/bin/python3

import cv2

#starting camera
capture = cv2.VideoCapture(0)   # 0 stands for internal camera or first camera
# if i had external camera it should be 1 , 2 , 3 etc
if capture.isOpened():              # shows the status of camera
    print('Camera is ready')
else:
    print('Check your web cam drivers')
# Now we can read data from camera
status,img = capture.read()
status1,img1 = capture.read()
# Now showing
cv2.imshow('working',img)
cv2.imshow('working1',img1)
cv2.waitKey(0)

#to close camera
#cv2.release()
