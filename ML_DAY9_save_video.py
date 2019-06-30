#!/usr/bin/python3
import cv2

# starting camera
capture = cv2.VideoCapture(0)

#added a plugin 
plugin = cv2.VideoWriter_fourcc(*'XVID') # xvid is a plugin to support avi and mp4 extension

#Video writer takes (file-name ,plugin, no-of-frames-per-second,(width-of-camera-frame,height-of-camera-frame)
output = cv2.VideoWriter('file-name.mkv',plugin,20,(640,480))

while capture.isOpened():
    status,frame = capture.read()
    cv2.imshow('window1',frame)
    output.write(frame)
    if cv2.waitKey(10) == 13:
        break
cv2.destroyAllWindows()
capture.release()
